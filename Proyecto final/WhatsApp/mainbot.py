from turtle import Terminator
import pyautogui as pt
from time import sleep 
import pyperclip
import Classes
from Classes import UsersData
sleep (3)
#gets message           
class buscador: 
    def barra_mensajes(self):
        global x, y
        position2 = pt.locateOnScreen("barra_mensajes.png", confidence=.6) #este métpodo es propio dE Python 
        x = position2 [0]
        y = position2 [1]
        pt.moveTo(x,y, duration=0.5)
        pt.moveTo(x,y, duration=.5)
        pt.moveTo(x+200, y-(-0), duration=.5)
        pt.click()
        

    #escribir
    def sendMsg(self, texto:str):
        pt.doubleClick
        pt.typewrite (texto, interval=.03)
        pt.click()

    ##def searchTextBubble():
        ##global x, y
        ##position2 = pt.locateOnScreen("WhatsApp/barra_mensajes.png", confidence=.6) #este métpodo es propio dE Python 
        #3x = position2 [0]
        ##y = position2 [1]
        ##pt.moveTo(x,y, duration=0.5)
        ##pt.moveTo(x,y, duration=.5)
        ##pt.moveTo(x+200, y-(-0), duration=.5)
    def readMsg(self):
        sleep (5)
        pt.moveTo(x+59, y-65, duration=.5)
        pt.tripleClick()
        pt.rightClick()

        sleep (1)
        pt.moveTo(x+100, y-45, duration=.5)
        pt.click()
        msg = pyperclip.paste()
        print("Mensaje recibido ", msg)
        return msg

chatOn = True
searcher = buscador()
Users = Classes.UsersData()

while chatOn:
    searcher.barra_mensajes()
    searcher.sendMsg("Bienvenido! Que desea ordenar?\n")
    searcher.sendMsg("1. Realizar pedido\n2. Crear usuario\n3.Ver saldo\n4.Salir\n")
    searcher.readMsg()  
    wpp_message = pyperclip.paste()
    print ("Mensaje recibido: " + wpp_message)
    wait = True
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


    



#class interacción():
#sleep (5)
#position1 = pt.locateOnScreen("WhatsApp/combo_terrase.png", confidence=.6)
#x = position1 [0]
#y = position1 [1]

#class interactuar: 
#    def leer(self):


#searcher = interactuar()
#searcher.leer()


