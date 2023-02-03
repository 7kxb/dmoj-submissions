#include <iostream>
using namespace std;
int main() {
    char a, b, c, d;
    cin >> a >> b >> c >> d;
    int x = (int)a - 48;
    int y = (int)c - 48;
    int z = (int)d - 48;
    int e = x*60 + y*10 + z;
    cout << e << endl;
}