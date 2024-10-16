import pyautogui
import time

# Sleep for a few seconds to give you time to switch to the window you want to automate
time.sleep(5)

# Move the mouse to position (x, y) and click
x, y, z = 1000, 200 , -500 # Replace with your desired coordinates
pyautogui.moveTo(x, y, z)
pyautogui.click()

# Optional: Repeat clicking every 10 seconds
while True:
    pyautogui.click(x, y, z)
    time.sleep(5)
