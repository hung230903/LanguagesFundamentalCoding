// Function
#include <iostream>
#include <math.h>

using namespace std;

void tich(int a, int b, int c){
    cout << a*b*c << endl;
}

int sum(int n){
    return n*(n+1)/2;
}

// tinh tong S = 1+1/2+1/3+...+1/n
float sum_1(int n){
    float res = 0;
    for(int i=1; i<=n; i++){
        res += 1.0/i;
    }

    return res;
}

//Kiem tra so nguyen to
bool prime(int n){
    for(int i=2; i<sqrt(n); i++){
        if(n%i==0)
            return false;
    }

    return n>1;
}

//Kiem tra tong chu so cua 1 so co phai so nguyen to hay khong
bool check(int n){
    int sum = 0;
    while(n){
        sum += n%10;
        n /= 10;
    }

    if(prime(sum))
        return true;    
    else
        return false;
}

//Truyen tham chieu
int tang(int &a){
    ++a;
    return a;
}

//Function overloading
int tong(int i, int g){
    return i+g;
}

float tong(float i, float g){
    return i+g;
}

int main(){
    int n;
    tich(10, 20, 30);
    
    cout << "Enter n: ";
    cin >> n;

    cout << sum(n) << endl;
    cout << sum_1(n) << endl;
    cout << n << " la so nguyen to: " << prime(n) << endl;
   
    if(check(n))
        cout << "Tong chu so cua n la so nguyen to: " << "True";
    else
        cout <<"Tong chu so cua n la so nguyen to: " << "False";
    
    int a=5;
    cout << "\n";
    cout << "Gia tri a sau khi truyen vao tham chieu: " << tang(a) << endl; 
    
    cout << "---" << endl;
    int i = 1, g = 2;
    //float i = 1.1, g = 2.2 thi ham float tong se dc chay
    cout << tong(i, g);
    return 0;
}