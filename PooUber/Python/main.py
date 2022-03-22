from car import Car
from account import Account
from payment import Payment
from paypal import paypal

if __name__ == "__main__": #El metodo de condicion de enrada de la aplicacion
    print("Hola mundo")

    car = Car("AMS234", Account("Andres Herrera", "INE ANDA876"))
    print(vars(car))
    print(vars(car.driver))

    car2 = Car("K98AZW", Account("Javier Gonzalez", "INE javs"))
    print(vars(car2))
    print(vars(car2.driver))

    payment1 = paypal(1234, "javivisega@gmail.com")
    print(vars(payment1))
