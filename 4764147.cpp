#include <iostream>
using namespace std;
int main() {
    int n;
    cin >> n;
    string a;
    cin >> a;
    string b = "";
    for (int i = 1; i < n+1; i++) {
        b += to_string(i) + " ";
    }
    cout << b << endl;
}