import java.util.Scanner;
public class Array1{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the limit of the Array");
        int limit = sc.nextInt();
        int[] array = new int[limit];
        for (int i = 0;i<limit;i++){
            System.out.println("Enter the " +i +" Element");
            int element = sc.nextInt();
            array[i] = element;
        }
        int sum = 0;
        for(int i: array){
            sum += i;
        }
        float average = (float) sum /limit;
        System.out.println("Sum:-"+ sum);
        System.out.println("Average:-" + average);
        sc.close();
    }
}
