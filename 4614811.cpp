#include <iostream>
#include <bits/stdc++.h>
using namespace std;
int main() {
    string number1;
    string number2;
    cin >> number1 >> number2;
    if (number1.length() > number2.length()) {swap(number1, number2);}
    string sum;
    int len1 = number1.length();
    int len2 = number2.length();
    int range = len2 - len1;
    int carry = 0;
    int sumint;
    for (int i = len1-1; i >= 0; i--) {
        sumint = ((number1[i]-'0') + (number2[i+range]- '0') + carry);
        sum.push_back(sumint % 10 + '0');
        carry = sumint/10;
    }
    for (int i = range-1; i >=0 ; i--) {
        sumint = ((number2[i]-'0')+carry);
        sum.push_back(sumint % 10 + '0');
        carry = sumint/10;
    }
    if (carry)
    sum.push_back(carry+'0');
    reverse(sum.begin(), sum.end());
    cout << sum << endl;
}