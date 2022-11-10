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
        for x in self.Menu.items():
            texto = texto + "{}. {} {}\n".format(x, self.Menu[x][0], self.Menu[x][1])
        return texto


class UsersData():
    def __init__(self):
        self.usersDict = {}
    def addBalance(self, user, code):
        if user in self.usersDict:
            oldBalance = self.usersDict.get(user)
            if (Codes.useCode(code)[0]):
                currentBalance = int(oldBalance) + int(Codes.useCode(code)[1])
                self.usersDict.update({user:str(currentBalance)})
                msg = "Su saldo es: {}\n".format(self.usersDict.get(user))
            else:
                msg = "El codigo no es valido"
        else:
            msg = "El usuario no existe\n"
        return msg

    def checkBalance(self, user:str):
        if user in self.usersDict:
            msg = "Su saldo es: {}\n".format(self.usersDict.get(user))
        else:
            msg = "El usuario no existe\n"
        return msg 

class Codes:
    def __init__(self):
        self.usedCodes = []
    def useCode(self, code):
        codeDigits = []
        verif = False
        codeDigits.extend(code) 
        codeValue = 0
        if codeDigits[0] == "1" and len(codeDigits) == 6:
            codeValue = "10000"
            verif = True
            self.usedCodes.append(code)
        elif codeDigits[0] == "2" and len(codeDigits) == 6:
            codeValue = "20000"
            verif = True
            self.usedCodes.append(code)
        elif codeDigits[0] == "5" and len(codeDigits) == 6:
            codeValue = "50000"
            verif = True
            self.usedCodes.append(code)
        else: 
            codeValue = "Codigo no valido"
        return verif,codeValue    
        
Terrase = Restaurant("Terrase")
Terrase.updtMenu("MenuTerrasse", ".csv")


        