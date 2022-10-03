import pyautogui as pt
from time import sleep 
import pyperclip
import random

sleep (3)
position1 = pt.locateOnScreen("WhatsApp/barra_mensajes.png", confidence=.6)
x = position1 [0]
y = position1 [1]

#gets message   
class buscador: 
    def barra_mensajes(self):

        global x, y
        position2 = pt.locateOnScreen("WhatsApp/barra_mensajes.png", confidence=.6) #este métpodo es propio dE Python 
        x = position2 [0]
        y = position2 [1]
        pt.moveTo(x,y, duration=0.5)
        pt.moveTo(x,y, duration=.5)
        pt.moveTo(x+200, y-(-0), duration=.5)
        pt.doubleClick()
        self.escribir()


    #escribir

    def escribir(self):
        pt.typewrite ("Bienvenido", interval=.01)

searcher = buscador()
searcher.barra_mensajes()


#def enviar(self):
pt.moveTo(x+575, y+2, duration=.5)
pt.click()









