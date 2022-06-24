from PySide6.QtCore import QCoreApplication, QMetaObject, QSize, Qt
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (QCheckBox, QGridLayout, QHBoxLayout, QLabel,
                               QLineEdit, QProgressBar, QPushButton, QTextEdit,
                               QToolButton, QVBoxLayout, QWidget)

import icon_rc


class Ui_windowMainWindow(object):
    def setupUi(self, windowMainWindow):
        if not windowMainWindow.objectName():
            windowMainWindow.setObjectName(u"windowMainWindow")
        windowMainWindow.resize(362, 231)
        windowMainWindow.setMinimumSize(QSize(362, 231))
        windowMainWindow.setMaximumSize(QSize(362, 231))
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
        self.lblEstimation.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lblEstimation)

        self.lblFilesize = QLabel(self.centralwidget)
        self.lblFilesize.setObjectName(u"lblFilesize")
        self.lblFilesize.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lblFilesize)

        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.txtLogOutput = QTextEdit(self.centralwidget)
        self.txtLogOutput.setObjectName(u"txtLogOutput")
        self.txtLogOutput.setFocusPolicy(Qt.NoFocus)
        self.txtLogOutput.setUndoRedoEnabled(False)
        self.txtLogOutput.setReadOnly(True)
        self.txtLogOutput.setTextInteractionFlags(Qt.NoTextInteraction)

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
