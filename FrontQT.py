import logging
import sys
from PySide6 import QtWidgets
from MainWindow import Ui_MainWindow
import qasync
import asyncioClass


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow, asyncioClass.Asyncio):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.test)
        self.started.connect(self.started1)
        self.finished.connect(self.finished1)
        self.outputCmd.connect(self.emite)
    def test(self):
        self.runAsyncioCmd("ssh pi@192.168.16.44 journalctl -n20")
    def started1(self):
        print("start")

    def finished1(self):
        print("koniec")

    def emite(self, a):
        print(a)


def startAplication():
    app = QtWidgets.QApplication(sys.argv)
    loop = qasync.QEventLoop(app)
    window = MainWindow()
    window.show()
    logging.debug("Starting aplication Curlator ...")
    with loop:
        loop.run_forever()
