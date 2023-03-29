import asyncio
import json
import logging
import os
import sys
import threading
import time
import qasync
from PySide6 import QtWidgets
from PySide6.QtWidgets import QFileDialog
from PySide6.QtCore import QTimer
import asyncioClass
from MainWindow import Ui_MainWindow
from paramiko import SSHClient, AutoAddPolicy


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow, asyncioClass.Asyncio):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setConnectionObject()
        self.setInitStartValue()

        self.timer = QTimer()
        self.timer.timeout.connect(self.liveLogTimerFunction)
        self.timer.start(1000)

        # Variable
        self.data = None
        self.localHostFlag = bool
        self.ip = str
        self.username = str
        self.password = str
        self.listToJson = []

    def setInitStartValue(self):
        self.stackedWidget.setCurrentIndex(0)
        self.maxLineLogLive.setValue(10)
        self.fontSize.setValue(10)

    def setConnectionObject(self):
        self.openJsonButton.clicked.connect(self.openJson)
        self.error.connect(self.errorSSH)
        self.connectionOK.connect(self.loginSSH)
        self.curlList.itemDoubleClicked.connect(self.listJsonDoubleClick)

        self.startLiveLog.clicked.connect(self.stratLogPHS)
        self.stopLiveLog.clicked.connect(self.stopLogPHS)
        self.started.connect(self.started1)
        self.finished.connect(self.finished1)
        self.outputCmd.connect(self.emite)



    def openJson(self):
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
            else:
                logging.info("Starting ssh Curlator ...")
                self.infoHomePage.setText(f'Curlator startuje dla {self.data["ip"]} ...')
                self.checkConnectionSSH(self.data['ip'], self.data['username'], self.data['password'], "ls")
        except ValueError:
            logging.exception(f'Can not open and decoding json file {path}')
            self.infoHomePage.setText(f'Wystąpil błąd podczas dekodowania pliku JSON !!!')

    def errorSSH(self):
        #self.stackedWidget.setCurrentIndex(0)
        self.infoHomePage.setText(f'Błąd podczas łącznia do {self.data["ip"]}')
        logging.error(f'Błąd podczas łącznia do {self.data["ip"]}')

    def loginSSH(self):
        logging.info(f'Logging to {self.data["ip"]} is succesed')
        self.stackedWidget.setCurrentIndex(1)
        for i in self.data['curls']:
            self.listToJson.append(i['curl'])
            self.curlList.addItem(i['shortInfo'])

    def listJsonDoubleClick(self):
        self.stackedWidget.setCurrentIndex(2)
        logging.info(f'List of Json was clicked and value of '
                     f'row is {str(self.listToJson[self.curlList.currentIndex().row()])}')

    def closeEvent(self, event):
        os._exit(0)
        event.accept()

    def stratLogPHS(self):
        self.timer.start()

    def stopLogPHS(self):
        self.timer.stop()

    def test(self):
        self.runAsyncioCmd("192.168.122.21", "amsort", "amsort25@%", "tail -n 20 ~/PHS/logs/(date +%Y_%m_%d)_logging.log")

    def started1(self):
        pass

    def finished1(self):
        print("koniec")

    def liveLogTimerFunction(self):
        self.logPHSLive.setFontPointSize(self.fontSize.value())
        if self.stackedWidget.currentIndex() == 2:
            if self.grepLineEdit.text() == "":
                self.runAsyncioCmd(self.data['ip'], self.data['username'], self.data['password'],
                                   "tail -n " + str(
                                       self.maxLineLogLive.value()) + " ~/PHS/logs/(date +%Y_%m_%d)_logging.log")
            else:
                self.runAsyncioCmd(self.data['ip'], self.data['username'], self.data['password'],
                           "tail -n "+str(self.maxLineLogLive.value())+" ~/PHS/logs/(date +%Y_%m_%d)_logging.log | grep "+self.grepLineEdit.text())

    def emite(self, out):
        if self.logPHSLive.toPlainText() != out:
            self.logPHSLive.setText(out)
        self.logPHSLive.verticalScrollBar().setValue(self.logPHSLive.verticalScrollBar().maximum()-10)



def startAplication():
    app = QtWidgets.QApplication(sys.argv)
    loop = qasync.QEventLoop(app)
    window = MainWindow()
    window.show()
    logging.info("Starting aplication Curlator ...")
    with loop:
        loop.run_forever()
