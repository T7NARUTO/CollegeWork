import java.util.Scanner;

public class Array2{
    static void IsPrime(int[] array) {
        for (int i : array) {
            boolean isPrime = true;
            if (i < 2) {
                isPrime = false;
            } else {
                for (int j = 2; j * j <= i; j++) {
                    if (i % j == 0) {
                        isPrime = false;
                        break;
                    }
                }
            }
            if (isPrime) {
                System.out.println(i + " is a prime number.");
            } else {
                System.out.println(i + " is not a prime number.");
            }
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the limit of the array");
        int limit = sc.nextInt();
        int[] array = new int[limit];
        for(int i=0;i<limit;i++) {
            System.out.println("Enter the "+i+" Element of the array");
            int el = sc.nextInt();
            array[i] = el;
        };
        IsPrime(array);
    }
}
