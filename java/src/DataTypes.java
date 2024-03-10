public class DataTypes {
    public static void main(String[] args) {
        // Primitive Data Types
        int num = 10;            // integer data type
        double decimal = 3.14;   // floating-point data type
        char letter = 'A';       // character data type
        boolean flag = true;     // boolean data type

        // Reference Data Types
        String name = "Abc";    // string data type
        int[] array = {1, 2, 3}; // array data type

        // Output
        System.out.println("Primitive Data Types:");
        System.out.println("Integer: " + num);
        System.out.println("Double: " + decimal);
        System.out.println("Character: " + letter);
        System.out.println("Boolean: " + flag);

        System.out.println("\nReference Data Types:");
        System.out.println("String: " + name);
        System.out.print("Array: ");
        for (int i : array) {
            System.out.print(i + " ");
        }
        System.out.println();
    }
}
