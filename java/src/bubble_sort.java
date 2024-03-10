import java.util.Arrays;
import java.util.Scanner;
public class bubble_sort{
    static void BubbleSort(int[] array){
        int len = array.length;
        while(len > 0){
            int i = 0;
            while(i < len -1){
                if (array[i] > array[i+1]){
                    int temp = array[i];
                    array[i] = array[i+1];
                    array[i+1] = temp;
                }
                i += 1;
            }
            len -= 1;
        }
    }

    public static void main (String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the limit of the array");
        int n = sc.nextInt();
        int[] array = new int[n];
        for(int i = 0; i < n; i++){
            System.out.println("Enter the "+i+" Element of the array");
            int el = sc.nextInt();
            array[i] = el;
        }
        System.out.println("Unsorted array :- "+(Arrays.toString(array)));
        BubbleSort(array);
        System.out.println("Sorted array :- "+(Arrays.toString(array)));
    }
}
