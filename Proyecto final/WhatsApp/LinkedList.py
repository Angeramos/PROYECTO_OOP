class Nodo:
    """
    Clase general de Nodo
    """
    def __init__(self, data):
        self.data = data
        self.next = None
        self.cart = LinkedListCart()
    def __repr__(self):
        return str(self.data)

class Usuario(Nodo):
    """
    Clase Usuario heredada de nodo, esta maneja los datos del usuario para luego insertarlos en una LinkedList
    """
    def __init__(self, data, Name, Wallet):
        super().__init__(data)
        self.Name = Name
        self.Wallet = Wallet
        self.cart = LinkedListCart()
    def showCartTotal(self):
        P = self.cart.PTR
        Total = "0"
        while P != None:
            Total = int(Total) + int(P.price)
            P = P.next
        return Total    

class LinkedList:
    """
    Clase general de LinkedList
    """
    def __init__(self):
        self.PTR = None
        self.ULT = None

    def AddNode(self,data):
        #añade un nuevo nodo
        P = Nodo(data)
        if (self.PTR == None):
            self.PTR = P
            self.ULT = P 
        else:
            self.ULT.next = P
            self.ULT = P 

    def Recorrido(self):
        #recorre la lista
        P = self.PTR
        while(P != None):
            print(P.data, end="->")
            P = P.next
        print("None")
    
    def __repr__(self):
        respuesta = ""
        P = self.PTR
        while(P != None):
            respuesta = respuesta + str(P.data) + "->"
            P = P.next
        respuesta = respuesta + "None"
        return respuesta
    
class LinkedListUser(LinkedList):
    """
    LinkedList creada con el proposito de manejar los datos del usuario usando los nodos de tipo Usuario
    """
    def AddUserNode(self, data, Name, Wallet):
        P = Usuario(data, Name, Wallet)
        if (self.PTR == None):
            self.PTR = P
            self.ULT = P
        else:
            self.ULT.next = P
            self.ULT = P
    def search(self, data):
        P = self.PTR
        while (str(P.data) != data) or P.data != None:
            P = P.next
        return P
    def showBalance(self, data):
        P = self.PTR
        try:
            while P.data != None:
                if P.data == data :
                    a = P.Wallet
                    break
                P = P.next
        except AttributeError:
            a = "El usuario no existe"
        return a
    def fillUserList(self):
        f = open(r"Proyecto final\WhatsApp\users.csv", "r")
        for line in f.readlines():
            a = line.split(",")
            self.AddUserNode(a[0], a[1], a[2])
        f.close()
    def addUserToFile(self, file, CE, Name):
        P = self.ULT
        f = open(file, "a")
        f.write("\n")
        f.write(CE + "," + Name + ',' + "0")
        f.close()
    def updtFile(file, search, newData):
        f = open(file, "r")
        for line in f.readlines():
            a = line.split(",")
            if a[0] == search:
                print(a[0])
                break
        with open(file, "r") as f:
            data = f.read()
            data = data.replace(a[0]+","+a[1]+","+a[2], a[0]+","+a[1]+","+newData + "\n")
        with open(file, "w") as f:
                f.write(data)

class Domiciliario(Nodo):
    def __init__(self, data, Name):
        super().__init__(data)
        self.Name = Name
        self.Pedidos = LinkedListPedidos()

class Pedido(Nodo):
    def __init__(self, data, total):
        super().__init__(data)
        self.total = total
    
    def __repr__(self):
        return str(self.data + " - " + self.total)

class LinkedListPedidos(LinkedList):
    def AddPedidoNode(self, data, total):
        P = Pedido(data, total)
        if (self.PTR == None):
            self.PTR = P
            self.ULT = P
        else:
            self.ULT.next = P
            self.ULT = P
    def __len__(self):
        P = self.PTR
        count = 0
        while P != None:
            count = count + 1
            P = P.next
        return count
    def __repr__(self):
        respuesta = ""
        P = self.PTR
        while(P != None):
            respuesta = respuesta + str(P.data) + "  Total = " + str(P.total) + "->"
            P = P.next
        respuesta = respuesta + "None"
        return respuesta

