package PooUber.Java;

class Main{
    public static void main(String[] args) {
        System.out.println("Hola mundo");
        Car car = new Car("AMQ123", new Account("Andres Herrera", "INE AND123"));
        car.passenger = 4;
        car.printDataCar();

        Car car2 = new Car("QWE567", new Account("Andrea Herrera", "INE AND456"));
        car2.passenger = 3;
        car2.printDataCar();

    }
}
