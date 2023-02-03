import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner myObj = new Scanner(System.in);
        long n = myObj.nextLong();
        System.out.println("#include <iostream>");
        System.out.println("using namespace std;");
        System.out.println("int main(){");
        System.out.println("    cout << \""+((n*(n+1))/2)+"\";");
        System.out.println("}");
    }
}