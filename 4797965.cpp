#include <iostream>
#include <vector>
using namespace std;
int main() {
    int n, m, k;
    cin >> n >> m >> k;
    int a[n][m] = {};
    int b = 0;
    for (int i = 0; i < k; i++) {
        char c;
        int d;
        cin >> c >> d;
        if (c == 'R') {
            for (int j = 0; j < m; j++) {
                a[d-1][j] += 1;
                if (a[d-1][j]%2 == 0) {
                    b -= 1;
                }
                else {
                    b += 1;
                }
            }
        }
        if (c == 'C') {
            for (int k = 0; k < m; k++) {
                a[k][d-1] += 1;
                if (a[k][d-1]%2 == 0) {
                    b -= 1;
                }
                else {
                    b += 1;
                }
            }
        }
    }
    cout << b << endl;
}