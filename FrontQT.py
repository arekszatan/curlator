import json
import logging
import os
import sys
from datetime import datetime
import qasync
from PySide6 import QtWidgets
from PySide6.QtWidgets import QFileDialog
from PySide6.QtCore import QTimer
import asyncioClass
from MainWindow import Ui_MainWindow
from curlParser import CurlParser


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow, asyncioClass.Asyncio):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Curlator")

        # Timer to live logging
        self.timer = QTimer()
        self.timer.timeout.connect(self.liveLogTimerFunction)
        self.timerLocal = QTimer()
        self.timerLocal.timeout.connect(self.liveLogTimerFunctionLocal)

        # Variable
        self.data = None
        self.localHostFlag = bool
        self.ip = str
        self.username = str
        self.password = str
        self.actualCurl = str
        self.filePath = str
        self.localAPP = bool

        # Set list of parameter for curl
        self.listToJson = []
        self.listOfParametr = []
        self.listOfParametr.append([self.p1, self.p1label])
        self.listOfParametr.append([self.p2, self.p2label])
        self.listOfParametr.append([self.p3, self.p3label])
        self.listOfParametr.append([self.p4, self.p4label])
        self.listOfParametr.append([self.p5, self.p5label])
        self.listOfParametr.append([self.p6, self.p6label])
        self.listOfParametr.append([self.p7, self.p7label])
        self.listOfParametr.append([self.p8, self.p8label])
        self.listOfParametr.append([self.p9, self.p9label])
        self.listOfParametr.append([self.p10, self.p10label])
        self.setInitStartValue()

        # Curl parser
        self.CurlParser = CurlParser()
        self.setConnectionObject()

    def setInitStartValue(self):
        self.stackedWidget.setCurrentIndex(0)
        self.maxLineLogLive.setValue(100)
        self.fontSize.setValue(12)
        self.countLineForCurl.setValue(20)
        self.timerPHSLive.setValue(500)
        self.delayForCurlResponse.setValue(500)
        for param, label in self.listOfParametr:
            param.setVisible(False)
            label.setVisible(False)

    def setConnectionObject(self):

        # Connect of push button to function
        self.openJsonButton.clicked.connect(self.openJson)
        self.startLiveLog.clicked.connect(self.stratLogPHS)
        self.stopLiveLog.clicked.connect(self.stopLogPHS)
        self.sendPushButton.clicked.connect(self.sendCurlButton)
        self.backPushButton.clicked.connect(self.backToCurls)
        self.pathForLogButton.clicked.connect(self.setPathForLog)

        # Connect double-click list to function
        self.curlList.itemDoubleClicked.connect(self.listJsonDoubleClick)

        # Connect signal from asyncioClass
        self.error.connect(self.errorSSHFirstConnect)
        self.connectionOK.connect(self.loginSSH)
        self.startedSendCurl.connect(self.startedSendCurlFun)
        self.finishedSendCurl.connect(self.finishedSendCurlFun)
        self.outputCmd.connect(self.outputCmdFun)
        self.errorSendCurl.connect(self.errorSendCurlFun)
        self.curlCallBackSignal.connect(self.curlCallBackFun)
        self.logLocalHostSignal.connect(self.logLocalHostFun)
        self.logLocalHostSignalCurl.connect(self.logLocalHostCurlFun)

        # Connect text change line edit to end curl
        for param, label in self.listOfParametr:
            param.textChanged.connect(self.setOnlyActulCurl)

    def openJson(self):  # Function to open file dialog, decode JSON file and start local or ssh version
        logging.info(f'Opening QFileDialog ...')
        file = QFileDialog.getOpenFileName(self, 'Open file', 'C:\\', "*")
        path = file[0]
        try:
            logging.info(f'Trying decode to JSON file {file[0]}')
            f = open(path, "r", encoding="utf-8")
            self.data = json.load(f)
            f.close()
            if self.data['ip'] == "localhost" or self.data['ip'] == "":
                self.localAPP = True
                self.setWindowTitle("Curlator dla sesji lokalnej")
                logging.info("Starting local Curlator ...")
                self.infoHomePage.setText(f'Curlator startuje dla localhost ...')
                self.loginLocal()
            else:
                self.localAPP = False
                self.setWindowTitle(f'Curlator dla {self.data["ip"]}')
                logging.info("Starting ssh Curlator ...")
                self.infoHomePage.setText(f'Curlator startuje dla {self.data["ip"]} ...')
                self.checkConnectionSSH(self.data['ip'], self.data['username'], self.data['password'])
        except:
            logging.exception(f'Can not open and decoding json file {path}')
            self.infoHomePage.setText(f'Wystąpil błąd podczas dekodowania pliku JSON !!!')

    def errorSSHFirstConnect(self):  # Error when check first connect ssh
        self.infoHomePage.setText(f'Błąd podczas łącznia do {self.data["ip"]}')
        logging.error(f'Błąd podczas łącznia do {self.data["ip"]}')

    def loginSSH(self):  # First response of ssh is success and change Widget to list of Curls
        logging.info(f'Logging to {self.data["ip"]} is succesed')
        self.runAsyncioCmdLiveLog(self.data['ip'], self.data['username'], self.data['password'])
        self.stackedWidget.setCurrentIndex(1)
        for i in self.data['curls']:
            self.listToJson.append(i['curl'])
            self.curlList.addItem(i['shortInfo'])

    def loginLocal(self):
        self.stackedWidget.setCurrentIndex(3)
        for i in self.data['curls']:
            self.listToJson.append(i['curl'])
            self.curlList.addItem(i['shortInfo'])

    def setPathForLog(self):
        logging.info(f'Opening QFileDialog ...')
        try:
            self.filePath = QFileDialog.getExistingDirectory(self, 'Open a folder', 'C:\\')
            date = datetime.today().strftime('%Y_%m_%d_logging.log')
            logging.info(f'Log file patch {self.filePath}/{date}')
            self.pathInfoLabel.setText(f'{self.filePath}/{date}')
            self.stackedWidget.setCurrentIndex(1)

        except:
            self.pathInfoLabel.setText(f'Nie udało sie wybrac odpowiedniego folderu')
            logging.error(f'Nie udało sie wybrac odpowiedniego folderu')

    def logLocalHostFun(self, outLog):
        self.logPHSLive.setFontPointSize(self.fontSize.value())
        self.logPHSLive.clear()
        lenLogs = len(outLog) - self.maxLineLogLive.value()
        i = 0
        for log in outLog:
            if i >= lenLogs:
                ind = 0
                findingLogData = 0
                while ind < 3:
                    findingLogIndex = log[findingLogData:].find(":")
                    findingLogData += findingLogIndex + 1
                    ind += 1
                findingLogData = findingLogData
                findingLogInfo = log[findingLogData + 2:].find(":")

                colorInfo = ['#0ccaf0', '#fcf403', '#fc0303']  # [INFO, DBUG, WARN]
                info = log[findingLogData:findingLogData + 2 + findingLogInfo]

                classNameStart = findingLogData + 2 + findingLogInfo
                classNameStart = log[classNameStart:].find(".") + classNameStart
                classNameStop = log[classNameStart:].find(":") + classNameStart
                className = log[classNameStart:classNameStop]
                flagaLog = True
                if info == "INFO":
                    colorInfo = colorInfo[0]
                elif info == "DBUG":
                    colorInfo = colorInfo[1]
                elif info == "WARN":
                    colorInfo = colorInfo[2]
                else:
                    flagaLog = False
                log = log.replace('<', '&lt;')
                log = log.replace('>', '&gt;')
                if self.grepLineEdit.text() == "":
                    if flagaLog:
                        log = log[:-1]
                        if log != "\n":
                            self.logPHSLive.append(f'<head><meta charset="utf-8"></head>'
                                                   f'<body>'
                                                   f'<span style="font-size: {self.fontSize.value()}pt;">'
                                                   f'<span style="color:#317507;">'
                                                   f'{log[:findingLogData]}'
                                                   f'</span>'
                                                   f'<span style="color:{colorInfo};">'
                                                   f'{info}'
                                                   f'</span>'
                                                   f'<span style="color:">'
                                                   f'{log[findingLogData + 2 + findingLogInfo:classNameStart]}'
                                                   f'</span>'
                                                   f'<span style="color:#0ccaf0;">'
                                                   f'{className}'
                                                   f'</span>'
                                                   f'{log[classNameStop:]}'
                                                   f'</span>'
                                                   f'</body>')
                        else:
                            if log != "\n":
                                if log.find('Exception') != -1 or log.find('at ') != -1:
                                    self.logPHSLive.append(
                                        f'<span style="font-size: {self.fontSize.value()}pt; color:#fc0303;">'
                                        f'{log}'
                                        f'</span>')
                                else:
                                    self.logPHSLive.append(
                                        f'<span style="font-size: {self.fontSize.value()}pt; color:#0ccaf0;">'
                                        f'{log}'
                                        f'</span>')
                else:
                    findingLog = log.find(self.grepLineEdit.text())
                    if findingLog != -1:
                        newLogBefore = log[:findingLog]
                        logFind = log[findingLog:findingLog + len(self.grepLineEdit.text())]
                        newLogAfter = log[findingLog + len(self.grepLineEdit.text()):]
                        newLogAfter = newLogAfter[:-1]
                        if log != "\n":
                            self.logPHSLive.append(f'<span style="font-size: {self.fontSize.value()}pt;">'
                                                   f'{newLogBefore}'
                                                   f'<span style="color:red;">'
                                                   f'{logFind}'
                                                   f'</span>'
                                                   f'{newLogAfter}'
                                                   f'</span>')

            i += 1
        if self.logPHSLive.toPlainText() == "":
            self.logPHSLive.setFontPointSize(self.fontSize.value())
            self.logPHSLive.setText(f'Brak logów dla {self.grepLineEdit.text()}')

    def logLocalHostCurlFun(self, outLog):
        self.logAfterCurl.setFontPointSize(self.fontSize.value())
        lenLogs = len(outLog)
        i = lenLogs
        findedLog = False
        while i >= 0:
            if outLog[i - 1].find(" 127.0.0.1: Executing request") != -1:  # " 127.0.0.1: Executing request"
                findedLog = True
                break
            i -= 1
        findLine = i
        if findedLog:
            firstLine = True
            while i < findLine + self.countLineForCurl.value() and i <= lenLogs:
                log = outLog[i - 1][:-1]
                log = log.replace('<', '&lt;')
                log = log.replace('>', '&gt;')
                ind = 0
                findingLogData = 0
                while ind < 3:
                    findingLogIndex = log[findingLogData:].find(":")
                    findingLogData += findingLogIndex + 1
                    ind += 1
                findingLogData = findingLogData
                findingLogInfo = log[findingLogData + 2:].find(":")

                colorInfo = ['#0ccaf0', '#fcf403', '#fc0303']  # [INFO, DBUG, WARN]
                info = log[findingLogData:findingLogData + 2 + findingLogInfo]
                classNameStart = findingLogData + 2 + findingLogInfo
                classNameStart = log[classNameStart:].find(".") + classNameStart
                classNameStop = log[classNameStart:].find(":") + classNameStart
                className = log[classNameStart:classNameStop]
                flagaLog = True
                if info == "INFO":
                    colorInfo = colorInfo[0]
                elif info == "DBUG":
                    colorInfo = colorInfo[1]
                elif info == "WARN":
                    colorInfo = colorInfo[2]
                else:
                    flagaLog = False
                if flagaLog:
                    if firstLine:
                        self.logAfterCurl.append(f'<span style="font-size: {self.fontSize.value()}pt; color:#ab5757;">'
                                                 f'{log}'
                                                 f'</span>')
                        firstLine = False
                    else:
                        self.logAfterCurl.append(f'<head><meta charset="utf-8"></head>'
                                                 f'<body>'
                                                 f'<span style="font-size: {self.fontSize.value()}pt;">'
                                                 f'<span style="color:#317507;">'
                                                 f'{log[:findingLogData]}'
                                                 f'</span>'
                                                 f'<span style="color:{colorInfo};">'
                                                 f'{info}'
                                                 f'</span>'
                                                 f'<span style="color:">'
                                                 f'{log[findingLogData + 2 + findingLogInfo:classNameStart]}'
                                                 f'</span>'
                                                 f'<span style="color:#0ccaf0;">'
                                                 f'{className}'
                                                 f'</span>'
                                                 f'{log[classNameStop:]}'
                                                 f'</span>'
                                                 f'</body>')
                else:
                    if log.find('Exception') != -1 or log.find('at ') != -1:
                        self.logAfterCurl.append(f'<span style="font-size: {self.fontSize.value()}pt; color:#fc0303;">'
                                                 f'{log}'
                                                 f'</span>')
                    else:
                        self.logAfterCurl.append(f'<span style="font-size: {self.fontSize.value()}pt; color:#0ccaf0;">'
                                                 f'{log}'
                                                 f'</span>')

                i += 1
        else:
            self.logAfterCurl.setFontPointSize(self.fontSize.value())
            self.logAfterCurl.append(f'Nie znalazłem call back dla curla')

    def liveLogTimerFunctionLocal(self):
        date = datetime.today().strftime('%Y_%m_%d_logging.log')
        self.readFileOfLogs(f'{self.filePath}/{date}')

    def listJsonDoubleClick(self):  # Double-click on curl in list of curls
        self.stackedWidget.setCurrentIndex(2)
        logging.info(f'List of Json was clicked and value of '
                     f'row is {str(self.listToJson[self.curlList.currentIndex().row()])}')
        self.actualCurl = str(self.listToJson[self.curlList.currentIndex().row()])
        self.checgedCurl.setText(self.actualCurl)
        self.setActualCurlandParam(self.actualCurl)

    def closeEvent(self, event):  # Action to click right top exit button (os_exit->closing all threads)
        logging.warning("Aplication was closed !!!")
        os._exit(0)
        event.accept()

    def stratLogPHS(self):  # Push button start live log
        logging.info(f'Button start live was clicked')
        if self.localAPP:
            self.timerLocal.start(self.timerPHSLive.value())
        else:
            self.timer.start(self.timerPHSLive.value())
        self.startLiveLog.setStyleSheet("QPushButton{background-color:#11dd11;}")
        self.stopLiveLog.setStyleSheet("QPushButton{background-color:#555555;}")

    def stopLogPHS(self):  # Push button stop live log
        logging.info(f'Button stop live was clicked')
        if self.localAPP:
            self.timerLocal.stop()
        else:
            self.timer.stop()
        self.startLiveLog.setStyleSheet("QPushButton{background-color:#555555;}")
        self.stopLiveLog.setStyleSheet("QPushButton{background-color:#11dd11;}")

    def startedSendCurlFun(self):  # Start sending asynch curl to ssh
        logging.info(f'Curl is sending to execute ...')
        self.infoCurlLabel.setText("Curl jest w trakcie realizacji ...")

    def finishedSendCurlFun(self):  # Finished of send asynch curl to ssh with succeed
        logging.info(f'Curl sent and everything looks good <3')
        self.infoCurlLabel.setText("Curl został wysłany prawidłowo <3")
        if self.localAPP:
            date = datetime.today().strftime('%Y_%m_%d_logging.log')
            self.getCurlCallBackLocal(f'{self.filePath}/{date}', self.delayForCurlResponse.value() / 1000)
        else:
            self.getCurlCallBack(self.data['ip'], self.data['username'], self.data['password'],
                                 f'tac ~/PHS/logs/(date +%Y_%m_%d)_logging.log '
                                 f'| grep -m1 -B{self.countLineForCurl.value()} '
                                 f'" 127.0.0.1: Executing request" | tac',
                                 self.delayForCurlResponse.value() / 1000)

    def errorSendCurlFun(self):
        self.infoCurlLabel.setText("Wystąpił błąd podczas wysyłania curla")

    def liveLogTimerFunction(self):  # Interval function to send live log PHS (ssh)
        self.logPHSLive.setFontPointSize(self.fontSize.value())
        if self.stackedWidget.currentIndex() == 2:
            if self.grepLineEdit.text() == "":
                self.displayCdmLiveLog(f'tail -n {str(self.maxLineLogLive.value())}'
                                       f' ~/PHS/logs/(date +%Y_%m_%d)_logging.log')
            else:
                self.displayCdmLiveLog(f'tail -n {str(self.maxLineLogLive.value())}'
                                       f' ~/PHS/logs/(date +%Y_%m_%d)_logging.log'
                                       f' | grep "{self.grepLineEdit.text()}"')

    def outputCmdFun(self, out):  # Get result of live log PHS and display
        self.logPHSLive.clear()
        outList = out.split("\n")
        if self.logPHSLive.toPlainText() != out:
            for o in outList:
                ind = 0
                findingLogData = 0
                while ind < 3:
                    findingLogIndex = o[findingLogData:].find(":")
                    findingLogData += findingLogIndex + 1
                    ind += 1
                findingLogData = findingLogData
                findingLogInfo = o[findingLogData + 2:].find(":")
                colorInfo = ['#0ccaf0', '#fcf403', '#fc0303']  # [INFO, DBUG, WARN]
                info = o[findingLogData:findingLogData + 2 + findingLogInfo]
                classNameStart = findingLogData + 2 + findingLogInfo
                classNameStart = o[classNameStart:].find(".") + classNameStart
                classNameStop = o[classNameStart:].find(":") + classNameStart
                className = o[classNameStart:classNameStop]
                flagaLog = True
                if info == "INFO":
                    colorInfo = colorInfo[0]
                elif info == "DBUG":
                    colorInfo = colorInfo[1]
                elif info == "WARN":
                    colorInfo = colorInfo[2]
                else:
                    flagaLog = False
                o = o.replace('<', '&lt;')
                o = o.replace('>', '&gt;')
                if self.grepLineEdit.text() == "":
                    if flagaLog:
                        self.logPHSLive.append(f'<head><meta charset="utf-8"></head>'
                                               f'<body>'
                                               f'<span style="font-size: {self.fontSize.value()}pt;">'
                                               f'<span style="color:#317507;">'
                                               f'{o[:findingLogData]}'
                                               f'</span>'
                                               f'<span style="color:{colorInfo};">'
                                               f'{info}'
                                               f'</span>'
                                               f'<span style="color:">'
                                               f'{o[findingLogData + 2 + findingLogInfo:classNameStart]}'
                                               f'</span>'
                                               f'<span style="color:#0ccaf0;">'
                                               f'{className}'
                                               f'</span>'
                                               f'{o[classNameStop:]}'
                                               f'</span>'
                                               f'</body>')
                    else:
                        if o != "\n":
                            if o.find('Exception') != -1 or o.find('at ') != -1:
                                self.logPHSLive.append(
                                    f'<span style="font-size: {self.fontSize.value()}pt; color:#fc0303;">'
                                    f'{o}'
                                    f'</span>')
                            else:
                                self.logPHSLive.append(
                                    f'<span style="font-size: {self.fontSize.value()}pt; color:#0ccaf0;">'
                                    f'{o}'
                                    f'</span>')

                else:
                    findingLog = o.find(self.grepLineEdit.text())
                    if findingLog != -1:
                        newLogBefore = o[:findingLog]
                        logFind = o[findingLog:findingLog + len(self.grepLineEdit.text())]
                        newLogAfter = o[findingLog + len(self.grepLineEdit.text()):]
                        if o != "\n":
                            self.logPHSLive.append(f'<span style="font-size: {self.fontSize.value()}pt;">'
                                                   f'{newLogBefore}'
                                                   f'<span style="color:red;">'
                                                   f'{logFind}'
                                                   f'</span>'
                                                   f'{newLogAfter}'
                                                   f'</span>')
            self.logPHSLive.verticalScrollBar().setValue(self.logPHSLive.verticalScrollBar().maximum())

        if self.logPHSLive.toPlainText() == "":
            self.logPHSLive.setFontPointSize(self.fontSize.value())
            self.logPHSLive.setText(f'Brak logów dla {self.grepLineEdit.text()}')

    def sendCurlButton(self):  # Send Curl to execute push button
        logging.info(f'Button sending curl was clicked and send curl {self.finishedCurl.text()} to {self.data["ip"]}')
        self.logAfterCurl.clear()
        if self.localAPP:
            self.sendLocalCurl(self.finishedCurl.text())
        else:
            self.sendAsyncioCurl(self.data['ip'], self.data['username'], self.data['password'],
                                 self.finishedCurl.text())

    def backToCurls(self):  # Back to list of curls push button
        self.stackedWidget.setCurrentIndex(1)
        logging.info("Button back to list of curl was clicked and return to stacked widget index 1")
        self.logAfterCurl.clear()
        self.infoCurlLabel.clear()
        for param, label in self.listOfParametr:
            param.setVisible(False)
            label.setVisible(False)

    def setActualCurlandParam(self, curl):  # First setting after double-click curl (param visible,param text)
        type = self.CurlParser.getTypeOfCurl(curl)
        logging.info(f'Type of curl {curl} is {type}')
        if type == 1:
            param = self.CurlParser.getListOfParamForCurlMethodString(curl)
            self.p1.setVisible(True)
            self.p1label.setVisible(True)
            self.p1.setText(param)
            logging.info(f'Find 1 param for curl, param >> {param}')
        elif type == 2:
            tablicaParam = self.CurlParser.getListOfParamForCurlCallMethod(curl)
            i = 0
            while i < len(tablicaParam):
                self.listOfParametr[i][0].setVisible(True)
                self.listOfParametr[i][1].setVisible(True)
                self.listOfParametr[i][0].setText(tablicaParam[i])
                i += 1
        self.finishedCurl.setText(curl)

    def setOnlyActulCurl(self):  # Function connected to text line edit textchanged
        type = self.CurlParser.getTypeOfCurl(self.actualCurl)
        param = []
        for pa, label in self.listOfParametr:
            if pa.isVisible():
                param.append(pa.text())
        if type == 1:
            self.finishedCurl.setText(self.CurlParser.createFinishCurlMethodString(self.actualCurl, param))
        elif type == 2:
            self.finishedCurl.setText(self.CurlParser.createFinishCurlCallMethod(self.actualCurl, param))

    def curlCallBackFun(self, out):  # Catch signal for sending curl and get call back output
        outList = out.split("\n")
        firstLine = True
        for o in outList:
            if firstLine:
                if o.find(" 127.0.0.1: Executing request") == -1:
                    continue
                self.logAfterCurl.append(f'<span style="font-size: {self.fontSize.value()}pt; color:#ab5757;">'
                                         f'{o}'
                                         f'</span>')
                firstLine = False
            else:
                ind = 0
                findingLogData = 0
                while ind < 3:
                    findingLogIndex = o[findingLogData:].find(":")
                    findingLogData += findingLogIndex + 1
                    ind += 1
                findingLogData = findingLogData
                findingLogInfo = o[findingLogData + 2:].find(":")
                colorInfo = ['#0ccaf0', '#fcf403', '#fc0303']  # [INFO, DBUG, WARN]
                info = o[findingLogData:findingLogData + 2 + findingLogInfo]
                classNameStart = findingLogData + 2 + findingLogInfo
                classNameStart = o[classNameStart:].find(".") + classNameStart
                classNameStop = o[classNameStart:].find(":") + classNameStart
                className = o[classNameStart:classNameStop]
                flagaLog = True
                if info == "INFO":
                    colorInfo = colorInfo[0]
                elif info == "DBUG":
                    colorInfo = colorInfo[1]
                elif info == "WARN":
                    colorInfo = colorInfo[2]
                else:
                    flagaLog = False
                o = o.replace('<', '&lt;')
                o = o.replace('>', '&gt;')
                if flagaLog:
                    self.logAfterCurl.append(f'<head><meta charset="utf-8"></head>'
                                             f'<body>'
                                             f'<span style="font-size: {self.fontSize.value()}pt;">'
                                             f'<span style="color:#317507;">'
                                             f'{o[:findingLogData]}'
                                             f'</span>'
                                             f'<span style="color:{colorInfo};">'
                                             f'{info}'
                                             f'</span>'
                                             f'<span style="color:">'
                                             f'{o[findingLogData + 2 + findingLogInfo:classNameStart]}'
                                             f'</span>'
                                             f'<span style="color:#0ccaf0;">'
                                             f'{className}'
                                             f'</span>'
                                             f'{o[classNameStop:]}'
                                             f'</span>'
                                             f'</body>')
                else:
                    self.logAfterCurl.append(f'<span style="font-size: {self.fontSize.value()}pt;">'
                                             f'{o}'
                                             f'</span>')
        logging.info("Get call back for curl")


def startAplication():  # Start Application with qasync
    app = QtWidgets.QApplication(sys.argv)
    loop = qasync.QEventLoop(app)
    window = MainWindow()
    window.show()
    logging.info("Starting application Curlator ...")
    with loop:
        loop.run_forever()
