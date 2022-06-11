# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'mainwindow.ui'
##
# Created by: Qt User Interface Compiler version 6.3.0
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys

import qdarktheme
from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt, QThread,
                            QUrl)
from PySide6.QtGui import QAction, QDesktopServices, QIcon, QTextCursor
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout,
                               QHBoxLayout, QLabel, QLineEdit, QMainWindow,
                               QProgressBar, QPushButton, QTextEdit,
                               QToolButton, QVBoxLayout, QWidget)
from datetime import timedelta
from time import strftime, gmtime
import icon_rc


class Ui_windowMainWindow(object):
    def setupUi(self, windowMainWindow):
        if not windowMainWindow.objectName():
            windowMainWindow.setObjectName(u"windowMainWindow")
        windowMainWindow.resize(362, 231)
        windowMainWindow.setMinimumSize(QSize(362, 231))
        windowMainWindow.setMaximumSize(QSize(364, 231))
        icon = QIcon()
        icon.addFile(u":/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        windowMainWindow.setWindowIcon(icon)
        self.actionOpen = QAction(windowMainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.centralwidget = QWidget(windowMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMaximumSize(QSize(16777215, 10))
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)

        self.gridLayout.addWidget(self.progressBar, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.txtThing = QLineEdit(self.centralwidget)
        self.txtThing.setObjectName(u"txtThing")

        self.verticalLayout_2.addWidget(self.txtThing)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.txtImgCount = QLineEdit(self.centralwidget)
        self.txtImgCount.setObjectName(u"txtImgCount")

        self.verticalLayout.addWidget(self.txtImgCount)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnRender = QPushButton(self.centralwidget)
        self.btnRender.setObjectName(u"btnRender")

        self.horizontalLayout.addWidget(self.btnRender)

        self.btnOpen = QPushButton(self.centralwidget)
        self.btnOpen.setObjectName(u"btnOpen")

        self.horizontalLayout.addWidget(self.btnOpen)

        self.btnMusicManager = QToolButton(self.centralwidget)
        self.btnMusicManager.setObjectName(u"btnMusicManager")

        self.horizontalLayout.addWidget(self.btnMusicManager)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.chkboxCool = QCheckBox(self.centralwidget)
        self.chkboxCool.setObjectName(u"chkboxCool")
        self.chkboxCool.setChecked(True)

        self.verticalLayout_3.addWidget(self.chkboxCool)

        self.chkboxInclude = QCheckBox(self.centralwidget)
        self.chkboxInclude.setObjectName(u"chkboxInclude")

        self.verticalLayout_3.addWidget(self.chkboxInclude)

        self.lblEstimation = QLabel(self.centralwidget)
        self.lblEstimation.setObjectName(u"lblEstimation")
        self.lblEstimation.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lblEstimation)

        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.txtLogOutput = QTextEdit(self.centralwidget)
        self.txtLogOutput.setObjectName(u"txtLogOutput")
        self.txtLogOutput.setReadOnly(True)

        self.gridLayout.addWidget(self.txtLogOutput, 2, 0, 1, 1)

        windowMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(windowMainWindow)

        QMetaObject.connectSlotsByName(windowMainWindow)
    # setupUi

    def retranslateUi(self, windowMainWindow):
        windowMainWindow.setWindowTitle(QCoreApplication.translate(
            "windowMainWindow", u"bumblefuck", None))
        self.actionOpen.setText(QCoreApplication.translate(
            "windowMainWindow", u"Open", None))
        self.txtThing.setPlaceholderText(
            QCoreApplication.translate("windowMainWindow", u"Thing", None))
        self.txtImgCount.setPlaceholderText(
            QCoreApplication.translate("windowMainWindow", u"Count", None))
        self.btnRender.setText(QCoreApplication.translate(
            "windowMainWindow", u"Render", None))
# if QT_CONFIG(shortcut)
        self.btnRender.setShortcut(QCoreApplication.translate(
            "windowMainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.btnOpen.setText(QCoreApplication.translate(
            "windowMainWindow", u"Open Directory", None))
        self.btnMusicManager.setText(
            QCoreApplication.translate("windowMainWindow", u"...", None))
        self.chkboxCool.setText(QCoreApplication.translate(
            "windowMainWindow", u"Transitions", None))
        self.chkboxInclude.setText(QCoreApplication.translate(
            "windowMainWindow", u"Include \"s\" on things", None))
        self.lblEstimation.setText("Estimated time: 00:00:00")
    # retranslateUi


class MainWindow(QMainWindow, Ui_windowMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.actionOpen.triggered.connect(self.openDownloader)
        self.btnRender.clicked.connect(self.doTheThing)
        self.btnOpen.clicked.connect(self.openFolder)
        self.btnMusicManager.clicked.connect(self.openDownloader)
        self.txtImgCount.textChanged.connect(self.updateEstimation)
        self.show()

    def log(self, txt):
        self.txtLogOutput.insertPlainText(f"{txt}\n")
        self.txtLogOutput.moveCursor(QTextCursor.End)

    def updateEstimation(self):
        try:
            x = int(self.txtImgCount.text())
            val = (0.00147023*(x**2))+(0.32968*x)+1.6266
            timestr = strftime("%H:%M:%S", gmtime(val))
            self.lblEstimation.setText(f"Estimated time: {timestr}")
        except:
            pass

    def doTheThing(self):
        self.txtLogOutput.clear()
        self.btnRender.setEnabled(False)
        thing = self.txtThing.text()
        count = int(self.txtImgCount.text())
        cool = self.chkboxCool.isChecked()
        include = self.chkboxInclude.isChecked()
        self.videomaker = VideoMaker(thing, count, cool, include)
        self.videoThread = QThread()
        self.videoThread.name = "E"
        self.videomaker.moveToThread(self.videoThread)
        self.videoThread.started.connect(self.videomaker.run)
        self.videomaker.finished.connect(self.videoThread.quit)
        self.videomaker.finished.connect(self.videomaker.deleteLater)
        self.videoThread.finished.connect(self.videoThread.deleteLater)
        self.videomaker.progress.connect(self.progressBar.setValue)
        self.videomaker.addToLog.connect(self.log)
        self.videoThread.start()
        self.videoThread.finished.connect(
            lambda: self.btnRender.setEnabled(True))

    def openFolder(self):
        url = QUrl.fromLocalFile(bumblepath)
        QDesktopServices.openUrl(url)

    def openDownloader(self):
        dl = DownloadAlert(self)
        dl.exec()

    # TODO replace context menu with downloader button


if __name__ == '__main__':
    from DownloadAlert import DownloadAlert
    from main_html_scrape_ultra_super_low_bitrate import VideoMaker, bumblepath
    app = QApplication([])
    app.setStyleSheet(qdarktheme.load_stylesheet())
    window = MainWindow()

    sys.exit(app.exec())
