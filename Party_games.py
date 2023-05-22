import pyautogui
import time

dirt = "1"
wood = "2"
stone = "3"

x_top_left = 710
y_top_left = 322
x_bottom_right = 1225
y_bottom_right = 834

width = x_bottom_right - x_top_left
height = y_bottom_right - y_top_left

region = (x_top_left, y_top_left, width, height)

yes = True
while yes:
    for x in range(x_top_left, x_bottom_right, 30):
        screenshot = pyautogui.screenshot(region=region)
        screenshot.save("screenshot.png")
        for y in range(y_top_left, y_bottom_right, 30):
            screenshot = pyautogui.screenshot(region=region)
            
            print(x, y)

            # Dirt
            if screenshot.getpixel((x-710, y-322)) in [(183, 131, 91), (120, 84, 57), (88, 60, 40)]:
                pyautogui.press(dirt)
                break

            # Wood
            if screenshot.getpixel((x-710, y-322)) in [(186, 150, 97), (157, 130, 76), (114, 93, 56), (104, 83, 50)]:
                pyautogui.press(wood)
                break

            # Stone
            if screenshot.getpixel((x-710, y-322)) in [(125, 125, 125), (115, 115, 115), (103, 103, 103)]:
                pyautogui.press(stone)
                break


