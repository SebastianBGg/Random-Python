from time import sleep
import pyautogui as pg
import keyboard
import mss
import mss.tools
import pytesseract
from PIL import Image
from pyautogui import screenshot

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\sebbar001\AppData\Local\Tesseract-OCR\tesseract.exe"
print("Trykk et sted oppe venstere")
keyboard.wait("space")
mousepos = pg.position()
print("Trykk et sted nede høyere")
keyboard.wait("space")
mousepos2 = pg.position()
a = 1
keyboard.wait("space")


x = mousepos[0]
y = mousepos[1]
x2 = mousepos2[0]
y2 = mousepos2[1]
pos1 = x,y
pos2 = x2,y2
if y < y2:
    height = y2 - y
if y > y2:
    height = y - y2
if x < x2:
    width = x2 - x
if x > x2:  
    width = x - x2

print(width, height, x, y)
with mss.mss() as sct:

    region2 = {
        'height':height,
        'width': width,
        'left': x,
        'top': y,
        }
img = sct.grab(region2)
mss.tools.to_png(img.rgb, img.size, output='bilde.png')
text = pytesseract.image_to_string(Image.open("bilde.png"))
text = text.replace("\n", " ")
print(text)
pg.write(text, interval=0.1)
