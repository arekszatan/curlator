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
    QStackedWidget, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(853, 786)
        MainWindow.setStyleSheet(u"*{\n"
"	color:#fff;\n"
"	font:20px  \"Lucida Sans\";\n"
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
"	padding:5px;\n"
"}\n"
"\n"
"QPushButton{\n"
"	color:#fff;\n"
"	background-color:#555555;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color:#111;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	color:#111;\n"
"	background-color:#22aa33;\n"
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
        self.widget_2.setMaximumSize(QSize(300, 16777215))
        self.widget_2.setStyleSheet(u"QLineEdit{\n"
"\n"
"font-size:12px;\n"
"padding:5px;\n"
"}\n"
"\n"
"QLabel{\n"
"\n"
"font-size:12px;\n"
"}")
        self.gridLayout_4 = QGridLayout(self.widget_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.p3 = QLineEdit(self.widget_2)
        self.p3.setObjectName(u"p3")

        self.gridLayout_4.addWidget(self.p3, 5, 1, 1, 1)

        self.p4 = QLineEdit(self.widget_2)
        self.p4.setObjectName(u"p4")

        self.gridLayout_4.addWidget(self.p4, 6, 1, 1, 1)

        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_4, 20, 1, 1, 1, Qt.AlignBottom)

        self.p1label = QLabel(self.widget_2)
        self.p1label.setObjectName(u"p1label")

        self.gridLayout_4.addWidget(self.p1label, 3, 0, 1, 1)

        self.p5label = QLabel(self.widget_2)
        self.p5label.setObjectName(u"p5label")

        self.gridLayout_4.addWidget(self.p5label, 7, 0, 1, 1)

        self.p3label = QLabel(self.widget_2)
        self.p3label.setObjectName(u"p3label")

        self.gridLayout_4.addWidget(self.p3label, 5, 0, 1, 1)

        self.p2 = QLineEdit(self.widget_2)
        self.p2.setObjectName(u"p2")

        self.gridLayout_4.addWidget(self.p2, 4, 1, 1, 1)

        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_3, 0, 1, 1, 1, Qt.AlignTop)

        self.p9label = QLabel(self.widget_2)
        self.p9label.setObjectName(u"p9label")

        self.gridLayout_4.addWidget(self.p9label, 11, 0, 1, 1)

        self.p8label = QLabel(self.widget_2)
        self.p8label.setObjectName(u"p8label")

        self.gridLayout_4.addWidget(self.p8label, 10, 0, 1, 1)

        self.p7label = QLabel(self.widget_2)
        self.p7label.setObjectName(u"p7label")

        self.gridLayout_4.addWidget(self.p7label, 9, 0, 1, 1)

        self.p9 = QLineEdit(self.widget_2)
        self.p9.setObjectName(u"p9")

        self.gridLayout_4.addWidget(self.p9, 11, 1, 1, 1)

        self.label_20 = QLabel(self.widget_2)
        self.label_20.setObjectName(u"label_20")
        sizePolicy2.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setFamilies([u"MS Shell Dlg 2"])
        font1.setBold(True)
        font1.setItalic(False)
        self.label_20.setFont(font1)
        self.label_20.setStyleSheet(u"margin-top:20px;\n"
"font-weight:bold;")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_20, 15, 0, 1, 2)

        self.infoCurlLabel = QLabel(self.widget_2)
        self.infoCurlLabel.setObjectName(u"infoCurlLabel")
        sizePolicy2.setHeightForWidth(self.infoCurlLabel.sizePolicy().hasHeightForWidth())
        self.infoCurlLabel.setSizePolicy(sizePolicy2)
        self.infoCurlLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.infoCurlLabel, 16, 0, 1, 2)

        self.p10label = QLabel(self.widget_2)
        self.p10label.setObjectName(u"p10label")

        self.gridLayout_4.addWidget(self.p10label, 12, 0, 1, 1)

        self.p10 = QLineEdit(self.widget_2)
        self.p10.setObjectName(u"p10")

        self.gridLayout_4.addWidget(self.p10, 12, 1, 1, 1)

        self.label_6 = QLabel(self.widget_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 1, 0, 1, 1)

        self.label_7 = QLabel(self.widget_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_4.addWidget(self.label_7, 2, 0, 1, 1)

        self.maxLineLogLive = QSpinBox(self.widget_2)
        self.maxLineLogLive.setObjectName(u"maxLineLogLive")
        sizePolicy2.setHeightForWidth(self.maxLineLogLive.sizePolicy().hasHeightForWidth())
        self.maxLineLogLive.setSizePolicy(sizePolicy2)
        self.maxLineLogLive.setMaximumSize(QSize(9999, 16777215))
        self.maxLineLogLive.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.maxLineLogLive.setMaximum(3000)

        self.gridLayout_4.addWidget(self.maxLineLogLive, 1, 1, 1, 1)

        self.fontSize = QSpinBox(self.widget_2)
        self.fontSize.setObjectName(u"fontSize")
        sizePolicy2.setHeightForWidth(self.fontSize.sizePolicy().hasHeightForWidth())
        self.fontSize.setSizePolicy(sizePolicy2)
        self.fontSize.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.gridLayout_4.addWidget(self.fontSize, 2, 1, 1, 1)

        self.p2label = QLabel(self.widget_2)
        self.p2label.setObjectName(u"p2label")

        self.gridLayout_4.addWidget(self.p2label, 4, 0, 1, 1)

        self.p6label = QLabel(self.widget_2)
        self.p6label.setObjectName(u"p6label")

        self.gridLayout_4.addWidget(self.p6label, 8, 0, 1, 1)

        self.p1 = QLineEdit(self.widget_2)
        self.p1.setObjectName(u"p1")

        self.gridLayout_4.addWidget(self.p1, 3, 1, 1, 1)

        self.p4label = QLabel(self.widget_2)
        self.p4label.setObjectName(u"p4label")

        self.gridLayout_4.addWidget(self.p4label, 6, 0, 1, 1)

        self.p6 = QLineEdit(self.widget_2)
        self.p6.setObjectName(u"p6")

        self.gridLayout_4.addWidget(self.p6, 8, 1, 1, 1)

        self.p5 = QLineEdit(self.widget_2)
        self.p5.setObjectName(u"p5")

        self.gridLayout_4.addWidget(self.p5, 7, 1, 1, 1)

        self.p7 = QLineEdit(self.widget_2)
        self.p7.setObjectName(u"p7")

        self.gridLayout_4.addWidget(self.p7, 9, 1, 1, 1)

        self.p8 = QLineEdit(self.widget_2)
        self.p8.setObjectName(u"p8")

        self.gridLayout_4.addWidget(self.p8, 10, 1, 1, 1)

        self.backPushButton = QPushButton(self.widget_2)
        self.backPushButton.setObjectName(u"backPushButton")
        sizePolicy2.setHeightForWidth(self.backPushButton.sizePolicy().hasHeightForWidth())
        self.backPushButton.setSizePolicy(sizePolicy2)

        self.gridLayout_4.addWidget(self.backPushButton, 19, 0, 1, 1)

        self.sendPushButton = QPushButton(self.widget_2)
        self.sendPushButton.setObjectName(u"sendPushButton")
        sizePolicy2.setHeightForWidth(self.sendPushButton.sizePolicy().hasHeightForWidth())
        self.sendPushButton.setSizePolicy(sizePolicy2)

        self.gridLayout_4.addWidget(self.sendPushButton, 19, 1, 1, 1)


        self.horizontalLayout.addWidget(self.widget_2)

        self.widget = QWidget(self.curlPage)
        self.widget.setObjectName(u"widget")
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(150, 0))
        self.gridLayout_5 = QGridLayout(self.widget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.stopLiveLog = QPushButton(self.widget)
        self.stopLiveLog.setObjectName(u"stopLiveLog")

        self.gridLayout_5.addWidget(self.stopLiveLog, 2, 4, 1, 1)

        self.logPHSLive = QTextEdit(self.widget)
        self.logPHSLive.setObjectName(u"logPHSLive")
        sizePolicy.setHeightForWidth(self.logPHSLive.sizePolicy().hasHeightForWidth())
        self.logPHSLive.setSizePolicy(sizePolicy)
        self.logPHSLive.setReadOnly(True)

        self.gridLayout_5.addWidget(self.logPHSLive, 1, 2, 1, 3)

        self.logAfterCurl = QTextEdit(self.widget)
        self.logAfterCurl.setObjectName(u"logAfterCurl")
        sizePolicy.setHeightForWidth(self.logAfterCurl.sizePolicy().hasHeightForWidth())
        self.logAfterCurl.setSizePolicy(sizePolicy)

        self.gridLayout_5.addWidget(self.logAfterCurl, 4, 2, 1, 3)

        self.finishedCurl = QLabel(self.widget)
        self.finishedCurl.setObjectName(u"finishedCurl")
        sizePolicy2.setHeightForWidth(self.finishedCurl.sizePolicy().hasHeightForWidth())
        self.finishedCurl.setSizePolicy(sizePolicy2)
        self.finishedCurl.setStyleSheet(u"font-size:12px;")

        self.gridLayout_5.addWidget(self.finishedCurl, 5, 2, 1, 3)

        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)

        self.gridLayout_5.addWidget(self.label_8, 3, 2, 1, 1)

        self.startLiveLog = QPushButton(self.widget)
        self.startLiveLog.setObjectName(u"startLiveLog")

        self.gridLayout_5.addWidget(self.startLiveLog, 2, 3, 1, 1)

        self.checgedCurl = QLabel(self.widget)
        self.checgedCurl.setObjectName(u"checgedCurl")
        sizePolicy2.setHeightForWidth(self.checgedCurl.sizePolicy().hasHeightForWidth())
        self.checgedCurl.setSizePolicy(sizePolicy2)
        self.checgedCurl.setStyleSheet(u"font-size:12px;")

        self.gridLayout_5.addWidget(self.checgedCurl, 0, 2, 1, 3)

        self.grepLineEdit = QLineEdit(self.widget)
        self.grepLineEdit.setObjectName(u"grepLineEdit")
        sizePolicy2.setHeightForWidth(self.grepLineEdit.sizePolicy().hasHeightForWidth())
        self.grepLineEdit.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.grepLineEdit, 3, 3, 1, 2)


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
        self.p3.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Podgl\u0105d:", None))
        self.p1label.setText(QCoreApplication.translate("MainWindow", u"Parametr 1:", None))
        self.p5label.setText(QCoreApplication.translate("MainWindow", u"Parametr 5:", None))
        self.p3label.setText(QCoreApplication.translate("MainWindow", u"Parametr 3:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Wybrany curl:", None))
        self.p9label.setText(QCoreApplication.translate("MainWindow", u"Parametr 9:", None))
        self.p8label.setText(QCoreApplication.translate("MainWindow", u"Parametr 8:", None))
        self.p7label.setText(QCoreApplication.translate("MainWindow", u"Parametr 7:", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Info curl:", None))
        self.infoCurlLabel.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.p10label.setText(QCoreApplication.translate("MainWindow", u"Parametr 10:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Ilo\u015b\u0107 log\u00f3w\n"
"live:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Czcionka:", None))
        self.p2label.setText(QCoreApplication.translate("MainWindow", u"Parametr 2:", None))
        self.p6label.setText(QCoreApplication.translate("MainWindow", u"Parametr 6:", None))
        self.p4label.setText(QCoreApplication.translate("MainWindow", u"Parametr 4:", None))
        self.backPushButton.setText(QCoreApplication.translate("MainWindow", u"Powr\u00f3t", None))
        self.sendPushButton.setText(QCoreApplication.translate("MainWindow", u"Wy\u015blij", None))
        self.stopLiveLog.setText(QCoreApplication.translate("MainWindow", u"Stop live", None))
        self.finishedCurl.setText(QCoreApplication.translate("MainWindow", u"gotowy curl ------------------------------------------------------------", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Filtr log\u00f3w live:", None))
        self.startLiveLog.setText(QCoreApplication.translate("MainWindow", u"Start live", None))
        self.checgedCurl.setText(QCoreApplication.translate("MainWindow", u"wybrany cur l---------------------------------------------------------------------", None))
        self.grepLineEdit.setText("")
    # retranslateUi

