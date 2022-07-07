import logging
import os
from contextlib import redirect_stderr
from io import BytesIO, StringIO
from pathlib import Path
from secrets import SystemRandom
from time import perf_counter

import numpy as np
import requests
from bs4 import BeautifulSoup
from moviepy.editor import *
from PIL import Image
from PySide6.QtCore import QObject, Signal

from main import convertTime

#####################################################
# PARMETERS SECTION

RESOLUTION = (240, 140)
FPS = 8
rand = SystemRandom()

bumblepath = Path(Path.home(), "Videos", "bumblefolder")
exportpath = bumblepath / "output"
musicpath = bumblepath / "music"
exportpath.mkdir(parents=True, exist_ok=True)
musicpath.mkdir(parents=True, exist_ok=True)
logfile = bumblepath / "log.log"
logging.basicConfig(filename=logfile)


class VideoMaker(QObject):
    progress = Signal(int)
    finished = Signal()
    addToLog = Signal(str)
    notify = Signal(str, int, Path)
    error = Signal()

    def __init__(self, thing, count, cool, include):
        super().__init__()
        self.thing = thing
        self.count = count
        self.cool = cool
        self.include = include

    def updateBar(self, finalvideo, filepath: Path):
        with redirect_stderr(BarReader(self.progress)):

            finalvideo.write_videofile(
                f"{filepath}", temp_audiofile=f"{exportpath/'temp_audio.mp3'}", fps=self.FPS, audio_bitrate="45k", bitrate="6k", threads=16, preset="ultrafast")

    def run(self):
        start = perf_counter()
        randomhandfulcount = int(self.count * 2)
        self.FPS = 8 if self.cool else 1
        log = self.addToLog.emit
        log("bumblefuck list generator")
        introtext = f"top {self.count} \n{self.thing}"
        if self.include:
            introtext += "s"

        try:
            url = f"https://www.google.com/search?tbm=isch&oq=&aqs=&q={self.thing.replace(' ', '+')}"

            imglinks = []
            while len(imglinks) < randomhandfulcount:
                page = requests.get(url)
                soup = BeautifulSoup(page.content, "lxml")
                imgs = soup.find_all("img", {"class": "yWs4tf"})
                imglinks.extend(img.get("src") for img in imgs)
                nextBtn = soup.find_all("a", {"class": "frGj1b"})
                match len(nextBtn):
                    case 1:
                        nextUrl = nextBtn[0].get("href")
                    case 2:
                        nextUrl = nextBtn[1].get("href")
                    case _:
                        pass

                url = f"https://google.com{nextUrl}"

                log(f"got {len(imglinks)} images...")

            imageresults = []

            log("downloading and shuffling images...")
            _imglinks = rand.sample(imglinks, self.count)
            for (i, x) in enumerate(_imglinks):
                a = requests.get(x)
                if a.status_code == 200:
                    log(f"downloading image {i+1}...")
                    temp_img = Image.open(
                        BytesIO(a.content))

                    imageresults.append(temp_img)
                else:
                    log(
                        f"Unable to retrieve sufficient images, stopping at {len(imageresults)}")
                    break

            rand.shuffle(imageresults)

            log("checking directories...")

            log("starting video creation...")

            try:
                self.buildVideo(
                    introtext, imageresults, log, start)
            except Exception as e:
                logging.error(e)
        except Exception as e:
            logging.error(e)
            log("Error during video creation, see log file for more info.")
            self.error.emit()

    def buildVideo(self, introtext, imageresults, log, start):
        if self.cool:
            color = ColorClip(size=RESOLUTION, duration=2.5,
                              color=[66, 128, 214])
            intro = TextClip(introtext, fontsize=35, color='white', font='Comic-Sans-MS',
                             size=RESOLUTION).set_pos('center').set_duration(2.5).crossfadein(0.3)

            introshadow = intro.invert_colors().set_position(
                ((RESOLUTION[0] * 0.01), (RESOLUTION[1] * 0.01))).crossfadein(0.3)
            introshadow = introshadow.crossfadein(0.3)

            intro = CompositeVideoClip([color, introshadow, intro])

        else:
            color = ColorClip(size=RESOLUTION, duration=2.5,
                              color=[66, 128, 214])
            intro = TextClip(introtext, fontsize=35, color='white', font='Comic-Sans-MS',
                             size=RESOLUTION).set_pos('center').set_duration(2.5)

            intro = CompositeVideoClip([color, intro])

        cliplist = [intro]

        samples = rand.sample(imageresults, self.count)

        for index, x in enumerate(samples):
            if self.cool:
                numberclip = TextClip("number \n" + str(self.count - index), fontsize=35,
                                      color='white', font='Comic-Sans-MS', size=RESOLUTION)
                numberclip = numberclip.set_pos(
                    'center').set_duration(2.5).crossfadein(0.3)

                numberclipshadow = numberclip.invert_colors().set_position(
                    ((RESOLUTION[0] * 0.01), (RESOLUTION[1] * 0.01)))
                numberclipshadow = numberclipshadow.crossfadein(0.3)

                numberclip = CompositeVideoClip(
                    [color, numberclipshadow, numberclip])

            else:
                numberclip = TextClip("number \n" + str(self.count - index), fontsize=35,
                                      color='white', font='Comic-Sans-MS', size=RESOLUTION)
                numberclip = numberclip.set_pos(
                    'center').set_duration(2.5)

                numberclip = CompositeVideoClip([color, numberclip])

            temp_img = x

            imageclip = ImageClip(img=np.array(temp_img)).resize(
                RESOLUTION).set_duration(3)

            cliplist.append(numberclip)
            cliplist.append(imageclip)
            log(f"added image {index+1}...")
        finalvideo = concatenate_videoclips(cliplist)

        if len(os.listdir(musicpath)) != 0:

            musiclist = [AudioFileClip(f"{musicpath}/{x}")
                         for x in os.listdir(musicpath)]
            rand.shuffle(musiclist)

            musiclist = concatenate_audioclips(musiclist)

            musiclist = musiclist.set_duration(
                finalvideo.duration).set_fps(1)

            finalvideo.audio = musiclist

        filepath = exportpath / f"{self.thing}.mp4"
        self.updateBar(finalvideo, filepath)
        end = perf_counter()
        # copy(path.getsize(path.normpath(filepath)))
        log(f"Time elapsed: {convertTime(round(end-start))}")
        self.notify.emit(self.thing, self.count, filepath)
        self.finished.emit()


class BarReader(StringIO):
    def __init__(self, signal: Signal):
        super().__init__(newline="\n")
        self.signal = signal

    def write(self, __s: str) -> int:
        percentage = 0

        if "%" in __s:
            if "chunk:" in __s:
                v = __s.index("%")  # index in sys.stdout where the nan is
                percentage = int(__s[v-2:v:]) / 2
            if "t:" in __s:
                v = __s.index("%")  # index in sys.stdout where the nan is
                percentage = 50 + (int(__s[v-2:v:]) / 2)
        # self.window.progressBar.setValue(percentage)
        self.signal.emit(percentage)
