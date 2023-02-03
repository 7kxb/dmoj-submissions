#include <iostream>
using namespace std;
int main() {
    int n;
    cin >> n;
    for (int _ = 0; _ < n; _++) {
        string a;
        cin >> a;
        bool b = true;
        for (int i = 0; i < a.length(); i++) {
            if (a[i] == 'k' || a[i] == 'n' || a[i] == 'm' || a[i] == 'r') {
                if (i+1 != a.length()) {
                    if (a[i+1] != 'a' && a[i+1] != 'e' && a[i+1] != 'i' && a[i+1] != 'o' && a[i+1] != 'u') {
                        b = false;
                    }
                }
                else {
                    b = false;
                }
            }
            else if (a[i] == 'h') {
                if (i+1 != a.length()) {
                    if (a[i+1] != 'a' && a[i+1] != 'e' && a[i+1] != 'i' && a[i+1] != 'o') {
                        b = false;
                    }
                }
                else {
                    b = false;
                }
            }
            else if (a[i] == 'f') {
                if (i+1 != a.length()) {
                    if (a[i+1] != 'u') {
                        b = false;
                    }
                }
                else {
                    b = false;
                }
            }
            else if (a[i] != 'a' && a[i] != 'e' && a[i] != 'i' && a[i] != 'o' && a[i] != 'u') {
                b = false;
            }
        }
        if (b = true) {
            cout << "YES" << endl;
        }
        else {
            cout << "NO" << endl;
        }
    }
}