#include <iostream>
using namespace std;
int main() {
    int x, y;
    int a, b;
    cin >> x >> y;
    cin >> a >> b;
    int counter = 0;
    //
    for (int i = 1; i < a+b-x-y; i++) {
        if (x + 1 <= 8 && y + 2 <= 8) {
    		int x = x + 1;
    		int y = y + 2;
    		counter += 1;
    	}
        else if (x + 2 <= 8 && y + 1 <= 8) {
    		int x = x + 2;
    		int y = y + 1;
    		counter += 1;
    	}
    	else if (x + 2 <= 8 && y - 1 >= 1) {
    		int x = x + 2;
    		int y = y - 1;
    		counter += 1;
    	}
        else if (x + 1 <= 8 && y - 2 >= 1) {
    		int x = x + 1;
    		int y = y - 2;
    		counter += 1;
    	}
        else if (x - 2 >= 1 && y - 1 >= 1) {
    		int x = x - 2;
    		int y = y - 1;
    		counter += 1;
    	}
        else if (x - 1 >= 1 && y - 2 >= 1) {
    		int x = x - 1;
    		int y = y - 2;
    		counter += 1;
    	}
        else if (x - 2 >= 1 && y + 1 <= 8) {
    		int x = x - 2;
    		int y = y + 1;
    		counter += 1;
    	}
    	else if (x - 1 >= 1 && y + 2 <= 8) {
    		int x = x - 1;
    		int y = y + 2;
    		counter += 1;
    	}
    }
	//
	cout << counter/2 << endl;
}