    // for loop
#include <iostream>
#include <math.h>

using namespace std;

int main(){
    // In ra Hello world 4 lần
    cout << "In ra Hello world 4 lần" << endl;
    for(int i = 1; i <= 4; i++){
        cout << "Hello world\n";
    }
    
    // In ra các số chẵn
    cout << "---" << endl;
    cout << "In ra các số chẵn" << endl;
    int n;
    cout << "Enter n: ";
    cin >> n;
    for(int i = 0; i <= n; i+=2){
        if(i==0)
            continue;
        cout << i << endl;
    }
    
    
    // In ra các số i giảm dần
    cout << "---" << endl;
    cout << "In ra các số i giảm dần" << endl;
    for(int i = 10; i >= 0; i--){
        cout << i << endl;
    }
    
    // Dùng break trong for loop
    cout << "---" << endl;
    cout << "Dùng break trong for loop" << endl;
    for(int i = 10; i >= 0; i--){
        cout << i << endl;
        if(i == 6)
            break;
    }
    
    // Dùng continue trong for loop
    cout << "---" << endl;
    cout << "Dùng continue trong for loop" << endl;
    for(int i = 10; i >= 0; i--){
        if(i == 6)
            continue;
        cout << i << endl;

    }

    /*
        Bai tap:
            Nhap vao n nguyen duong, in ra tong S
            S = 1+2+3+...+n
    */ 

    int a, s = 0;
    cout << "---" << endl;
    cout << "Nhập vào số nguyên dương, in ra tổng S, S = 1+2+3+...+n" << endl;
    cout << "Enter a: ";
    cin >> a;

    for(int i=1; i<=a; i++){
        s += i;         
    }
    
    cout << "S = " << s << endl;
    
    /*
        Bai tap:
            Nhap vao n nguyen duong, in ra tong S
             = 1^2 + 2^2+ 3^2 +...+ n^2
    */ 
   int b, sum = 0;
    cout << "---" << endl;
    cout << "Nhập vào số nguyên dương, in ra tổng S, S = = 1^2 + 2^2+ 3^2 +...+ n^2" << endl;
    cout << "Enter a: ";
    cin >> b;

    for(int i=1; i<=b; i++){
        sum += pow(i, 2);         
    }
    
    cout << "S = " << sum;
    
    return 0;
}