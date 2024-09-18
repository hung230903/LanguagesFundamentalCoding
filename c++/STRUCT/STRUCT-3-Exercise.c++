// Dùng struct để nhập tử/mẫu số sau đó in ra phân số đó
#include <bits/stdc++.h>

using namespace std;

#define ll long long

struct Fraction{
    ll denomirator, numerator;
};

ll Common_Divisor_Greatest(ll a, ll b){
    while(b){
        ll t = a % b;
        a = b;
        b = t;
    }
    return a;
}

void Frac_info(Fraction &p){
    cout << "Enter numerator: ";
    cin >> p.numerator;
    cout << "Enter denomirator: ";
    cin >> p.denomirator;
}

void Symplify(Fraction &p){
    ll k = Common_Divisor_Greatest(p.numerator, p.denomirator);
    p.numerator /= k;
    p.denomirator /= k;
}

void Print_Frac(Fraction p){
    cout << "Fraction: " << p.numerator << "/" << p.denomirator;
}

int main(){
    Fraction p;
    Frac_info(p);
    Symplify(p);
    Print_Frac(p);
}