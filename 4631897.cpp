#include <iostream>
#include <vector>
#include <bits/stdc++.h>
using namespace std;
int main() {
    int N, M;
    cin >> N >> M;
    vector <int> trees;
    for (int i = 0; i < N; i++) {
        int tree;
        cin >> tree;
        trees.push_back(tree);
    }
    sort(trees.begin(), trees.end());
    int H = trees[N-1];
    int wood = 0;
    while (wood < M) {
        wood = 0;
        for (int i = 0; i < N; i++) {
            int temp = trees[i] - H;
            if (temp < 0) {
                temp = 0;
            }
            wood += temp;
        }
        if (wood < M) {
            H -= 1;
        }
    }
    cout << H << endl;
}