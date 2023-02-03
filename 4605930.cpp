#include <iostream>
using namespace std;
int main() {
    int S, R;
    cin >> S >> R;
    int Square = S*S;
    int Circle = 3.14*(R*R);
    if (Square > Circle) {
        cout << "SQUARE";
    }
    else if (Circle > Square) {
        cout << "CIRCLE";
    }
}