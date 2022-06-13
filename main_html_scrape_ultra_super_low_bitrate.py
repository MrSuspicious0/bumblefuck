import logging
import os
from contextlib import redirect_stderr
from io import BytesIO, StringIO
from os import path
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

# thing = input("thing: ")
# count = int(input("count: "))
basedir = path.normpath(path.expanduser("~"))
bumblepath = path.join(
    basedir, "Videos", "bumblefolder")
exportpath = path.join(bumblepath, "output")
musicpath = path.join(bumblepath, "music")
# cool = input("cool transitions and details? (y/n): ")
# include = input("include 's' on name? (y/n): ")
if not path.isdir(exportpath):
    os.makedirs(exportpath)

if not path.isdir(musicpath):
    os.makedirs(musicpath)
logging.basicConfig(filename=path.join(bumblepath, "log.log"))


class VideoMaker(QObject):
    progress = Signal(int)
    finished = Signal()
    addToLog = Signal(str)

    def __init__(self, thing, count, cool, include):
        super().__init__()
        self.thing = thing
        self.count = count
        self.cool = cool
        self.include = include

    def updateBar(self, finalvideo, filepath):
        with redirect_stderr(BarReader(self.progress)):

            finalvideo.write_videofile(
                filepath, fps=self.FPS, audio_bitrate="45k", bitrate="6k")

    def run(self):
        start = perf_counter()
        randomhandfulcount = int(self.count * 2)
        self.FPS = 1 if not self.cool else 8
        log = self.addToLog.emit
        log("bumblefuck list generator")
        introtext = f"top {self.count} \n{self.thing}"
        if self.include:
            introtext += "s"

    # you can't just drop in another website, I did this specifically to work with google images
    ####################################################

        url = f"https://www.google.com/search?tbm=isch&oq=&aqs=&q={self.thing.replace(' ', '+')}"

        imglinks = list()
        while len(imglinks) < randomhandfulcount:
            page = requests.get(url)
            soup = BeautifulSoup(page.content, "lxml")
            imgs = soup.find_all("img", {"class": "yWs4tf"})
            for img in imgs:
                imglinks.append(img.get("src"))

            nextBtn = soup.find_all("a", {"class": "frGj1b"})
            match len(nextBtn):
                case 1:
                    nextUrl = nextBtn[0].get("href")
                case 2:
                    nextUrl = nextBtn[1].get("href")
                case _:
                    pass

            url = f"https://google.com{nextUrl}"

            # print("got " + str(len(imglinks)) + " images...")
            log(f"got {len(imglinks)} images...")

        imageresults = []

        log("downloading and shuffling images...")
        _imglinks = rand.sample(imglinks, self.count)
        for x in _imglinks:
            temp_img = Image.open(
                BytesIO(requests.get(x).content))

            imageresults.append(temp_img)

        rand.shuffle(imageresults)

        # temp_img.show()

        # time.sleep(100000)
        # just dont try and do the rest

        log("checking directories...")

        log("starting video creation...")

        try:
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

            index = 0

            samples = rand.sample(imageresults, self.count)

            for x in samples:
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
                    numberclip = numberclip.set_pos('center').set_duration(2.5)

                    numberclip = CompositeVideoClip([color, numberclip])

                temp_img = x

                imageclip = ImageClip(img=np.array(temp_img)).resize(
                    RESOLUTION).set_duration(3)

                cliplist.append(numberclip)
                cliplist.append(imageclip)

                index += 1

            finalvideo = concatenate_videoclips(cliplist)

            if len(os.listdir(musicpath)) != 0:

                musiclist = []
                for x in os.listdir(musicpath):
                    musiclist.append(AudioFileClip(musicpath + "/" + x))

                rand.shuffle(musiclist)

                musiclist = concatenate_audioclips(musiclist)

                musiclist = musiclist.set_duration(
                    finalvideo.duration).set_fps(1)

                finalvideo.audio = musiclist

            filepath = f"{exportpath}/{self.thing}.mp4"
            self.updateBar(finalvideo, filepath)
            end = perf_counter()
            log(f"Time elapsed: {convertTime(round(end-start, 2))}")
            self.finished.emit()
        except Exception as e:
            logging.error(e)
            log(e)


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
