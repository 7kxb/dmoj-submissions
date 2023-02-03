#include <iostream>
#include <bits/stdc++.h>
using namespace std;
int main() {
    int n, a, b, c;
    int sum = 0;
    cin >> n >> a >> b >> c;
    while (n > 0) {
        n -= 1;
        if (n >= 0) {
            a += 1;
            if (a % 35 == 0) {
                n += 30;
            }
            sum += 1;
        }
        n -= 1;
        if (n >= 0) {
            b += 1;
            if (b % 100 == 0) {
                n += 60;
            }
            sum += 1;
        }
        n -= 1;
        if (n >= 0) {
            c += 1;
            if (c % 10 == 0) {
                n += 9;
            }
            sum += 1;
        }
    }
    cout << "Martha plays " << sum << " times before going broke." << endl;
}