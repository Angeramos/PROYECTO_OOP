class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.cart = LinkedListCart()
    def __repr__(self):
        return str(self.data)

class Usuario(Nodo):
    def __init__(self, data, Name, Wallet):
        super().__init__(data)
        self.Name = Name
        self.Wallet = Wallet
        self.cart = LinkedListCart()
    def showCartTotal(self):
        P = self.cart.PTR
        Total = 0
        while P != None:
            Total = Total + int(P.price)
            P = P.next
        return Total    

class LinkedList:
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
        while P.data != data:
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
    def addUserToFile(file, list):
        P = list.ULT
        f = open(file, "a")
        f.write("\n")
        f.write(P.data + "," + P.Name + ',' + P.Wallet)
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

#abra cadabra para crear el domicilio 
#TODO

class pedido(Nodo):
    def __init__(self, data):
        super().__init__(data)

class LinkedListDomicilio (LinkedList):
    def __init__(self, name, ce):
        super().__init__()
        self.name = name
        self.ce = ce 
        #self.domicilio = Domicilio()
        self.domicilio = LinkedListDomicilio
        P = pedido ()
        if (self.PTR == None):
            self.PTR = P
            self.ULT = P
        else:
            self.ULT.next = P
            self.ULT = P
#--------------------------

class Items(Nodo):
    def __init__(self, number, data, price):
        super().__init__(data)
        self.number = number
        self.price = price

class Cart(Nodo):
    def __init__(self, data, price):
        super().__init__(data)
        self.price = price

class LinkedListCart(LinkedList):
    def AddNodeCart(self, data, price):
        P = Cart(data, price)
        if (self.PTR == None):
            self.PTR = P
            self.ULT = P 
        else:
            self.ULT.next = P
            self.ULT = P

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

a = LinkedListUser()
Terrase = LinkedListMenu()
Terrase.fillMenu()
a.fillUserList()
a.PTR.cart.AddNodeCart(Terrase.PTR.data, Terrase.PTR.price)

a.PTR.Wallet = int(a.PTR.Wallet) - int(a.PTR.showCartTotal())

print(a.PTR.cart)
print(a.PTR.Wallet)