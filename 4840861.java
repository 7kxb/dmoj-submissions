import java.util.Scanner;
import java.util.Arrays;
public class Main {
    public static void main(String[] args) {
        Scanner myObj = new Scanner(System.in);
        int a = myObj.nextInt();
        int b = myObj.nextInt();
        int c = myObj.nextInt();
        if (a == 60 && b == 60 && c == 60) {
            System.out.println("Equilateral");
        }
        else if (a+b+c == 180 && (a == b || b == c || a == c)) {
            System.out.println("Isosceles");
        }
        else if (a+b+c == 180) {
            System.out.println("Scalene");
        }
        else {
            System.out.println("Error");
        }
    }
}