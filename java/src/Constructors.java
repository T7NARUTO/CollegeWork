class Car {
    String brand;
    String model;
    int year;

    // Default Constructor
    Car() {
        brand = "Toyota";
        model = "Corolla";
        year = 2020;
    }

    // Parameterized Constructor
    Car(String b, String m, int y) {
        brand = b;
        model = m;
        year = y;
    }

    // Copy Constructor
    Car(Car originalCar) {
        brand = originalCar.brand;
        model = originalCar.model;
        year = originalCar.year;
    }

    // Method to display car information
    void displayInfo() {
        System.out.println("Brand: " + brand);
        System.out.println("Model: " + model);
        System.out.println("Year: " + year);
    }
}

public class Constructors{
    public static void main(String[] args) {
        // Creating objects using different constructors
        Car car1 = new Car(); // Default Constructor
        Car car2 = new Car("Ford", "Mustang", 2019); // Parameterized Constructor
        Car car3 = new Car(car2); // Copy Constructor

        // Displaying information of each car
        System.out.println("Car 1:");
        car1.displayInfo();

        System.out.println("\nCar 2:");
        car2.displayInfo();

        System.out.println("\nCar 3 (Copy of Car 2):");
        car3.displayInfo();
    }
}
