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
        """
        Muestra el valor total de los productos en el carrito
        """
        P = self.cart.PTR
        Total = 0
        while P != None:
            Total = Total + int(P.price)
            P = P.next
        return str(Total) 
    def getPedido(self):
        """
        Devuelve el todos los items en el pedido, en un solo str
        """
        item = self.cart.PTR
        a = 1
        ped = ""
        while a <= self.cart.__len__():
            if a != self.cart.__len__():
                ped = ped + item.data + ","
            else: 
                ped = ped  + item.data
            item = item.next
            a = a + 1
        return ped
    def payPedido(self):
        """
        Paga los productos que tenga el nodo usuario en cart, descontando de su wallet el valor total
        """
        if int(self.Wallet) >= int(self.showCartTotal()):
            self.Wallet = int(self.Wallet) - int(self.showCartTotal())
            LinkedListUser.updtFile(self.data, str(self.Wallet))
            print("Entro")
        else:
            pass

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
        """Añade un nodo de tipo usuario"""
        P = Usuario(data, Name, Wallet)
        if (self.PTR == None):
            self.PTR = P
            self.ULT = P
        else:
            self.ULT.next = P
            self.ULT = P
    def search(self, data):
        """Busca dentro de la lista enlazada"""
        try:
            P = self.PTR
            while (P.data != data) or P.data != None:
                if P.data == data:
                    return P
                P = P.next
        except AttributeError:
            return None
    def showBalance(self, data):
        """Muestra el valor que tiene la wallet del nodo usuario"""
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
        """Llena la lista enlazada"""
        f = open(r"Proyecto final\WhatsApp\src\Data\users.csv", "r")
        for line in f.readlines():
            a = line.split(",")
            self.AddUserNode(a[0], a[1], a[2])
        f.close()
    def addUserToFile(self, file, CE, Name):
        """Añade al final del archivo, aquellos usuarios recien creados"""
        P = self.ULT
        f = open(file, "a")
        f.write("\n")
        f.write(CE + "," + Name + ',' + "50000")
        f.close()
    def updtFile(search, newData):
        """Actualiza un valor en especifo del archivo"""
        f = open(r"Proyecto final\WhatsApp\src\Data\users.csv", "r")
        for line in f.readlines():
            a = line.split(",")
            if a[0] == search:
                print(a[0])
                break
        with open(r"Proyecto final\WhatsApp\src\Data\users.csv", "r") as f:
            data = f.read()
            data = data.replace(a[0]+","+a[1]+","+a[2], a[0]+","+a[1]+","+newData + "\n")
        with open(r"Proyecto final\WhatsApp\src\Data\users.csv", "w") as f:
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
    """Lista enlazada con nodos del tipo pedido"""
    def AddPedidoNode(self, data, total):
        """Añade a la lista enlazada nodos del tipo pedido"""
        P = Pedido(data, total)
        if (self.PTR == None):
            self.PTR = P
            self.ULT = P
        else:
            self.ULT.next = P
            self.ULT = P
    def __len__(self):
        """Regresa el tamaño de la lista enlazada"""
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

class LinkedListDomiciliario ( LinkedList):
    """Lista enlazada con nodos del tipo domiciliario"""
    def AddDomiciliarioNode(self, data, Name):
        """Añade nodos del tipo domiciliario a la lista enlazada"""
        P = Domiciliario(data, Name)
        if (self.PTR == None):
            self.PTR = P
            self.ULT = P
        else:
            self.ULT.next = P
            self.ULT = P
    def search(self, data):
        """Busca dentro de la lista enlazada"""
        P = self.PTR
        try:
            while P != None or P.data!= data:
                if P.data == data:
                    return P
                P = P.next
        except AttributeError:
            return None
    def fillDomiciliarioList(self):
        """Llena la lista enlazada"""
        f = open(r"Proyecto final\WhatsApp\src\Data\Domiciliarios.csv", "r")
        for line in f.readlines():
            a = line.split(",")
            self.AddDomiciliarioNode(a[0], a[1])
        f.close()
    def addUserToFile(file, CE, Name):
        """Añade al final del archivo, aquellos usuarios recien creados"""
        f = open(file, "a")
        f.write("\n")
        f.write(CE + "," + Name + ',' + "0")
        f.close()
    def searchLess(self):
        """Busca aquel domiciliario que tenga la menor cantidad de pedidos, esto para que asi se den pedidos por cantidad iguales"""
        min = self.PTR.Pedidos.__len__()
        P = self.PTR
        ChosenOne = P
        while P != None:
            if min < P.Pedidos.__len__():
                min = P.Pedidos.__len__()
                ChosenOne = P
            P = P.next
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
        """Añade nodos del tipo cart a la lista enlazada"""
        P = Cart(data, price)
        if (self.PTR == None):
            self.PTR = P
            self.ULT = P 
        else:
            self.ULT.next = P
            self.ULT = P
    def __len__(self):
        """devuelve el tamaño de la lista enlazada"""
        P = self.PTR
        count = 0
        while P != None:
            count = count + 1
            P = P.next
        return count

class LinkedListMenu(LinkedList):
    """Lista enlazada con nodos del tipo items"""
    def AddNodeItem(self, number, data, price):
        """Añade nodos del tipo item a la lista enlazada"""
        P = Items(number, data, price)
        if (self.PTR == None):
            self.PTR = P
            self.ULT = P 
        else:
            self.ULT.next = P
            self.ULT = P
    def fillMenu(self):
        """Llena la lista enlazada"""
        f = open(r"Proyecto final\WhatsApp\src\Data\MenuTerrasse.csv", "r")
        for line in f.readlines():
            a = line.split(",")
            self.AddNodeItem(a[0], a[1], a[2]) 
        f.close()
    def showMenu(self):
        """Muestra el contenido de todos los nodos pertenecientes a la lista enlazada"""
        P = self.PTR
        menu = ""
        while P!=None:
            menu = menu + P.number + ". " + P.data + " - " + P.price + "\n"
            P = P.next
        return menu    
    def search(self, data):
        """Busca dentro de la lista enlazada"""
        P = self.PTR
        try:
            while P != None:
                if P.number == data:
                    return P
                P = P.next
        except AttributeError:
            return None

