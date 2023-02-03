#include <iostream>
using namespace std;
int main() {
    int day, eve, end;
    cin >> day >> eve >> end;
    int diffa, diffb;
    if (day - 100 < 0) {
        diffa = 0;
    }
    else {
        diffa = day - 100;
    }
    if (day - 250 < 0) {
        diffb = 0;
    }
    else {
        diffb = day - 250;
    }
    cout << "Plan A costs " << diffa * 0.25 + eve * 0.15 + end * 0.20 << endl;
    cout << "Plan B costs " << diffb * 0.45 + eve * 0.35 + end * 0.25 << endl;
    if (diffa * 0.25 + eve * 0.15 + end * 0.20 == diffb * 0.45 + eve * 0.35 + end * 0.25) {
        cout << "Plan A and B are the same price." << endl;
    }
    else if (diffa * 0.25 + eve * 0.15 + end * 0.20 < diffb * 0.45 + eve * 0.35 + end * 0.25) {
        cout << "Plan A is cheapest." << endl;
    }
    else if (diffa * 0.25 + eve * 0.15 + end * 0.20 > diffb * 0.45 + eve * 0.35 + end * 0.25) {
        cout << "Plan B is cheapest." << endl;
    }
}