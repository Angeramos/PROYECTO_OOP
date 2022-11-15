from turtle import Terminator
import pyautogui as pt
from time import sleep 
import pyperclip
import LinkedList
sleep (3)

class buscador: 
    def sendMsg(self, texto:str):
        #se encarga de enviar el mensaje
        buscador.searchTextBubble()
        c = ""
        pt.doubleClick()
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
        position2 = pt.locateOnScreen(r"Proyecto final\WhatsApp\BarraMensajesNuevas.png", confidence=.6) 
        x = position2 [0]
        y = position2 [1]
        pt.moveTo(x,y, duration=0.5)
        pt.moveTo(x,y, duration=.5)
        pt.moveTo(x+200, y-(-0), duration=.5)

    def readMsg(self):
        #lee el mensaje 
        msg = None
        while msg == None:
            sleep (5)
            buscador.searchTextBubble()
            print("entro ")
            pt.moveTo(x+65, y-65, duration=.5)
            pt.tripleClick()
            pt.rightClick()
            sleep (1)
            pt.moveTo(x+100, y-45, duration=.5)
            pt.click()
            pyperclip.waitForPaste()
            msg = pyperclip.paste()
            print("Mensaje recibido ", msg)
        return msg

searcher = buscador()
Users = LinkedList.LinkedListUser()
Domiciliarios = LinkedList.LinkedListDomiciliario()
Menu = LinkedList.LinkedListMenu()
Users.fillUserList()
Menu.fillMenu()
Domiciliarios.fillDomiciliarioList()

def createUser():
    #crea el usuario
    searcher.sendMsg("Desea crear cuenta de usuario o domiciliario?\n 1. Usuario\n 2. Domiciliario\n")
    a = searcher.readMsg()
    searcher.searchTextBubble
    searcher.sendMsg("Digite su codigo estudiantil\n")
    CE = searcher.readMsg()
    searcher.sendMsg("Como es su nombre?\n")
    Name = searcher.readMsg()
    if (CE != None) and (Users.search(CE) == None):
        if a == "1":
            Users.AddUserNode(CE, Name, "0")
            Users.addUserToFile(r"Proyecto final\WhatsApp\users.csv", CE, Name)
            print(Users)
        if a == "2":
            Domiciliarios.AddDomiciliarioNode(CE, Name)
            Domiciliarios.addUserToFile(r"Proyecto final\WhatsApp\Domiciliarios.csv", CE, Name)
    else:
        searcher.sendMsg("El usuario ya existe")
    
while __name__ == "__main__":
    #main
    print(Users)
    searcher.searchTextBubble
    searcher.sendMsg("Bienvenido!\n1. Realizar pedido\n2. Crear usuario\n3. Ver saldo\n4. Salir\n")
    wpp_message = searcher.readMsg()
    wait = True
    if wpp_message == "1" and wait == True:
        searcher.sendMsg(Menu.showMenu())
    elif wpp_message == "2" and wait == True:
        createUser()
    elif wpp_message == "3" and wait == True:
        searcher.sendMsg("Ingrese su codigo estudiantil")
        saldo = searcher.readMsg()
        User = Users.search()
        searcher.sendMsg("Su saldo actual es: " + User.Wallet)
    elif wpp_message == "4" and wait == True:
        searcher.sendMsg("Muchas Gracias!\n")
        break
    else:
        wpp_message = searcher.readMsg()
        wait = False



