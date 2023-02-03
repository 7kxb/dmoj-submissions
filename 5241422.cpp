#include <iostream>
using namespace std;
int main() {
	int s, f, n;
	cin >> n;
	for (int j = 0; j < n; j++) {
    	cin >> s >> f;
    	int a = 0;
    	for (int i = s; i <= f; i++) {
    		a = a ^ i;
    	}
    	cout << a << endl;
	}
	return 0;
}