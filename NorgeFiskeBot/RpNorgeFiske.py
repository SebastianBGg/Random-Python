import pyautogui as pg
import time
import keyboard
import random
import os
from Direct import PressKey, ReleaseKey
fisk = 0
keys = "num1"
def run():
    aggg = 1
    tall = 0
    santtt = 0
    TEST = 0
    shotpath = os.path.abspath(os.getcwd()) + "\shot.png"
    shot1path = os.path.abspath(os.getcwd()) + "\shot1.png"
    print(shotpath)
    print(shot1path)
    tilfeldig = random.randint(1, 2)
    if tilfeldig == 1:
        print("JA")
        time.sleep(0.5)
        PressKey(0x11)
        time.sleep(1)
        ReleaseKey(0x11)
    while aggg == 1:
        sant = 0
        search_region = (930, 778, 56, 58)
        TEST += 1
        print(str(TEST))

        screenshot_region = (858, 732, 208, 164)

        color = (34, 34, 34)
        color2 = (255, 255, 255)
        time.sleep(1)
        screenshot = pg.screenshot(region=screenshot_region)
        screenshot.save(shotpath)
        if screenshot.getpixel((87, 69)) == color2:
            key = "1"
            sant = 1
        if screenshot.getpixel((119, 95)) == color2:
            key = "2"
            sant = 1
        if screenshot.getpixel((118, 76)) == color2:
            key = "3"
            sant = 1
        if screenshot.getpixel((88, 75)) == color2:
            key = "4"
            sant = 1
        while sant == 1:
            print("sant")
            santtt += 1
            if santtt == 5:
                return
            for x in reversed(range(screenshot.width)):
                for y in range(screenshot.height):
                    if screenshot.getpixel((x, y)) == color:
                        print(x,y)
                        siste = 1
                        while siste == 1:
                            tall += 1
                            print("siste"+str(tall))
                            ss = pg.screenshot(region=screenshot_region)
                            ss.save(shot1path)
                            if tall == 300:
                                print("break")
                                return
                            if ss.getpixel((x, y)) == color2:
                                print(x,y)
                                print("click")
                                print(key)
                                pg.press(key)
                                return
while True:

    run()
