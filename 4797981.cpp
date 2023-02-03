#include <iostream>
#include <vector>
using namespace std;
int main() {
    int n, m;
    cin >> n >> m;
    int a[n][n] = {};
    int b = 0;
    for (int i = 0; i < m; i++) {
        int x, y, w, h;
        cin >> x >> y >> w >> h;
        for (int j = 0; j < w; j++) {
            for (int k = 0; k < h; k++) {
                a[x+j][y+k] += 1;
                if (a[x+j][y+k]%2 == 0) {
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