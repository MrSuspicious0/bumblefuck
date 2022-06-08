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
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect, QSize, Qt,
                            QTime, QUrl)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QGradient, QIcon, QImage,
                           QKeySequence, QLinearGradient, QPainter, QPalette,
                           QPixmap, QRadialGradient, QTransform, QTextCursor)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout,
                               QHBoxLayout, QLineEdit, QMainWindow,
                               QPushButton, QSizePolicy, QTextEdit,
                               QVBoxLayout, QWidget)

import icon_rc


class Ui_windowMainWindow(object):
    def setupUi(self, windowMainWindow):
        if not windowMainWindow.objectName():
            windowMainWindow.setObjectName(u"windowMainWindow")
        windowMainWindow.resize(323, 183)
        windowMainWindow.setMinimumSize(QSize(323, 183))
        windowMainWindow.setMaximumSize(QSize(323, 183))
        icon = QIcon()
        icon.addFile(u":/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        windowMainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(windowMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
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

        self.btnSave = QPushButton(self.centralwidget)
        self.btnSave.setObjectName(u"btnSave")

        self.horizontalLayout.addWidget(self.btnSave)

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

        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.txtLogOutput = QTextEdit(self.centralwidget)
        self.txtLogOutput.setObjectName(u"txtLogOutput")
        self.txtLogOutput.setReadOnly(True)
        self.gridLayout.addWidget(self.txtLogOutput, 1, 0, 1, 1)

        windowMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(windowMainWindow)

        QMetaObject.connectSlotsByName(windowMainWindow)
    # setupUi
        self.btnRender.clicked.connect(self.doTheThing)

    def doTheThing(self):
        self.txtLogOutput.clear()
        self.btnRender.setEnabled(False)
        thing = self.txtThing.text()
        count = int(self.txtImgCount.text())
        cool = self.chkboxCool.isChecked()
        include = self.chkboxInclude.isChecked()

        _doIt(thing, count, cool, include, self)

    def retranslateUi(self, windowMainWindow):
        windowMainWindow.setWindowTitle(QCoreApplication.translate(
            "windowMainWindow", u"bumblefuck", None))
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
        self.btnSave.setText(QCoreApplication.translate(
            "windowMainWindow", u"Save Result", None))
        self.chkboxCool.setText(QCoreApplication.translate(
            "windowMainWindow", u"Transitions", None))
        self.chkboxInclude.setText(QCoreApplication.translate(
            "windowMainWindow", u"Include \"s\" on things", None))
    # retranslateUi


class MainWindow(QMainWindow, Ui_windowMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.show()


if __name__ == '__main__':
    from main_html_scrape_ultra_super_low_bitrate import doIt, _doIt
    app = QApplication([])
    app.setStyleSheet(qdarktheme.load_stylesheet())
    window = MainWindow()

    sys.exit(app.exec())
