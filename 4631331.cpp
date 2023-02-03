#include <iostream>
#include <vector>
#include <bits/stdc++.h>
using namespace std;
int main() {
    int dist, n;
    cin >> dist >> n;
    vector <int> clubs;
    for (int i = 0; i < n; i++) {
        int club;
        cin >> club;
        clubs.push_back(club);
    }
    vector <int> dp;
    for (int i = 0; i < dist+1; i++) {
        dp.push_back(10000);
    }
    dp[0] = 0;
    for (int i = 0; i < dist; i++) {
        for (int j = 0; j < n; j++) {
            if (clubs[j] + i <= dist) {
                dp[i+clubs[j]] = min(dp[i+clubs[j]], dp[i]+1);
            }
        }
    }
    if (dp[-1] != 10000) {
        cout << "Roberta wins in " << dp[dp.size()-1] << " strokes." << endl;
    }
    else {
        cout << "Roberta acknowledges defeat" << endl;
    }
}