import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner myObj = new Scanner(System.in);
        int n = myObj.nextInt();
        System.out.println("#include <iostream>");
        System.out.println("using namespace std;");
        System.out.println("int main(){");
        System.out.println("    cout << "+(n*n+n)/2+" << endl;");
        System.out.println("}");
    }
}