#include <iostream>
#include <bits/stdc++.h>
using namespace std;
int main() {
    int num;
    cin >> num;
    if (num >= 1 and num <= 2) {
        cout << num << endl;
    }
    if (num >= 3 and num <= 5) {
        cout << num-1 << endl;
    }
    if (num == 6) {
        cout << num/2 << endl;
    }
    if (num >= 7 and num <= 8) {
        cout << 2 << endl;
    }
    if (num >= 9 and num <= 10) {
        cout << 1 << endl;
    }
}