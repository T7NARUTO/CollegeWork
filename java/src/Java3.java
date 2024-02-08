import java.util.Scanner;
public class Java3 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number");
        int i = sc.nextInt();
        int rem = i % 2;
        if (rem == 0) {
            System.out.println("Given number is even");
        }
        else {
            System.out.println("Given number is odd");
        }
    }
}
