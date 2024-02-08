import java.util.Scanner;
public class Java1 {
    public static void main(String[] args){
        Scanner sc  = new Scanner(System.in);
        System.out.println("""
                1.Addition
                2.Subtraction
                3.Multiplication
                4.Division
                5.Modulus
                6.Exit""");
        int ch = sc.nextInt();
        switch (ch) {
            case 1:
                System.out.println("Enter First number");
                int a  = sc.nextInt();
                System.out.println("Enter Second number");
                int b = sc.nextInt();
                int sum = a + b;
                System.out.println("sum = " + sum);
                break;
            case 2:
                System.out.println("Enter First number");
                a  = sc.nextInt();
                System.out.println("Enter Second number");
                b = sc.nextInt();
                int diff = a - b;
                System.out.println("Difference = " + diff);
                break;
            case 3:
                System.out.println("Enter First number");
                a  = sc.nextInt();
                System.out.println("Enter Second number");
                b = sc.nextInt();
                int mul = a * b;
                System.out.println("Product =" + mul);
                break;
            case 4:
                System.out.println("Enter First number");
                a  = sc.nextInt();
                System.out.println("Enter Second number");
                b = sc.nextInt();
                int div = a / b;
                System.out.println("Quotient = " + div);
                break;
            case 5:
                System.out.println("Enter First number");
                a  = sc.nextInt();
                System.out.println("Enter Second number");
                b = sc.nextInt();
                int mod = a % b;
                System.out.println("Difference = " + mod);
                break;
            case 6:
                System.out.println("You have selected Exit option");
                break;
            default:
                System.out.println("invalid option");
        }
    }
}