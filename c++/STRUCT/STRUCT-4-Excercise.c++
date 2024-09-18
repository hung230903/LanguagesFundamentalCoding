//Dùng struct để nhập vào tử/mẫu số của 2 phân số sau đó tính tổng và in ra tổng
#include <bits/stdc++.h>

using namespace std;

#define ll long long

struct Fraction{
    int numerator, denominator;
};

void Fraction_Info(Fraction &a, Fraction &b){
    cout << "Enter the first fraction" << endl;
    cout << "Enter numerator: ";
    cin >> a.numerator;
    cout << "Enter denominator: ";
    cin >> a.denominator;
    
    cout << "Enter the second fraction" << endl;
    cout << "Enter numerator: ";
    cin >> b.numerator;
    cout << "Enter denominator: ";
    cin >> b.denominator;
}

ll Common_Divisor_Greatest(ll a, ll b){
    while(b){
        ll t = a % b;
        a = b;
        b = t;
    }
    return a;
}

void Symplify(Fraction &p){
    ll k = Common_Divisor_Greatest(p.numerator, p.denominator);
    p.numerator /= k;
    p.denominator /= k;
}

Fraction Sum(Fraction a, Fraction b){
    Fraction res;
    res.denominator = (ll)a.denominator * b.denominator;
    res.numerator = (ll)b.denominator*a.numerator + (ll)a.denominator*b.numerator;
    Symplify(res);
    return res;
}

void Print_Sum(Fraction p){
    cout << "---" << endl;
    cout << "Sum = " << p.numerator << "/" << p.denominator;
}

int main(){
    Fraction x;
    Fraction y;

    Fraction_Info(x, y);
    Fraction t = Sum(x, y);
    Print_Sum(t);
}