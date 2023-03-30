import json
import logging
import os
import sys
import qasync
from PySide6 import QtWidgets
from PySide6.QtWidgets import QFileDialog
from PySide6.QtCore import QTimer, Signal
import asyncioClass
from MainWindow import Ui_MainWindow
from curlParser import CurlParser


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow, asyncioClass.Asyncio):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # Timer to live logging
        self.timer = QTimer()
        self.timer.timeout.connect(self.liveLogTimerFunction)

        # Variable
        self.data = None
        self.localHostFlag = bool
        self.ip = str
        self.username = str
        self.password = str
        self.actualCurl = str

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
        self.maxLineLogLive.setValue(10)
        self.fontSize.setValue(10)
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
                logging.info("Starting local Curlator ...")
                self.infoHomePage.setText(f'Curlator startuje dla localhost ...')
                # TO DO localhost version
            else:
                logging.info("Starting ssh Curlator ...")
                self.infoHomePage.setText(f'Curlator startuje dla {self.data["ip"]} ...')
                self.checkConnectionSSH(self.data['ip'], self.data['username'], self.data['password'])
        except ValueError:
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
        self.timer.start(self.timerPHSLive.value())
        self.startLiveLog.setStyleSheet("QPushButton{background-color:#11dd11;}")
        self.stopLiveLog.setStyleSheet("QPushButton{background-color:#555555;}")

    def stopLogPHS(self):  # Push button stop live log
        logging.info(f'Button stop live was clicked')
        self.timer.stop()
        self.startLiveLog.setStyleSheet("QPushButton{background-color:#555555;}")
        self.stopLiveLog.setStyleSheet("QPushButton{background-color:#11dd11;}")

    def startedSendCurlFun(self):  # Start sending asynch curl to ssh
        logging.info(f'Curl is sending to execute ...')
        self.infoCurlLabel.setText("Curl jest w trakcie realizacji ...")

    def finishedSendCurlFun(self):  # Finished of send asynch curl to ssh with succeed
        logging.info(f'Curl sent and everything looks good <3')
        self.infoCurlLabel.setText("Curl został wysłany prawidłowo <3")
        self.getCurlCallBack(self.data['ip'], self.data['username'], self.data['password'],
                             f'grep -C{self.countLineForCurl.value()-1} " 127.0.0.1: Executing request"'
                             f' ~/PHS/logs/(date +%Y_%m_%d)_logging.log | tail -{self.countLineForCurl.value()}',
                             self.delayForCurlResponse.value()/1000)

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
        if self.logPHSLive.toPlainText() != out:
            self.logPHSLive.setText(out)
        self.logPHSLive.verticalScrollBar().setValue(self.logPHSLive.verticalScrollBar().maximum())

    def sendCurlButton(self):  # Send Curl to execute push button
        logging.info(f'Button sending curl was clicked and send curl {self.finishedCurl.text()} to {self.data["ip"]}')
        self.logAfterCurl.clear()
        self.sendAsyncioCurl(self.data['ip'], self.data['username'], self.data['password'], self.finishedCurl.text())

    def backToCurls(self):  # Back to list of curls push button
        self.stackedWidget.setCurrentIndex(1)
        logging.info("Button back to list of curl was clicked and return to stacked widget index 1")
        for param, label in self.listOfParametr:
            param.setVisible(False)
            label.setVisible(False)

    def setActualCurlandParam(self, curl):  # First setting after double-click curl (param visible,param text)
        type = self.CurlParser.getTypeOfCurl(curl)
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
        logging.info("Get call back for curl")
        self.logAfterCurl.setFontPointSize(self.fontSize.value())
        self.logAfterCurl.setText(out)


def startAplication():  # Start Application with qasync
    app = QtWidgets.QApplication(sys.argv)
    loop = qasync.QEventLoop(app)
    window = MainWindow()
    window.show()
    logging.info("Starting application Curlator ...")
    with loop:
        loop.run_forever()
