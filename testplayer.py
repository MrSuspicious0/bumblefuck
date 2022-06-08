# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'blankwidget.ui'
##
# Created by: Qt User Interface Compiler version 6.3.0
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QSizePolicy, QWidget, QFileDialog)
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(436, 320)
        self.player = QMediaPlayer(self)
        self.video = QVideoWidget(self)

        self.video.resize(436, 320)
        self.player.setVideoOutput(self.video)
        self.player.setAudioOutput(QAudioOutput())
        url = QUrl()
        fdialog = QFileDialog(self)
        if fdialog.exec() == QFileDialog.Accepted:
            url = fdialog.selectedUrls()[0]
        print(url)
        self.player.setSource(url)
        self.player.play()
        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
    # retranslateUi


class Player(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.show()


app = QApplication([])
window = Player()
sys.exit(app.exec())
