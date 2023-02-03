#include <iostream>
#include <time.h>
using namespace std;
int main() {
    srand(time(NULL));
    cout << "1";
    cout << "16";
    cout << "2";
    for (int i = 0; i < 16; i++) rand();
    cout << to_string(rand());
}