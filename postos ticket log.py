import pyautogui as py
import time 
from time import sleep
py.PAUSE = 1.5

tes = "276"

py.click(x=892, y=1052) #abrir o protheus na barra de tarefa

py.click(x=112, y=214) #clicar na nota

for c in range(96):
    py.click(x=154, y=156) #vai classificar a nota
    time.sleep(5)
    py.press("enter") #confirma tela de erro
    time.sleep(5)
    py.click(x=1155, y=317) #clica no campo da TES
    py.write(tes) #escreve a TES
    py.press("right")
    py.click(x=1885, y=157) #salva lançamento
    time.sleep(2.5)
    py.press("down")
