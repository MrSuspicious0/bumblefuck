import math
import sys
from functools import partial

import qdarktheme
from PySide6.QtCore import QThread, QUrl
from PySide6.QtGui import QDesktopServices, QTextCursor
from PySide6.QtWidgets import QApplication, QMainWindow
from win10toast_click import ToastNotifier

import icon_rc
from mainwindowUI import Ui_windowMainWindow


class MainWindow(QMainWindow, Ui_windowMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.group = (self.txtImgCount, self.txtThing,
                      self.btnRender, self.chkboxCool, self.chkboxInclude)
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

    def showHide(self, x: bool):
        for e in self.group:
            e.setEnabled(x)

    def doTheThing(self):
        try:

            self.txtLogOutput.clear()
            self.showHide(False)
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
            self.videoThread.finished.connect(lambda: self.showHide(True))
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
