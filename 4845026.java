// kenship's code, just submitted for them because they are locked out of dmoj and password reset is slow, dw i already solved this myself

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Stack;
class Combo implements Cloneable{
    Stack<Integer> coins = new Stack<>();
    int total;

    public Object clone() throws CloneNotSupportedException{
        return super.clone();
    }
}
public class Main {
    public static void main(String[] args) throws IOException, CloneNotSupportedException {
        int total = readInt();
        int count = readInt();
        int[] values = getCoins(count);
        Arrays.sort(values);

        Stack<int[]> history = new Stack<>();
        //initialize history
        int[] root = new int[3];

        history.push(root);
        ArrayList<int[]> results = new ArrayList<>();
        //loop index or number of coins


        while(true){
            if(history.isEmpty())
                break;
            int[] current = history.pop();
            if(current[0] == total) {
                results.add(current);
                continue;
            }




            history.addAll(newComb(current,values,total));

        }
        //output amount of coins aka i
        output(results);

    }

    private static void output(ArrayList<int[]> results) {
        int min = 99999999;
        for (int[] i: results) {

            if (i[2] < min)
                min = i[2];

        }
        System.out.println(min);
    }

    private static Stack<int[]> newComb(int[] input, int[] values,int max) throws CloneNotSupportedException {
        Stack<int[]> local = new Stack<>();
        for(int i = 0; i < values.length; i++){
            int[] current = input.clone();

            int curValue = values[i];
            if(current[2] == 0){
                //total value
                current[0] = curValue;
                //previous value
                current[1] = curValue;
                //# of coins
                current[2]++;
                if(current[1] <= max)
                    local.push(current);
                continue;
            }
            int previous = current[1];
            if(curValue > previous){
                continue;
            }
            current[0] += curValue;
            current[1] = curValue;
            current[2]++;
            if(current[0] >max)
                continue;
            local.push(current);
        }
        return local;
    }

    private static int[] getCoins(int count) throws IOException {
        int[] coins = new int[count];
        for(int i = 0; i < count; i ++){
            coins[i] = readInt();
        }
        return coins;
    }
    private static int readInt() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        return Integer.parseInt(br.readLine());
    }
}