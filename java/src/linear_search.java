import java.util.Scanner;
public class linear_search {
    static void Linear_search(int[]array,int value){
        int len = array.length;
        int i = 0;
        while(i < len){
            if (array[i] == value) {
                System.out.println("found" + value + "at" + i);
                return;
            }
            i += 1;
        }
        System.out.println("value not found ");
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the limit of the array");
        int n = sc.nextInt();
        int[] array = new int[n];
        for(int i = 0; i < n; i++){
            System.out.println("Enter the "+i+" Element of the array");
            int el = sc.nextInt();
            array[i] = el;
        }
        System.out.println("Enter the value to search");
        int value = sc.nextInt();
        Linear_search(array,value);
    }
}
