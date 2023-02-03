#include <iostream>
#include <vector>
#include <bits/stdc++.h>
using namespace std;
int main() {
    int x, n;
    cin >> x >> n;
    vector <int> ds;
    for (int i = 0; i < n; i++) {
        int d;
        cin >> d;
        ds.push_back(d);
    }
    vector <int> dp;
    for (int i = 0; i < x+1; i++) {
        dp.push_back(10000);
    }
    dp[0] = 0;
    for (int i = 0; i < x; i++) {
        for (int j = 0; j < n; j++) {
            if (ds[j] + i <= x) {
                dp[i+ds[j]] = min(dp[i+ds[j]], dp[i]+1);
            }
        }
    }
    if (dp[dp.size()-1] != 10000) {
        cout << dp[dp.size()-1] << endl;
    }
    else {
        cout << "err" << endl;
    }
}