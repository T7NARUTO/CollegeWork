import java.util.Scanner;
public class binarySearch {
    static void Binary_Search(int[]array,int value){
        int low = 0;
        int high = array.length;
        while (low <= high){
            int mid = (low + high)/2;
            if (array[mid] == value){
                System.out.println("Element found at " + mid);
                return;
            }
            else if (array[mid] > value){
                high = mid-1;
            }
            else{
                low = mid+1;
            }
        }
        System.out.println("Element not found");
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the limit of the sorted array");
        int n = sc.nextInt();
        int[] array = new int[n];
        for(int i = 0; i < n; i++){
            System.out.println("Enter the "+i+" Element of the array");
            int el = sc.nextInt();
            array[i] = el;
        }
        System.out.println("Enter the value to search");
        int value = sc.nextInt();
        Binary_Search(array,value);
    }
}
