import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner myObj = new Scanner(System.in);
        int n = myObj.nextInt();
        System.out.println("#include <iostream>");
        System.out.println("int main(){");
        System.out.println("    printf(\""+((n*n+n)/2)+"\");");
        System.out.println("}");
    }
}