from car import Car

if __name__ == "__main__": #El m[etodo de condicion de enrada de la aplicacion
    print("Hola mundo")
    car = Car()
    car.license = "AMS234"
    car.driver = "Andres Herrera"
    print(vars(car))

    car2 = Car()
    car2.license = "K98AZW"
    car2.driver = "Javier Gonzalez"
    print(vars(car2))