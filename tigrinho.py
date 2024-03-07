from subprocess import Popen
import pywinauto as pyau
import pyautogui as teclado
import time
import keyboard
import sys
exitProgram = False

def quit():
    global exitProgram
    exitProgram=True
    
  
keyboard.add_hotkey('`', lambda: quit())


def closeTab():
    teclado.keyDown('alt')
    teclado.keyDown('f4')

    time.sleep(1)

    teclado.keyUp('alt')
    teclado.keyUp('f4')

def outString (x, y):
    return (f"{x}{y}@gmail.com")

index = 95
nome = "lawd"
senha = "lawdd123"


while not exitProgram:
    app = pyau.Application().start(cmd_line=u'C:/Users/minha/AppData/Local/Programs/Opera GX/launcher.exe')
    time.sleep(3)
    teclado.keyDown('ctrl')
    teclado.keyDown('shift')
    teclado.keyDown('N')

    teclado.keyUp('ctrl')
    teclado.keyUp('shift')
    teclado.keyUp('N')

    time.sleep(3)

    teclado.typewrite('https://www.win7b.com')
    teclado.press('enter')

    time.sleep(3)

    teclado.moveTo(1200, 360, duration=1)
    teclado.click()

    time.sleep(3)

    teclado.moveTo(1769, 214, duration=1)
    teclado.click()

    teclado.press('tab')
    teclado.typewrite(outString(nome, index))
    print(outString(nome, index))
    index += 1 

    time.sleep(3)

    teclado.press('tab')
    teclado.typewrite(senha)
    time.sleep(3)
    teclado.press('enter')

    time.sleep(3)


    closeTab()
    closeTab()

print("bye bye")


