import os
from os import path
from io import BytesIO, StringIO
from secrets import SystemRandom

import numpy as np
import requests
from bs4 import BeautifulSoup
from moviepy.editor import *
from PIL import Image
import main
from functools import partial
from threading import Thread
from contextlib import redirect_stderr
#####################################################
# PARMETERS SECTION

RESOLUTION = (240, 140)
FPS = 8
rand = SystemRandom()

# thing = input("thing: ")
# count = int(input("count: "))
# cool = input("cool transitions and details? (y/n): ")
# include = input("include 's' on name? (y/n): ")


class DogNigga(StringIO):
    def __init__(self, window: main.MainWindow):
        super().__init__(newline="\n")
        self.window = window

    def write(self, __s: str) -> int:
        percentage = 0

        if "%" in __s:
            if "chunk:" in __s:
                v = __s.index("%")  # index in sys.stdout where the nan is
                percentage = int(__s[v-2:v:]) / 2
            if "t:" in __s:
                v = __s.index("%")  # index in sys.stdout where the nan is
                percentage = 50 + (int(__s[v-2:v:]) / 2)
        self.window.progressBar.setValue(percentage)


def updateBar(window: main.MainWindow, finalvideo, exportpath):

    with redirect_stderr(DogNigga(window)):

        finalvideo.write_videofile(
            exportpath, fps=FPS, audio_bitrate="45k", bitrate="6k")
        window.btnRender.setEnabled(True)
    # while True:

    #     percentage = 0

    #     sys.stdout = buffer = StringIO()

    #     txt = buffer.getvalue()

    #     if "Moviepy - Done !" in txt:
    #         break

    #     if "%" in txt:
    #         if "chunk" in txt:
    #             v = txt.index("%")  # index in sys.stdout where the nan is
    #             percentage = int(txt[v-2:v:]) / 2
    #         if "t" in txt:
    #             v = txt.index("%")  # index in sys.stdout where the nan is
    #             percentage = 50 + (int(txt[v-2:v:]) / 2)
    #     window.progressBar.setValue(percentage)


def _updateBar(window: main.MainWindow):
    t = Thread(target=updateBar, args=(window))
    t.start()


def changeLog(window: main.MainWindow, txt):
    window.txtLogOutput.insertPlainText(f"{txt}\n")
    window.txtLogOutput.moveCursor(main.QTextCursor.End)


def _doIt(thing, count, cool, include, window):
    t = Thread(target=doIt, args=(thing, count, cool, include, window))
    t.start()


def doIt(thing, count, cool, include, window: main.MainWindow):
    global FPS, RESOLUTION
    randomhandfulcount = int(count * 2)
    FPS = 1 if not cool else 8
    log = partial(changeLog, window)
    log("Top list generator Joshtifer edition")
    introtext = f"top {count} \n{thing}"
    if include:
        introtext += "s"

    basedir = path.normpath(path.expanduser("~"))
    exportpath = path.join(
        basedir, "Videos", "bumblefolder", "output", )
    musicpath = path.join(basedir, "Videos", "bumblefolder", "music")

    try:
        os.makedirs(exportpath)
    except:
        pass

    try:
        os.makedirs(musicpath)
    except:
        pass
# you can't just drop in another website, I did this specifically to work with google images
####################################################

    image_tags = list()
    url = f"https://www.google.com/search?tbm=isch&oq=&aqs=&q={thing.replace(' ', '+')}"

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

    log("downloading and shuffling images")
    _imglinks = rand.sample(imglinks, count)
    for x in _imglinks:
        temp_img = Image.open(
            BytesIO(requests.get(x).content))

        imageresults.append(temp_img)

    rand.shuffle(imageresults)
# for index, img in enumerate(imageresults):
#     img.save(f"img/{index}.png")
# temp_img.show()


# time.sleep(100000)
# just dont try and do the rest

    log("checking directories...")

    log("starting video creation...")

    if cool:
        color = ColorClip(size=RESOLUTION, duration=2.5, color=[66, 128, 214])
        intro = TextClip(introtext, fontsize=35, color='white', font='Comic-Sans-MS',
                         size=RESOLUTION).set_pos('center').set_duration(2.5).crossfadein(0.3)

        introshadow = intro.invert_colors().set_position(
            ((RESOLUTION[0] * 0.01), (RESOLUTION[1] * 0.01))).crossfadein(0.3)
        introshadow = introshadow.crossfadein(0.3)

        intro = CompositeVideoClip([color, introshadow, intro])

    else:
        color = ColorClip(size=RESOLUTION, duration=2.5, color=[66, 128, 214])
        intro = TextClip(introtext, fontsize=35, color='white', font='Comic-Sans-MS',
                         size=RESOLUTION).set_pos('center').set_duration(2.5)

        intro = CompositeVideoClip([color, intro])

    my_bytes_io = BytesIO()

    cliplist = [intro]

    index = 0

    samples = rand.sample(imageresults, count)

    for x in samples:
        if cool:
            numberclip = TextClip("number \n" + str(count - index), fontsize=35,
                                  color='white', font='Comic-Sans-MS', size=RESOLUTION)
            numberclip = numberclip.set_pos(
                'center').set_duration(2.5).crossfadein(0.3)

            numberclipshadow = numberclip.invert_colors().set_position(
                ((RESOLUTION[0] * 0.01), (RESOLUTION[1] * 0.01)))
            numberclipshadow = numberclipshadow.crossfadein(0.3)

            numberclip = CompositeVideoClip(
                [color, numberclipshadow, numberclip])

        else:
            numberclip = TextClip("number \n" + str(count - index), fontsize=35,
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

        musiclist = musiclist.set_duration(finalvideo.duration).set_fps(1)

        finalvideo.audio = musiclist

    updateBar(window, finalvideo, exportpath + f"/{thing}.mp4")
    log("Done!")
