#include <iostream>
#include <vector>
#include <stdio.h>
using namespace std;
int fib(int n) {
  int a = 0, b = 1, c, i;
  if (n == 0)
    return a%1000000007;
  for (i = 2; i <= n; i++) {
     c = a + b;
     a = b;
     b = c;
  }
  return b%1000000007;
}
int main() {
  int n;
  cin >> n;
  cout << fib(n) << endl;
}