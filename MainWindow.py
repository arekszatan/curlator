# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QPushButton, QSizePolicy, QSpinBox,
    QStackedWidget, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(853, 786)
        MainWindow.setStyleSheet(u"*{\n"
"	color:#fff;\n"
"	font:25px  \"Lucida Sans\";\n"
"	\n"
"}\n"
"QWidget{\n"
"background-color: #333333;\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"	color:#fff;\n"
"	background-color:#555555;\n"
"	border-radius: 10px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.gridLayout_2 = QGridLayout(self.homePage)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.openJsonButton = QPushButton(self.homePage)
        self.openJsonButton.setObjectName(u"openJsonButton")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.openJsonButton.sizePolicy().hasHeightForWidth())
        self.openJsonButton.setSizePolicy(sizePolicy)
        self.openJsonButton.setStyleSheet(u"font: 40pt \"MS Shell Dlg 2\";")

        self.gridLayout_2.addWidget(self.openJsonButton, 3, 0, 1, 1)

        self.label = QLabel(self.homePage)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"MS Shell Dlg 2"])
        font.setPointSize(60)
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"font: 60pt \"MS Shell Dlg 2\";")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)

        self.helpButton = QPushButton(self.homePage)
        self.helpButton.setObjectName(u"helpButton")
        sizePolicy.setHeightForWidth(self.helpButton.sizePolicy().hasHeightForWidth())
        self.helpButton.setSizePolicy(sizePolicy)
        self.helpButton.setStyleSheet(u"font: 40pt \"MS Shell Dlg 2\";")

        self.gridLayout_2.addWidget(self.helpButton, 3, 1, 1, 1)

        self.infoHomePage = QLabel(self.homePage)
        self.infoHomePage.setObjectName(u"infoHomePage")
        self.infoHomePage.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.infoHomePage, 1, 0, 1, 2)

        self.stackedWidget.addWidget(self.homePage)
        self.curlsPage = QWidget()
        self.curlsPage.setObjectName(u"curlsPage")
        self.gridLayout_3 = QGridLayout(self.curlsPage)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.curlList = QListWidget(self.curlsPage)
        self.curlList.setObjectName(u"curlList")

        self.gridLayout_3.addWidget(self.curlList, 1, 1, 1, 1)

        self.label_2 = QLabel(self.curlsPage)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.curlsPage)
        self.curlPage = QWidget()
        self.curlPage.setObjectName(u"curlPage")
        self.curlPage.setStyleSheet(u"QLabel{\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"\n"
"}\n"
"\n"
"QTextEdit{\n"
"	font: 12pt \"MS Shell Dlg 2\";\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.curlPage)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget_2 = QWidget(self.curlPage)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)

        self.verticalLayout_2.addWidget(self.label_3)

        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)

        self.verticalLayout_2.addWidget(self.label_4)

        self.maxLineLogLive = QSpinBox(self.widget_2)
        self.maxLineLogLive.setObjectName(u"maxLineLogLive")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.maxLineLogLive.sizePolicy().hasHeightForWidth())
        self.maxLineLogLive.setSizePolicy(sizePolicy3)
        self.maxLineLogLive.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.maxLineLogLive.setMaximum(3000)

        self.verticalLayout_2.addWidget(self.maxLineLogLive)

        self.fontSize = QSpinBox(self.widget_2)
        self.fontSize.setObjectName(u"fontSize")
        sizePolicy3.setHeightForWidth(self.fontSize.sizePolicy().hasHeightForWidth())
        self.fontSize.setSizePolicy(sizePolicy3)
        self.fontSize.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.verticalLayout_2.addWidget(self.fontSize)

        self.stopLiveLog = QPushButton(self.widget_2)
        self.stopLiveLog.setObjectName(u"stopLiveLog")

        self.verticalLayout_2.addWidget(self.stopLiveLog)

        self.startLiveLog = QPushButton(self.widget_2)
        self.startLiveLog.setObjectName(u"startLiveLog")

        self.verticalLayout_2.addWidget(self.startLiveLog)

        self.pushButton = QPushButton(self.widget_2)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy2.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy2)

        self.verticalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.widget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy2.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy2)

        self.verticalLayout_2.addWidget(self.pushButton_2)


        self.horizontalLayout.addWidget(self.widget_2)

        self.widget = QWidget(self.curlPage)
        self.widget.setObjectName(u"widget")
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(150, 0))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.logPHSLive = QTextEdit(self.widget)
        self.logPHSLive.setObjectName(u"logPHSLive")
        sizePolicy.setHeightForWidth(self.logPHSLive.sizePolicy().hasHeightForWidth())
        self.logPHSLive.setSizePolicy(sizePolicy)
        self.logPHSLive.setReadOnly(True)

        self.verticalLayout.addWidget(self.logPHSLive)

        self.grepLineEdit = QLineEdit(self.widget)
        self.grepLineEdit.setObjectName(u"grepLineEdit")
        sizePolicy3.setHeightForWidth(self.grepLineEdit.sizePolicy().hasHeightForWidth())
        self.grepLineEdit.setSizePolicy(sizePolicy3)

        self.verticalLayout.addWidget(self.grepLineEdit)

        self.logAfterCurl = QTextEdit(self.widget)
        self.logAfterCurl.setObjectName(u"logAfterCurl")
        sizePolicy.setHeightForWidth(self.logAfterCurl.sizePolicy().hasHeightForWidth())
        self.logAfterCurl.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.logAfterCurl)


        self.horizontalLayout.addWidget(self.widget)

        self.stackedWidget.addWidget(self.curlPage)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.stackedWidget.addWidget(self.page_5)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout.addWidget(self.stackedWidget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.openJsonButton.setText(QCoreApplication.translate("MainWindow", u"Otw\u00f3rz plik JSON", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Curlator", None))
        self.helpButton.setText(QCoreApplication.translate("MainWindow", u"Pomoc", None))
        self.infoHomePage.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Wybierz curla:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Wybrany curl:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Podgl\u0105d:", None))
        self.stopLiveLog.setText(QCoreApplication.translate("MainWindow", u"Stop live", None))
        self.startLiveLog.setText(QCoreApplication.translate("MainWindow", u"Start live", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Wy\u015blij", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Powr\u00f3t", None))
        self.grepLineEdit.setText(QCoreApplication.translate("MainWindow", u"a", None))
    # retranslateUi

