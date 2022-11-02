from dataclasses import dataclass
@dataclass
class Motor():
    cylinders:int
    @classmethod
    def ignite():
        return "Engine started"

class Car(Motor):
    def __init__(self,brand,color,model):
        self.brand = brand
        self.color = color 
        self.model = model
        super().__init__(self,cylinders)
        self.cylinders = cylinders
    def startMotor(self):
        print(Motor.ignite)
    def antal_cylindrar(self):
        output = f"{self.brand} har {self.cylinders} cylindrar"
        return output

Tesla = Car(brand = "Tesla",cylinders=4,color = "röd",model="S400")

print(Tesla.antal_cylindrar())