import pyautogui
import time
import pandas
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
pyautogui.press('enter')
time.sleep(3)

path = r'C:\Users\chrys\Downloads\Vendas - Dez.xlsx'
table = pandas.read_excel(path)
print(table)

total_sales = table["Valor Final"].sum()
total_items = table['Quantidade'].sum()
print(total_sales)
print(total_items)

pyautogui.hotkey('ctrl', 't')
pyautogui.write('https://mail.google.com/mail/u/1/#inbox')
pyautogui.press('enter')
time.sleep(5)
pyautogui.click(x=91, y=215)
time.sleep(2)