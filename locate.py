import pyautogui
import time

print("You have 5 seconds to move your mouse to the target location...")
time.sleep(5)

x, y = pyautogui.position()
print(f"Mouse is at: X={x}, Y={y}")
