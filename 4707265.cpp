#include <iostream>
#include <math.h>
using namespace std;
bool isPrime(long long n) {
    if (n <= 1 || (n % 2 == 0 && n != 2)) {
        return false;
    }
    for (int i = 3; i < pow(0.5, n) + 1; i+2) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}
int main() {
    int t;
    long long n;
    cin >> t;
    for (int i = 0; i < t; i++) {
        cin >> n;
        bool b = isPrime(n);
        if (b == true) {
            cout << "PRIME" << endl;
        }
        else {
            cout << "NOT" << endl;
        }
    }
}