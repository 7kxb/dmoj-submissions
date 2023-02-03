#include <iostream>
#include <stdio.h>
#include <bits/stdc++.h>
using namespace std;
void primeInRange(int L, int U)
{
    int i, j, flag;
    int counter = 0;
    for (i = L; i <= U; i++) {
        if (i == 1 || i == 0)
            continue;
        flag = 1;
        for (j = 2; j <= i / 2; ++j) {
            if (i % j == 0) {
                flag = 0;
                break;
            }
        }
        if (flag == 1) {
            string S = to_string(i);
            string P = to_string(i);
            reverse(P.begin(), P.end());
            if (S == P) {
                counter += 1;
            }
        }
    }
    cout << counter << endl;
}
int main()
{
    int L;
    int U;
    for (int i = 1; i <= 5; i++) {
        cin >> L >> U;
        primeInRange(L, U);
    }
}