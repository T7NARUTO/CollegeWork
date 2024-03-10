import java.util.Scanner;
class doWhile{
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int num;
        // Prompt the user to enter a number
        System.out.println("Enter a number: ");
        // Read the number entered by the user
        num = scanner.nextInt();
        // Initialize sum variable
        int sum = 0;
        // Perform the loop at least once to calculate the sum of digits
        do {
            // Get the last digit of the number
            int digit = num % 10;
            // Add the digit to the sum
            sum += digit;
            // Remove the last digit from the number
            num /= 10;
        } while (num != 0); // Continue looping until num becomes 0
        // Display the sum of digits
        System.out.println("Sum of digits: " + sum);
        scanner.close();
    }
}
