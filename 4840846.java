import java.util.Scanner;
import java.util.Arrays;
public class Main {
    public static void main(String[] args) {
        Scanner myObj = new Scanner(System.in);
        int a = myObj.nextInt();
        int b = myObj.nextInt();
        int c = myObj.nextInt();
        int arr[] = {a,b,c};
        Arrays.sort(arr);
        System.out.println(arr[1]);
    }
}