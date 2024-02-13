public class linear_search {
    public static void main(String[] args){
        int[] arr = new int[5];
        arr[0] = 10;
        arr[1] = 20;
        arr[2] = 30;
        arr[3] = 40;
        arr[4] = 50;
        int len = arr.length;
        int i = 0;
        int value = 1;
        int flag = 0;
        while(i < len){
            if (arr[i] == value) {
                flag = 1;
                break;
            }
            i += 1;
        }
        if (flag == 1){
            System.out.println("value present in array");
        }
        else{
            System.out.println("value not present in array");
        }
    }
}
