import java.util.Scanner;
public class Main {
    public static void main(String[] args){
        Scanner sc  = new Scanner(System.in);
        System.out.println("Enter a number ");
        int a = sc.nextInt();
        System.out.println("Enter another number ");
        int b = sc.nextInt();
        int sum = a + b;
        int difference = a - b;
        int product = a * b;
        int remainder = a % b;
        int quotient = a / b;
        System.out.println("sum  =" + sum );
        System.out.println("remainder =" + remainder);
        System.out.println("product =" + product);
        System.out.println("difference =" + difference);
        System.out.println("quotient =" + quotient);
    }
}