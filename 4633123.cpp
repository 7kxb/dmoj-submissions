#include <iostream>
#include <bits/stdc++.h>
using namespace std;
int main() {
    int spaces;
    cin >> spaces;
    string one;
    cin >> one;
    string two;
    cin >> two;
    int counter = 0;
    for (int i = 0; i < spaces; i++) {
        if (one[i] == 'C' && two[i] == 'C') {
            counter += 1;
        }
    }
    cout << counter << endl;
}