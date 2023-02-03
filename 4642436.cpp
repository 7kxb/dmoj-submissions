#include <iostream>
#include <vector>
using namespace std;
//
void alg(int x1, int y1, vector<vector<int>> & sq, int m) {
	sq[x1][y1] = m;
	if (x1 + 1 <= 8 && y1 + 2 <= 8) {
		int x2 = x1 + 1;
		int y2 = y1 + 2;
		if ((sq[x2][y2] == 0) || (sq[x2][y2] > m + 1))
			alg(x2, y2, sq, m + 1);
	} if (x1 + 2 <= 8 && y1 + 1 <= 8) {
		int x2 = x1 + 2;
		int y2 = y1 + 1;
		if ((sq[x2][y2] == 0) || (sq[x2][y2] > m + 1))
			alg(x2, y2, sq, m + 1);
	} if (x1 + 2 <= 8 && y1 - 1 >= 1) {
		int x2 = x1 + 2;
		int y2 = y1 - 1;
		if ((sq[x2][y2] == 0) || (sq[x2][y2] > m + 1))
			alg(x2, y2, sq, m + 1);
	} if (x1 + 1 <= 8 && y1 - 2 >= 1) {
		int x2 = x1 + 1;
		int y2 = y1 - 2;
		if ((sq[x2][y2] == 0) || (sq[x2][y2] > m + 1))
			alg(x2, y2, sq, m + 1);
	} if (x1 - 2 >= 1 && y1 - 1 >= 1) {
		int x2 = x1 - 2;
		int y2 = y1 - 1;
		if ((sq[x2][y2] == 0) || (sq[x2][y2] > m + 1))
			alg(x2, y2, sq, m + 1);
	} if (x1 - 1 >= 1 && y1 - 2 >= 1) {
		int x2 = x1 - 1;
		int y2 = y1 - 2;
		if ((sq[x2][y2] == 0) || (sq[x2][y2] > m + 1))
			alg(x2, y2, sq, m + 1);
	} if (x1 - 2 >= 1 && y1 + 1 <= 8) {
		int x2 = x1 - 2;
		int y2 = y1 + 1;
		if ((sq[x2][y2] == 0) || (sq[x2][y2] > m + 1))
			alg(x2, y2, sq, m + 1);
	} if (x1 - 1 >= 1 && y1 + 2 <= 8) {
		int x2 = x1 - 1;
		int y2 = y1 + 2;
		if ((sq[x2][y2] == 0) || (sq[x2][y2] > m + 1))
			alg(x2, y2, sq, m + 1);
	}
}
//
int main() {
	int ax, ay;
    int bx, by;
	cin >> ax >> ay;
	cin >> bx >> by;
	if (ax == bx && bx == by) {
		cout << 0 << endl;
	} else {
	vector<vector<int>> sq(9, vector<int>(9, 0));
	alg(ax, ay, sq, 0);
	cout << sq[bx][by] << endl;
	}
}