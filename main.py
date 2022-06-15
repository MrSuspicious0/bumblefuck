# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'mainwindow.ui'
##
# Created by: Qt User Interface Compiler version 6.3.0
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import math
import sys
from functools import partial

import qdarktheme
from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt, QThread,
                            QUrl)
from PySide6.QtGui import QAction, QDesktopServices, QIcon, QTextCursor
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout,
                               QHBoxLayout, QLabel, QLineEdit, QMainWindow,
                               QProgressBar, QPushButton, QTextEdit,
                               QToolButton, QVBoxLayout, QWidget)
# from PyTaskbar import Progress
from win10toast_click import ToastNotifier

import icon_rc


class Ui_windowMainWindow(object):
    def setupUi(self, windowMainWindow):
        if not windowMainWindow.objectName():
            windowMainWindow.setObjectName(u"windowMainWindow")
        windowMainWindow.resize(378, 231)
        windowMainWindow.setMinimumSize(QSize(378, 231))
        windowMainWindow.setMaximumSize(QSize(378, 231))
        icon = QIcon()
        icon.addFile(u":/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        windowMainWindow.setWindowIcon(icon)
        self.actionOpen = QAction(windowMainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.centralwidget = QWidget(windowMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.txtLogOutput = QTextEdit(self.centralwidget)
        self.txtLogOutput.setObjectName(u"txtLogOutput")
        self.txtLogOutput.setReadOnly(True)

        self.gridLayout.addWidget(self.txtLogOutput, 2, 0, 1, 1)

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
        icon1 = QIcon()
        icon1.addFile(u":/dancingbee.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.btnMusicManager.setIcon(icon1)

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
        self.lblEstimation.setMaximumSize(QSize(133, 16777215))
        self.lblEstimation.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lblEstimation)

        self.lblFilesize = QLabel(self.centralwidget)
        self.lblFilesize.setObjectName(u"lblFilesize")
        self.lblFilesize.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lblFilesize)

        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

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
# if QT_CONFIG(tooltip)
        self.btnMusicManager.setToolTip(QCoreApplication.translate(
            "windowMainWindow", u"Music Manager", None))
#endif // QT_CONFIG(tooltip)
        self.btnMusicManager.setText("")
        self.chkboxCool.setText(QCoreApplication.translate(
            "windowMainWindow", u"Transitions", None))
        self.chkboxInclude.setText(QCoreApplication.translate(
            "windowMainWindow", u"Include \"s\" on things", None))
        self.lblEstimation.setText(QCoreApplication.translate(
            "windowMainWindow", u"Estimated Time: 00:00:00", None))
        self.lblFilesize.setText(QCoreApplication.translate(
            "windowMainWindow", u"Estimated Size: 0 MB", None))
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
        self.txtImgCount.textChanged.connect(self.updateFilesize)
        self.show()

    def finishNotification(self, thing, count, filepath):
        notifier.show_toast(
            "bumblefuck", f"your top {count} {thing} has finished rendering, click here to open it.", "icon.ico", 5, True, partial(self.openFile, filepath))

    def log(self, txt):
        self.txtLogOutput.insertPlainText(f"{txt}\n")
        self.txtLogOutput.moveCursor(QTextCursor.End)

    def updateEstimation(self):
        try:
            x = int(self.txtImgCount.text())
            seconds = round((0.374032*x)+1.48253)

            self.lblEstimation.setText(
                f"Estimated time: {convertTime(seconds)}")
        except:
            pass

    def updateFilesize(self):
        try:
            x = int(self.txtImgCount.text())
            bytes = round((38199.5*x)+15698.6)
            self.lblFilesize.setText(
                f"Estimated Size: {convertBytes(bytes)}")
        except:
            pass

    def doTheThing(self):
        try:
            self.txtLogOutput.clear()
            self.btnRender.setEnabled(False)
            thing = self.txtThing.text()
            count = int(self.txtImgCount.text())
            cool = self.chkboxCool.isChecked()
            include = self.chkboxInclude.isChecked()
            self.videomaker = VideoMaker(thing, count, cool, include)
            self.videoThread = QThread()
            self.videomaker.moveToThread(self.videoThread)
            self.videoThread.started.connect(self.videomaker.run)
            self.videomaker.finished.connect(self.videoThread.quit)
            self.videomaker.finished.connect(self.videomaker.deleteLater)
            self.videoThread.finished.connect(self.videoThread.deleteLater)
            self.videomaker.progress.connect(self.progressBar.setValue)
            self.videomaker.addToLog.connect(self.log)
            self.videoThread.start()
            self.videomaker.notify.connect(self.finishNotification)
            self.videoThread.finished.connect(
                lambda: self.btnRender.setEnabled(True))
            self.videomaker.error.connect(
                lambda: self.btnRender.setEnabled(True))
            self.videomaker.error.connect(self.videoThread.quit)
        except:
            self.btnRender.setEnabled(True)

    def openFolder(self):
        url = QUrl.fromLocalFile(bumblepath)
        QDesktopServices.openUrl(url)

    def openFile(self, filepath):
        url = QUrl.fromLocalFile(filepath)
        QDesktopServices.openUrl(url)

    def openDownloader(self):
        dl = DownloadAlert(self)
        dl.exec()


def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    hours = f"0{hours}" if hours < 10 else hours
    minutes = f"0{minutes}" if minutes < 10 else minutes
    seconds = f"0{seconds}" if seconds < 10 else seconds
    return f"{hours}:{minutes}:{seconds}"


def convertBytes(bytes):
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = math.floor(math.log(bytes, 1024))
    p = 1024 ** i
    return f"{round(bytes/p, 2)} {size_name[i]}"


if __name__ == '__main__':
    from DownloadAlert import DownloadAlert
    from main_html_scrape_ultra_super_low_bitrate import VideoMaker, bumblepath
    app = QApplication([])
    notifier = ToastNotifier()
    # taskbar = Progress()
    # taskbar.init()

    app.setStyleSheet(qdarktheme.load_stylesheet())
    window = MainWindow()

    sys.exit(app.exec())
