#include <bits/stdc++.h>

using namespace std;

struct ComplexNumber{
    int real, imag;

    /*Cách 1: dùng operator
    ComplexNumber operator + (ComplexNumber other){
        ComplexNumber res;
        res.real = real * other.real;
        res.imag = imag * other.imag;
        return res;
    }
    */

    /*Cách 2: dùng hàm friend
    friend ComplexNumber operator * (ComplexNumber other){
        ComplexNumber res;
        res.real = real * other.real;
        res.imag = imag * other.imag;
        return res;
    }
    */
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

void PrintComplexNumber(ComplexNumber c , ComplexNumber d){
    cout << "Add: " << c.real << " + " << c.imag << "i" << endl;
    cout << "Multiply: " << d.real << " * " << d.imag << "i" << endl;
}

int main(){
    ComplexNumber a{1, 2}, b{8, 9};
    ComplexNumber c = a + b;
    ComplexNumber d = a * b;
    PrintComplexNumber(c, d);
}