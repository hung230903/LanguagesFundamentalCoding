    // while loop
#include <iostream>

using namespace std;

int main(){
    int i = 0;

    // In ra i từ 0 đến 4
    while(i<5){
        cout << i << endl;
        i++;
    }

    // Dùng break trong while loop
    cout << "---" << endl;
    int f = 0;
    while(f<5){
        cout << f << endl;
        f++;
        if(f==3)
            break;
    }

    // Dùng continue trong while loop
    cout << "---" << endl;
    int g = 0;
    cout << 0 << endl;
    while(g<10){
        g++;
        if(g==3)
            continue;
        cout << g << endl;
    }

    /*
        Bai tap:
            Nhap vao so nguyen duong n, dem so luong chu so cua n
    */
    cout << "---" << endl;
    int n, cnt = 0;
    cout << "Enter n: ";
    cin >> n;
    while(n!=0){
        cnt++;
        n /= 10; 
    }
    cout << "Numbers of the interger: " << cnt << endl;

    /*
        Bai tap:
            Nhap vao so nguyen duong n, tinh tong cac chu so cua n
    */
    cout << "---" << endl;
    int a, sum = 0;
    cout << "Enter a: ";
    cin >> a;
    while(a!=0){
        sum += a%10;
        a /= 10; 
    }
    cout << "Sum of the interger: " << sum << endl;

    // do-while loop
    cout << "---" << endl;
    int m;
    do{
        cout << "Enter m>5: ";
        cin >> m;
    } while(m<=5);
    cout << m;

    return 0;
}