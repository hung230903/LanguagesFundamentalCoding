//Big(O): Độ phức tạp của thuật toán

#include <iostream>
#include <math.h>

using namespace std;

bool prime(int n){
//O(Logn): vòng lặp chạy căn 2 n lần
    for(int i = 2; i <= sqrt(n); i++){
        if(n % i == 0)
            return false;
    }
    return n>1;
}

bool prime_1(int n){
    // O(n)
    for(int i = 2; i < n; i++){
        if(n % i == 0)
            return false;
    }
    return true;
}

int main(){
    //Đồng bộ thời gian chạy cout, cin với printf và scanf(cin, cout chạy nhanh hơn)
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    
    int a = 10; //O(1)
    int b = a + 10; //O(1)
    int n; //O(1)
    cout << "Enter n: "; //O(1)
    cin >> n; //O(1)

    //vòng lặp for đc coi là O(n): chỉ khi câu lệnh trong vòng lặp cũng là O(n)
    for(int i = 1; i <= n; i++){
        cout << i << endl;
    }

    cout << "---" << endl;
    
    //O(n*logn)
    for(int i = 1; i <= n; i++){
        if(prime(i))
            cout << i << endl;
    }

    cout << "---" << endl;

    // O(n*n) = O(n^2)
    int m;
    cout << "Enter m: "; //O(1)
    cin >> m; //O(1)
    for(int i = 0; i <= m; i++){
        if(prime(i)){
            cout << i << endl;
        }
    }

    cout << "---" << endl;

    //O(m*n) = O(n^2)
    int j, k;
    cout <<"Enter j:";
    cin >> j;
    cout <<"Enter k:";
    cin >> k;
    for(int i = 0; i <= j; i++){
        for(int i = 0; i <= m; i++)
            cout << i << endl; // câu lệnh này pahri là O(n)
    }

    /*
        Tổng độ phức tạp của chương trình sau khi code
            VD: O(n^2 + n + 1 + n^3 + n*logn)
                -> Độ phức tạp của chương trình là thành phần có bậc lớn nhất: O(n^3)
    */
    return 0;
}

