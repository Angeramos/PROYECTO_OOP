class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)

class Usuario(Nodo):
    def __init__(self, data, Name, Wallet): 
        super().__init__(data)
        self.Name = Name
        self.Wallet = Wallet

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
    
def fillUserList(list):
    f = open(r"PROYECTO_OOP\Proyecto final\WhatsApp\users.csv", "r")
    for line in f.readlines():
        a = line.split(",")
        print(a[0], a[1], a[2])
        list.AddUserNode(a[0], a[1], a[2]) 
    f.close()

def addUserToFile(file, data, Name, Wallet):
    f = open(file, "a")
    f.write("\n")
    f.write(data +","+ Name + "," + Wallet) 
    f.close()

def updtFile(file, search, newData):#, replace):
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


