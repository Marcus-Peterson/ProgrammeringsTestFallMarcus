#3 klasser
#Fisk superklass
#Gädda ärver från Fisk
#Aborre ärver från Fisk
#Fisk ska ha attributet simhastighet som sätts i konstruktorn
#Andra fiskar ska också skapas med simhastighet som argument


class Fisk:
    def __init__(self,simhastighet):
        self.simhastighet = simhastighet
    def __str__(self):
        return (f"{self.simhastighet}")

class Gädda(Fisk):
    def __init__(self, simhastighet):
        super().__init__(simhastighet)
    def __str__(self):
        return (f"{self.simhastighet}")

class Aborre(Fisk):
    def __init__(self, simhastighet):
        super().__init__(simhastighet)

    def __str__(self):
        return (f"{self.simhastighet}")

Fisk1 = Fisk(12)
Fisk2 = Gädda(13)
Fisk3 = Aborre(14)

print(str(Fisk1),str(Fisk2),str(Fisk3))