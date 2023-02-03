#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
    long n, p, m;
    cin >> n >> p >> m;
    long ui, vi;
    vector <long> u, v;
    for(long i = 0; i < n; i++) {
        cin >> ui >> vi;
        u.push_back(ui);
        v.push_back(vi);
    }
    long ai;
    vector <long> a;
    for(long i = 0; i < p; i++) {
        cin >> ai;
        a.push_back(ai);
    }
    long bi;
    vector <long> b;
    for(long i = 0; i < m; i++) {
        cin >> bi;
        b.push_back(bi);
    }
    vector <long> total;
    for (long j = 0; j < n; j++) {
        long physical = 0;
        long magical = 0;
        for(long k = 0; k < p; k++) {
            if (a[k] - u[j] < 0) {
                physical += 0;
            }
            else {
                physical += a[k] - u[j];
            }
        }
        for(long k = 0; k < m; k++) {
            if (b[k] - v[j] < 0) {
                magical += 0;
            }
            else {
                magical += b[k] - v[j];
            }
        }
        total.push_back(physical+magical);
        //cout << physical << ' ' << magical << endl;
        //cout << physical+magical << endl;
    }
    long min = 1e18+5;
    long index = 0;
    long size = total.size();
    for(long i = 0; i < size; i++){
        if(total[i]< min){
            min = total[i];
            index = i;
        }
    }
    cout << index+1 << endl;
}