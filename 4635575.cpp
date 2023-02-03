#include <iostream>
using namespace std;
int main() {
    int S, M, L;
    cin >> S >> M >> L;
    int hap;
    hap = S*1+M*2+L*3;
    if (hap >= 10) {
        cout << "happy" << endl;
    }
    else {
        cout << "sad" << endl;
    }
}