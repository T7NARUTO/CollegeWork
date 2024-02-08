import  java.util.Scanner;
public class Java4 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a Number");
        int i = sc.nextInt();
        if (i == 0){
            System.out.println("given number is zero");
        }
        else if(i >= 1){
            System.out.println("given number is greater than zero");
        }
        else{
            System.out.println("given number is less than zero");
        }
    }
}
