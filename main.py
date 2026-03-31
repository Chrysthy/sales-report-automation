import pyautogui
import time
pyautogui.PAUSE = 1

pyautogui.click 
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

time.sleep(2)

link = 'https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga'

pyautogui.write(link)
pyautogui.press('enter')
time.sleep(3)

pyautogui.click(x=483, y=607, clicks=2)
pyautogui.click(x=595, y=595)
time.sleep(2)
pyautogui.click(x=678, y=620)
time.sleep(3)