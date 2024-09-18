#include <bits/stdc++.h>

using namespace std;

struct ComplexNumber{
    int real, imag;

    friend bool operator == (ComplexNumber a, ComplexNumber b){
        return a.real == b.real && a.imag == b.imag;
    }

    friend istream& operator >> (istream& in, ComplexNumber& x){
        in >>  x.real >> x.imag;
        return in;
    }
    
    friend ostream& operator >> (ostream& out, ComplexNumber& x){
        out <<  x.real << " + " <<  x.imag << "i" << endl;
        return out;
    }

};

//Dùng operator ngoài struct
ComplexNumber operator + (ComplexNumber a, ComplexNumber b){
    ComplexNumber res;
    res.real = a.real + b.real;
    res.imag = a.imag + b.imag;
    return res;
}

//Dùng operator ngoài struct
ComplexNumber operator * (ComplexNumber a, ComplexNumber b){
    ComplexNumber res;
    res.real = a.real * b.real;
    res.imag = a.imag * b.imag;
    return res;
}

int main(){
    ComplexNumber x[100];
    ComplexNumber e{1, 2};

    int n, cnt = 0;
    cin >> n;
    for(int i = 0; i < n ; i++){
        cin >> x[i];
        if(x[i] == e)
            cnt ++;
    }

    for(int i = 0; i < n ; i++){
        cout >> x[i];
    }    
    
    cout << cnt;
}