import java.util.Arrays;

public class bubble_sort{
    public static void main (String[] args){
        int[]arr = new int[5];
        arr[0] = 10;
        arr[1] = 2;
        arr[2] = 6;
        arr[3] = 20;
        arr[4] = 1;
        int len = arr.length;
        while(len > 0){
            int i = 0;
            while(i < len -1){
                if (arr[i] > arr[i+1]){
                   int temp = arr[i];
                   arr[i] = arr[i+1];
                   arr[i+1] = temp;
                }
                i += 1;
            }
            len -= 1;
        }
        System.out.println(Arrays.toString(arr));
    }
}
