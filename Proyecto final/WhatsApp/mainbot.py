from turtle import Terminator
import pyautogui as pt
from time import sleep 
import pyperclip
import Classes
from Classes import UsersData
sleep (3)

class buscador: 
    def sendMsg(self, texto:str):
        #se encarga de enviar el mensaje
        buscador.searchTextBubble()
        c = ""
        pt.doubleClick
        for a in texto: 
            if a != "\n":
                c = c + a
            else:
                pt.typewrite (c, interval=.003)
                c = ""
                pt.hotkey("shift", "enter")
        pt.press("enter")
        
    def searchTextBubble():
        #busca la imagen de texto 
        global x, y
        position2 = pt.locateOnScreen("WhatsApp/barra_mensajes.png", confidence=.6) 
        x = position2 [0]
        y = position2 [1]
        pt.moveTo(x,y, duration=0.5)
        pt.moveTo(x,y, duration=.5)
        pt.moveTo(x+200, y-(-0), duration=.5)

    def readMsg(self):
        #lee el mensaje 
        sleep (5)
        buscador.searchTextBubble()
        pt.moveTo(x+59, y-65, duration=.5)
        pt.tripleClick()
        pt.rightClick()
        sleep (1)
        pt.moveTo(x+100, y-45, duration=.5)
        pt.click()
        msg = pyperclip.paste()
        print("Mensaje recibido ", msg)
        return msg

searcher = buscador()
Users = Classes.UsersData()

def createUser():
    #crea el usuario
    searcher.sendMsg("Desea crear cuenta de usuario o domiciliario?\n 1. Usuario\n 2. Domiciliario\n")
    a = searcher.readMsg()
    searcher.searchTextBubble()
    searcher.sendMsg("Digite su numero")
    num = searcher.readMsg()
    if a == "1":
        Users.usersDict.update({num: 0})
    if a == "2":
        pass

while __name__ == "__main__":
    #main
    searcher.searchTextBubble()
    searcher.sendMsg("Bienvenido!\n1. Realizar pedido\n2. Crear usuario\n3. Ver saldo\n4. Salir\n")
    
    wait = False
    if wpp_message == "1" and wait == True:
        searcher.sendMsg(Classes.Terrase.showMenu())
    elif wpp_message == "2" and wait == True:
        searcher.sendMsg("Digite su numero\n")
        num = searcher.readMsg()
        Users.usersDict.update({num: 0})
        print(Users.usersDict)
    elif wpp_message == "3" and wait == True:
        searcher.sendMsg("Coming Soon")
    elif wpp_message == "4" and wait == True:
        chatOn = False
        searcher.sendMsg("Muchas Gracias!\n")
    else:
        wpp_message = searcher.readMsg()
        if wpp_message != None:
            wait = True