class LinkedListDomiciliario (LinkedList):
    def AddDomiciliarioNode(self, data, Name):
        P = Domiciliario(data, Name)
        if (self.PTR == None):
            self.PTR = P
            self.ULT = P
        else:
            self.ULT.next = P
            self.ULT = P
    def search(self, data):
        P = self.PTR
        while (str(P.data) != data) or P.data != None:
            P = P.next
        return P
    def fillDomiciliarioList(self):
        f = open(r"Proyecto final\WhatsApp\Domiciliarios.csv", "r")
        for line in f.readlines():
            a = line.split(",")
            self.AddDomiciliarioNode(a[0], a[1])
        f.close()
    def addUserToFile(file, CE, Name):
        P = list.ULT
        f = open(file, "a")
        f.write("\n")
        f.write(CE + "," + Name + ',' + "0")
        f.close()
    def searchLess(self):
        min = self.PTR.Pedidos.__len__()
        P = self.PTR.Pedidos
        ChosenOne = P
        while P != None:
            if min < self.PTR.Pedidos.__len__():
                min = self.PTR.Pedidos.__len__()
                ChosenOne = self.PTR
        return ChosenOne

class Items(Nodo):
    """
    Clase Items heredada de Nodo, esta tiene guardados los datos de cada comida del menu
    """
    def __init__(self, number, data, price):
        super().__init__(data)
        self.number = number
        self.price = price

class Cart(Nodo):
    """
    Nodo de tipo Cart para guardar los items que escoja el usuario
    """
    def __init__(self, data, price):
        super().__init__(data)
        self.price = price

class LinkedListCart(LinkedList):
    """
    LinkedList para guardar los items que el usario tenga en su carrito mediante los nodos Cart
    """
    def AddNodeCart(self, data, price):
        P = Cart(data, price)
        if (self.PTR == None):
            self.PTR = P
            self.ULT = P 
        else:
            self.ULT.next = P
            self.ULT = P
    def __len__(self):
        P = self.PTR
        count = 0
        while P != None:
            count = count + 1
            P = P.next
        return count

class LinkedListMenu(LinkedList):

    def AddNodeItem(self, number, data, price):
        P = Items(number, data, price)
        if (self.PTR == None):
            self.PTR = P
            self.ULT = P 
        else:
            self.ULT.next = P
            self.ULT = P
    def fillMenu(self):
            f = open(r"Proyecto final\WhatsApp\MenuTerrasse.csv", "r")
            for line in f.readlines():
                a = line.split(",")
                self.AddNodeItem(a[0], a[1], a[2]) 
            f.close()
    #Mostrar menu
    def showMenu(self):
        P = self.PTR
        menu = ""
        while P!=None:
            menu = menu + P.number + ". " + P.data + " - " + P.price + "\n"
            P = P.next
        return menu    

Users = LinkedListUser()
Domicili = LinkedListDomiciliario()
Domicili.fillDomiciliarioList()
Users.fillUserList()
Users.AddUserNode("1-938198", "Carlos Del Toro", "10000")
Users.addUserToFile(r"Proyecto final\WhatsApp\users.csv","1-938198", "Carlos Del Toro")
Users.PTR.cart.AddNodeCart("Perro caliente", "5400")
Users.PTR.cart.AddNodeCart("Perro caliente", "5400")
Users.PTR.cart.AddNodeCart("Perro caliente", "5400")

item = Users.PTR.cart.PTR
a = 1
ped = ""
while a <= Users.PTR.cart.__len__():
    
    if a != Users.PTR.cart.__len__():
        ped = ped + item.data + ","
    else: 
        ped = ped  + item.data
    item = item.next
    a = a + 1

Domicili.PTR.Pedidos.AddPedidoNode(ped, Users.PTR.showCartTotal())

print(Domicili.PTR.Pedidos)