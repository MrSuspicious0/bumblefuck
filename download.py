# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'downloadalert.ui'
##
# Created by: Qt User Interface Compiler version 6.3.0
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QGridLayout, QHBoxLayout, QLineEdit, QListWidget,
                               QProgressBar, QPushButton, QVBoxLayout)

import icon_rc


class Ui_windowAlert(object):
    def setupUi(self, windowAlert):
        if not windowAlert.objectName():
            windowAlert.setObjectName(u"windowAlert")
        windowAlert.resize(276, 274)
        windowAlert.setMinimumSize(QSize(276, 274))
        windowAlert.setMaximumSize(QSize(276, 274))
        icon = QIcon()
        icon.addFile(u":/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        windowAlert.setWindowIcon(icon)
        self.gridLayout = QGridLayout(windowAlert)
        self.gridLayout.setObjectName(u"gridLayout")
        self.vlayoutMaster = QVBoxLayout()
        self.vlayoutMaster.setObjectName(u"vlayoutMaster")
        self.vlayoutText_Buttons = QVBoxLayout()
        self.vlayoutText_Buttons.setObjectName(u"vlayoutText_Buttons")
        self.txtInput = QLineEdit(windowAlert)
        self.txtInput.setObjectName(u"txtInput")

        self.vlayoutText_Buttons.addWidget(self.txtInput)

        self.hlayoutButtons = QHBoxLayout()
        self.hlayoutButtons.setObjectName(u"hlayoutButtons")
        self.btnAdd = self.makeButtons(windowAlert, u"btnAdd")
        self.btnRemove = self.makeButtons(windowAlert, u"btnRemove")
        self.btnDownload = self.makeButtons(windowAlert, u"btnDownload")
        self.vlayoutText_Buttons.addLayout(self.hlayoutButtons)

        self.vlayoutMaster.addLayout(self.vlayoutText_Buttons)

        self.progressBar = QProgressBar(windowAlert)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMaximumSize(QSize(16777215, 12))
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)

        self.vlayoutMaster.addWidget(self.progressBar)

        self.listWidget = QListWidget(windowAlert)
        self.listWidget.setObjectName(u"listWidget")

        self.vlayoutMaster.addWidget(self.listWidget)

        self.gridLayout.addLayout(self.vlayoutMaster, 0, 0, 1, 1)

        self.retranslateUi(windowAlert)

        QMetaObject.connectSlotsByName(windowAlert)

    def makeButtons(self, windowAlert, arg1):
        result = QPushButton(windowAlert)
        result.setObjectName(arg1)

        self.hlayoutButtons.addWidget(result)

        return result
    # setupUi

    def retranslateUi(self, windowAlert):
        windowAlert.setWindowTitle(QCoreApplication.translate(
            "windowAlert", u"Music Downloader", None))
        self.txtInput.setPlaceholderText(
            QCoreApplication.translate("windowAlert", u"URL", None))
        self.btnAdd.setText(QCoreApplication.translate(
            "windowAlert", u"Add", None))
        self.btnRemove.setText(QCoreApplication.translate(
            "windowAlert", u"Remove", None))
        self.btnDownload.setText(QCoreApplication.translate(
            "windowAlert", u"Download", None))
    # retranslateUi
