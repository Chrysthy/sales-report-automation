import pyautogui
import time
import pandas
import pyperclip
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

pyautogui.click(x=424, y=369, clicks=2)
time.sleep(1)
pyautogui.click(x=407, y=444) 
pyautogui.click(x=502, y=365) 
time.sleep(2)
pyautogui.click(x=582, y=452) 
time.sleep(3)
pyautogui.press("enter")

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
time.sleep(3)

pyautogui.write('xxxxx@gmail.com')
pyautogui.press('tab')
pyautogui.press('tab')
pyperclip.copy('Relatório de Vendas')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('tab')
message = f"""
    Prezado(a),
    Segue o relatório de vendas do mês de dezembro.

    Faturamento: R$ {total_sales:,.2f}
    Quantidade de produtos vendidos: {total_items:,}

    Atenciosamente,

    Chrystine
"""

pyperclip.copy(message)
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('ctrl', 'enter')
