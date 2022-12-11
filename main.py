import pydirectinput as pg
import pyautogui as py
import time

time.sleep(5)
pg.PAUSE = 0.01
py.PAUSE = 0.01

while True:
    pg.press("space")