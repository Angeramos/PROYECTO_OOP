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
        position2 = pt.locateOnScreen(r"Proyecto final\WhatsApp\BarraMensajesV2.png", confidence=.4) 
        x = position2[0]    
        y = position2[1]
        pt.moveTo(x,y, duration=0.5)
        pt.moveTo(x,y, duration=.5)
        pt.moveTo(x+200, y-(-0), duration=.5)

    def readMsg(self):
        #lee el mensaje 
        msg = None
        while msg == None:
            sleep (15)
            buscador.searchTextBubble()
            pt.moveTo(x+400, y-65, duration=.5)
            pt.tripleClick()
            pt.rightClick()
            sleep (1)
            pt.moveTo(x+420, y-300, duration=.5)
            pt.doubleClick()
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
    while a !="1" and a!="2":
        searcher.sendMsg("La respuesta no es valida, digitela de nuevo\n")
        a = searcher.readMsg()
    searcher.searchTextBubble
    searcher.sendMsg("Digite su codigo estudiantil\n")
    CE = searcher.readMsg()
    searcher.sendMsg("Como es su nombre?\n")
    Name = searcher.readMsg()
    if (CE != None) and (Users.search(CE) == None):
        if a == "1":
            Users.AddUserNode(CE, Name, "50000")
            Users.addUserToFile(r"Proyecto final\WhatsApp\users.csv", CE, Name)
        if a == "2":
            Domiciliarios.AddDomiciliarioNode(CE, Name)
            Domiciliarios.addUserToFile(r"Proyecto final\WhatsApp\Domiciliarios.csv", CE, Name)
        searcher.sendMsg("Usuario creado!\n")
    else:
        searcher.sendMsg("El usuario ya existe\n")
    
while __name__ == "__main__":
    searcher.sendMsg("Bienvenido!\n1. Realizar pedido\n2. Crear usuario\n3. Ver saldo\n4. Salir\n")
    wpp_message = searcher.readMsg()
    while wpp_message != "1" and wpp_message != "2" and wpp_message != "3" and wpp_message != "4":
        searcher.sendMsg("La respuesta no es valida, digitela de nuevo\n")
        wpp_message = searcher.readMsg()
    wait = True
    if wpp_message == "1" and wait == True:
        searcher.sendMsg("Que desea realizar?\n1. Ver menu\n2. Ver carrito\n")
        if searcher.readMsg() == "1":
            searcher.sendMsg(Menu.showMenu())
            searcher.sendMsg("Desea ordenar algo?\n1. Si\n2. No\n")
            wpp_message = searcher.readMsg()
            while wpp_message != "1" and wpp_message != "2":
                searcher.sendMsg("La respuesta no es valida, digitela de nuevo\n")
                wpp_message = searcher.readMsg()
            if wpp_message == "1":
                searcher.sendMsg("Digite su Codigo Estudiantil\n")
                tempUser = searcher.readMsg()
                tempUser = Users.search(tempUser)
                while tempUser == None:
                    searcher.sendMsg("El usuario no existe, desea crearlo?\n1. Si\n2. No\n")
                    temp = searcher.readMsg()
                    if  temp == "1":
                        createUser()
                    elif temp == "2":
                        break 
                    tempUser = searcher.readMsg()
                    tempUser = Users.search(tempUser)
                    break
                order = True
                while order == True:
                    searcher.sendMsg("Digite la opcion que desea\n")
                    it = searcher.readMsg()
                    item = Menu.search(it) 
                    if item != None:
                        tempUser.cart.AddNodeCart(item.number, item.price)
                    elif item == None:
                        searcher.sendMsg("Este item no existe o no se encuentra disponible por el momento\n")
                    searcher.sendMsg("Desea ordenar algo mas?\n1. Si\n2. No\n")
                    wpp_message = searcher.readMsg()
                    if wpp_message == "1":
                        order = True
                    elif wpp_message == "2":
                        order = False 
            elif wpp_message == "2":
                break              
        elif searcher.readMsg () == "2":
            tempUser = searcher.readMsg()
            searchUser = Users.search(tempUser)
            if searchUser != None:
                try:
                    searcher.sendMsg("Que desea realizar?\n1. Pagar\n2. Eliminar item\n")
                    wpp_message = searcher.readMsg()
                    if wpp_message == "1":
                        searchUser.payPedido()
                        P = Domiciliarios.searchLess()
                        P.AddPedidoNode(searchUser.getPedido(), str(searchUser.showCartTotal()))
                except AttributeError:
                    searcher.sendMsg("No tiene ningun item en el pedido\n")
            
    elif wpp_message == "2" and wait == True:
        createUser()
    elif wpp_message == "3" and wait == True:
        searcher.sendMsg("Ingrese su codigo estudiantil\n")
        saldo = searcher.readMsg()
        User = Users.search(saldo)
        searcher.sendMsg("Su saldo actual es: " + User.Wallet)
    elif wpp_message == "4" and wait == True:
        searcher.sendMsg("Muchas Gracias!\n")
        break
    else:
        wpp_message = searcher.readMsg()
        wait = False



