import java.util.Arrays;
import java.util.Scanner;

public class selectionSort {
    static void Selection_Sort(int[] array) {
        int len = array.length;
        for (int i = 0; i < len - 1; i++) {
            int minIndex = i;
            for (int j = i + 1; j < len; j++) {
                if (array[j] < array[minIndex]) {
                    minIndex = j;
                }
            }
            int temp = array[minIndex];
            array[minIndex] = array[i];
            array[i] = temp;
        }
    }
    public static void main(String[] args) {
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
        Selection_Sort(array);
        System.out.println("Sorted array :- "+(Arrays.toString(array)));
    }
}
