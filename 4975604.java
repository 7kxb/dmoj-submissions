import java.util.*;
class dog{
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int S = sc.nextInt();
        int M = sc.nextInt();
        int L = sc.nextInt();
        int hap = S*1+M*2+L*3;
        if (hap >= 10) {
            System.out.println("happy");
        }
        else {
            System.out.println("sad");
        }
    }
}