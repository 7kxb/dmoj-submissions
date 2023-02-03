#include <iostream>
#include <vector>
using namespace std;
int main() {
    int n;
    cin >> n;
    vector <int> a;
    int x;
    for (int i = 0; i < n*2; i++) {
        cin >> x;
        a.push_back(x);
    }
    int e = 0;
    for (int i = 0; i < n; i++) {
        vector <int> b;
        for (int x = i; x < n+i; x++) {
            b.push_back(a[x]);
        }
        vector <int> c;
        for (int y = n+i; y < 2*n+1; y++) {
            c.push_back(a[y]);
        }
        for (int z = 0; z < i; z++) {
            c.push_back(a[z]);
        }
        int d = 0;
        for (int j = 0; j < n; j++) {
            if (b[j] == c[j]) {
                d += 1;
            }
        }
        if (d > e) {
            e = d;
        }
    }
    cout << e << endl;
}