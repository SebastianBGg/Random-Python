import pyautogui
import keyboard
import mouse
import time

while True:
    if keyboard.is_pressed("p"):
        pyautogui.move(1000, 1000) 
        time.sleep(5)
    if keyboard.is_pressed("alt"):
        
        time.sleep(0.5)