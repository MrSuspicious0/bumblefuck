import qdarktheme
from PySide6.QtCore import QObject, QThread, Signal
from PySide6.QtWidgets import QApplication, QDialog
from pytube import Playlist, YouTube

from download import *
from main_html_scrape_ultra_super_low_bitrate import musicpath


class DownloadAlert(QDialog, Ui_windowAlert):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.videos = []
        self.parent_ = parent
        self.setupUi(self)
        self.listWidget.setAlternatingRowColors(True)
        self.listWidget.setSelectionMode(self.listWidget.ContiguousSelection)
        self.btnAdd.clicked.connect(self.addItem)
        self.btnRemove.clicked.connect(self.removeItems)
        self.btnDownload.clicked.connect(self.downloadVideos)

    def updateProgressBar(self, percentage, maximum=False):
        if maximum:
            self.progressBar.setMaximum(percentage)
        elif percentage == 0:
            self.progressBar.setValue(0)
        else:
            self.progressBar.setValue(
                self.progressBar.value() + percentage)

    def addItem(self):
        url = self.txtInput.text()
        self.parent_.showHide(False)
        if url.startswith("http"):
            self.txtInput.clear()
            self.btnDownload.setEnabled(False)
            self.btnAdd.setEnabled(False)
            self.adder = ItemAdder(url)
            self.addThread = QThread()
            self.adder.moveToThread(self.addThread)
            self.addThread.started.connect(self.adder.run)
            self.adder.finished.connect(self.addThread.quit)
            self.adder.finished.connect(self.adder.deleteLater)
            self.addThread.finished.connect(self.addThread.deleteLater)
            self.adder.progress.connect(self.updateProgressBar)
            self.adder.newURL.connect(self.videos.append)
            self.adder.newItem.connect(self.listWidget.addItem)
            self.addThread.start()
            self.addThread.finished.connect(
                lambda: self.btnDownload.setEnabled(True))
            self.addThread.finished.connect(
                lambda: self.btnAdd.setEnabled(True))
            self.addThread.finished.connect(
                lambda: self.parent_.showHide(True))

    def downloadVideos(self):
        self.parent_.showHide(False)
        self.btnAdd.setEnabled(False)
        self.btnDownload.setEnabled(False)
        self.progressBar.setMaximum(len(self.videos))
        self.downloadThread = QThread()
        self.downloader = Downloader(self.videos)
        self.downloader.moveToThread(self.downloadThread)
        self.downloadThread.started.connect(self.downloader.run)
        self.downloader.progress.connect(self.updateProgressBar)
        self.downloader.finished.connect(self.downloadThread.quit)
        self.downloader.finished.connect(self.downloader.deleteLater)
        self.downloadThread.finished.connect(self.downloadThread.deleteLater)
        self.downloadThread.start()
        self.downloadThread.finished.connect(
            lambda: self.btnAdd.setEnabled(True))
        self.downloadThread.finished.connect(
            lambda: self.btnDownload.setEnabled(True))
        self.downloadThread.finished.connect(lambda: self.videos.clear())
        self.downloadThread.finished.connect(
            lambda: self.parent_.showHide(True))

    def removeItems(self):
        items = self.listWidget.selectedItems()

        for item in items:
            text = item.text()
            matches = [i for i, tuple in enumerate(
                self.videos) if tuple[1] == text]
            for i in matches:
                self.videos.pop(i)
            self.listWidget.takeItem(self.listWidget.row(item))


class ItemAdder(QObject):
    progress = Signal(int, bool)
    finished = Signal()
    newURL = Signal(tuple)
    newItem = Signal(str)

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        if "&list" in self.url or "playlist" in self.url:
            vids = Playlist(self.url)
            self.progress.emit(vids.length, True)
            for vid in vids.video_urls:
                v = YouTube(vid)
                if not v.age_restricted:
                    self.newURL.emit((vid, v.title))
                    self.newItem.emit(v.title)

                self.progress.emit(1, False)

        else:
            v = YouTube(self.url)
            if not v.age_restricted:
                self.newURL.emit((self.url, v.title))
                self.newItem.emit(v.title)
        self.progress.emit(0, False)
        self.finished.emit()


class Downloader(QObject):
    progress = Signal(int)
    finished = Signal()

    def __init__(self, videos):
        super().__init__()
        self.videos = videos

    def run(self):
        for video in self.videos:
            v = YouTube(video[0]).streams.get_audio_only("mp4")
            invalidChars = '\/:?*|"<>'
            title = v.title
            for char in invalidChars:
                title = title.replace(char, "_")
            v.download(musicpath, f"{title}.mp3")
            self.progress.emit(1)
        self.progress.emit(0)
        self.finished.emit()


if __name__ == '__main__':
    app = QApplication([])
    app.setStyleSheet(qdarktheme.load_stylesheet())
    window = DownloadAlert()
    window.exec()
