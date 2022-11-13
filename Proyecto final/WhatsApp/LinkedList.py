class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.PTR = None
        self.ULT = None

    def AddNode(self,data):
        P = Nodo(data)
        if (self.PTR == None):
            self.PTR = P
            self.ULT = P 
        else:
            self.ULT.next = P
            self.ULT = P             

    def Recorrido(self):
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
    def AddUserNode(self, data, Name, Wallet):
        P = Usuario(data, Name, Wallet)
        if (self.PTR == None):
            self.PTR = P
            self.ULT = P 
        else:
            self.ULT.next = P
            self.ULT = P  

class Cart(Nodo):
    def _init_(self, data, price):
        super()._init_(data)
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

class Usuario(Nodo):
    def _init_(self, data, Name, Wallet): 
        super()._init_(data)
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