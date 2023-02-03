# include <iostream>
using namespace std;
int main() {
string a;
cin >> a;
if (
a.find('A') != string::npos || 
a.find('B') != string::npos ||
a.find('C') != string::npos ||
a.find('D') != string::npos ||
a.find('E') != string::npos ||
a.find('F') != string::npos ||
a.find('G') != string::npos ||
a.find('J') != string::npos ||
a.find('K') != string::npos ||
a.find('L') != string::npos ||
a.find('M') != string::npos ||
a.find('P') != string::npos ||
a.find('Q') != string::npos ||
a.find('R') != string::npos ||
a.find('T') != string::npos ||
a.find('U') != string::npos ||
a.find('V') != string::npos ||
a.find('W') != string::npos ||
a.find('Y') != string::npos
)
cout << "NO" << endl;
else 
cout << "YES" << endl;
}