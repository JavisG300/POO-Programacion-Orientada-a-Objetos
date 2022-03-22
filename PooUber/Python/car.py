from account import Account #Como se cambia el tipo de dato en driver debemos importar la clase

class Car:
    id        = int
    license   = str
    driver    = Account("","") #Cambiamos el tipo de dato a Account
    passenger = int

    def __init__(self, license, driver):
        self.license    = license
        self.driver     = driver