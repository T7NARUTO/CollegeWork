import java.util.Scanner;
public class Java2 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("""
                1.Area of Circle
                2.Area of Triangle
                3.Area of Rectangle
                4.Area of Square
                5.Area of Semicircle
                6.Area of Sphere
                7.Area of Cylinder
                """);
        int ch = sc.nextInt();
        switch (ch){
            case 1:
                System.out.println("Enter the radius of the circle");
                double radius = sc.nextDouble();
                double area = 3.14159265359 * radius * radius;
                System.out.println("Area of circle = "+ area);
                break;
            case 2:
                System.out.println("Enter the base of the Triangle");
                double base = sc.nextDouble();
                System.out.println("Enter the height of the Triangle");
                double height = sc.nextDouble();
                area = (base * height) / 2;
                System.out.println("Area of triangle = "+ area);
                break;
            case 3:
                System.out.println("Enter the length of the Rectangle");
                base = sc.nextDouble();
                System.out.println("Enter the width of the Rectangle");
                double width = sc.nextDouble();
                area = base * width;
                System.out.println("Area of Rectangle = " + area);
                break;
            case 4:
                System.out.println("Enter the side  of the Square");
                double side = sc.nextDouble();
                area = side * side;
                System.out.println("Area of Rectangle = " + area);
                break;
            case 5:
                System.out.println("Enter the radius of the Semicircle");
                radius = sc.nextDouble();
                area = (3.14159265359*radius*radius)/2;
                System.out.println("Area of Rectangle = " + area);
                break;
            case 6:
                System.out.println("Enter the radius of the Sphere");
                radius = sc.nextDouble();
                area = (4*3.14159265359*radius*radius)/2;
                System.out.println("Area of Rectangle = " + area);
                break;
            case 7:
                System.out.println("Enter the radius of the Cylinder");
                radius = sc.nextDouble();
                System.out.println("Enter the height of the Cylinder");
                height = sc.nextDouble();
                area = 2*3.14159265359*radius*(radius+height);
                System.out.println("Area of Rectangle = " + area);
                break;
            default:
                break;
        }
    }
}
