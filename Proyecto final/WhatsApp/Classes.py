class Restaurant():
    def __init__(self, name):
        self.name = name
        self.Menu = {}
    def updtMenu(self, file, ext):
        f = open(file+ext, "r")
        for line in f.readlines():
            a =  line.split(",")
            self.Menu.update({a[0]:[a[1], a[2]]})
    def showMenu(self):
        texto = ""
        for x,y in self.Menu.items():
            texto = texto + "{}. {} {}\n".format(x, self.Menu[x][0], self.Menu[x][1])
        return texto
class UsersData():
    def __init__(self):
        self.usersDict = {}
    def addBalance(self, user, newBalance):
        if user in self.usersDict:
            oldBalance = self.usersDict.get(user)
            currentBalance = int(oldBalance) + int(newBalance)
            self.usersDict.update({user:str(currentBalance)})
            msg = "Su saldo es: {}\n".format(self.usersDict.get(user))
            
        else:
            msg = "El usuario no existe\n"
        return msg
            

    def checkBalance(self, user:str):
        if user in self.usersDict:
            msg = "Su saldo es: {}\n".format(self.usersDict.get(user))
        else:
            msg = "El usuario no existe\n"
        return msg 


Terrase = Restaurant("Terrase")
Terrase.updtMenu("MenuTerrasse", ".csv")


        