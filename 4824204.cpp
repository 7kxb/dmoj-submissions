#include <iostream>
using namespace std;
int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        string a;
        cin >> a;
        string x = a;
        while (a.length() != 2) {
            int b = a[-1];
            a.pop_back();
            int c = stoi(a);
            string a = to_string(c-b);
        }
        if (stoi(a)/11 == 1) {
            cout << "The number " << x << "is divisible by 11.";
        }
        else {
            cout << "The number " << x << "is not divisible by 11.";
        }
    }
}