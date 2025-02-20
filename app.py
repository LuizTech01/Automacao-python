import pyautogui
from time import sleep

pyautogui.click(967,596,duration=2)

pyautogui.click(1012,540,duration=2)
pyautogui.write('User')

pyautogui.click(1012,568,duration=2)
pyautogui.write('User123')

pyautogui.click(910,598,duration=2)

pyautogui.click(970,543,duration=2)
pyautogui.write('User')

pyautogui.click(1004,567,duration=2)
pyautogui.write('User123')

pyautogui.click(872,595,duration=2)

with open('produtos.txt', 'r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]

        pyautogui.click(708,527,duration=2)
        pyautogui.write(produto)

        pyautogui.click(712,554,duration=2)
        pyautogui.write(quantidade)

        pyautogui.click(709,581,duration=2)
        pyautogui.write(preco)

        pyautogui.click(594,737,duration=2)
        sleep(1)