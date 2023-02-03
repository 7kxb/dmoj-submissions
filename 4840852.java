import java.util.Scanner;
import java.util.Arrays;
public class Main {
    public static void main(String[] args) {
        Scanner myObj = new Scanner(System.in);
        int c = myObj.nextInt();
        for (int i = 0; i < c; i++) {
            int a = myObj.nextInt();
            int b = myObj.nextInt();
            System.out.println(a+b);
        }
    }
}