public class VariableDemo {
    // Instance variables
    int instanceVar;  // Example of an instance variable

    // Static variables
    static int staticVar;  // Example of a static variable

    public static void main(String[] args) {
        // Local variables
        int localVar = 10;  // Example of a local variable
        System.out.println("Local Variable: " + localVar);

        // Creating an object of VariableDemo class to access instance variables
        VariableDemo obj = new VariableDemo();
        obj.instanceVar = 20;  // Assigning a value to instance variable
        System.out.println("Instance Variable: " + obj.instanceVar);

        // Accessing static variable
        VariableDemo.staticVar = 30;  // Assigning a value to static variable
        System.out.println("Static Variable: " + VariableDemo.staticVar);

        // Constants (Final Variables)
        final int MAX_VALUE = 100;  // Example of an instance constant
        System.out.println("Instance Constant: " + MAX_VALUE);

        final double PI = 3.14;  // Example of a static constant
        System.out.println("Static Constant: " + PI);
    }
}
