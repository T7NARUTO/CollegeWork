import java.util.Scanner;

public class Array3 {
    static void EvenOdd(int[] array){
        for(int i:array){
            if(i%2 == 0){
                System.out.println(i+ " is even");
            }
            else{
                System.out.println(i+ " is odd");
            }
        }
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the limit of the array");
        int limit = sc.nextInt();
        int[] array = new int[limit];
        for (int i=0; i<limit; i++){
            System.out.println("Enter the "+i+"th element");
            int element = sc.nextInt();
            array[i] = element;
        }
        EvenOdd(array);
    }
}
