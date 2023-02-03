#include <bits/stdc++.h>
#include <iostream>
using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);   
    int n, a, b;
    cin >> n;
    for (int i = 1; i <= n; i++) {
        cin >> a >> b;
        if (i == 1 or i == 2 or i == 6 or i == 20 or i == 70 or i == 252 or i == 924 or i == 3432 or i == 12870 or i == 48620 or i == 184756 or i == 705432) {
            cout << a-b << "\n";
        }
        else {
            cout << a+b << "\n";
        }
    }
}