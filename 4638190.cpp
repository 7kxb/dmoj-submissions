#include <iostream>
using namespace std;
int main() {
    int n;
    cin >> n;
    int c;
    cin >> c;
    string x;
    for (int i = 0; i < n; i++) {
        int h;
        cin >> h;
        h += c * 2;
        x += to_string(h) + ' ';
    }
    cout << x << endl;
}