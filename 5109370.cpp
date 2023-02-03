#include <iostream>
using namespace std;
int main() {
    int n,m,k;
    cin >> n >> m >> k;
    int a[n+2][m+2];
    for (int i = 0; i < n+2; i++) {
        for (int j = 0; j < m+2; j++) {
            a[i][j] = 0;
        }
    }
    for (int i = 0; i < k; i++) {
        int x,y;
        cin >> x >> y;
        a[x][y] = 1;
    }
    int c = 0;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            int b = 0;
            for (int l = -1; l <= 1; l++) {
                for (int k = -1; k <= 1; k++) {
                    if (a[i+l][j+k] == 1 && !(l == 0 && k == 0)) b++;
                }
            }
            if (b >= 3) c++;
        }
    }
    cout << c << endl;
}