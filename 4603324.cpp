#include <iostream>
#include <vector>
using namespace std;
int main() {
    int m, n, k;
    vector<vector <int>> row(m);
    for (int i = 0; i < m; i++) {
        vector<int> col(n);
        for (int j = 0; j < n; j++) {
            col.push_back(-1);
        }
        row.push_back(col);
    }
    for (int i = 0; i < k; i++) {
        char temp1;
        int temp2;
        cin >> temp1 >> temp2;  
        if (temp1 == 'R') {
            for (int h = 0; h < n; h++) {
                row[temp2][i] *= -1;
            }
        }
        if (temp1 == 'C') {
            for (int j = 0; j < m; j++) {
                row[j][temp2] *= -1;
            }
        }
    }
    string art;
    for (int h = 0; h < m; h++) {
        for (int j = 0; j < n; j++) {
            if (row[h][j] == -1) {
                art.push_back('B');
            }
            if (row[h][j] == 1) {
                art.push_back('G');
            }
        }
    }
    int gold = 0;
    for (int i = 0; i < m*n; i++) {
        if (art[i] == 'G') {
            gold += 1;
        }
    }
    cout << gold << endl;
}