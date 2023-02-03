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
            cout << i << endl;
        }
    }
}
int main()
{
    int L;
    int U;
    cin >> L >> U;
    primeInRange(L, U);
}