#include <bits/stdc++.h>

using namespace std;

bool prime(int n){
    for(int i = 2; i <= sqrt(n); i++){
        if(n%i == 0)
            return false;
    }
    return n > 1;
}

int main(){
    // Kieu_Du_Lieu Array_name[So luong phan tu mang]

    //Nhập số phần tử và in ra các phần tử trong mảng
    cout << "Nhập số phần tử và in ra các phần tử trong mảng" << endl;
    int n;
    cout << "Enter number elements of the array: ";
    cin >> n;
    int a[n]; 
    for(int i = 0; i < n; i++){
        cout << "a[" << i << "]" << " = ";
        cin >> a[i];
    }
    cout << endl;
    cout << "All the elements in the array" << endl;
    for(int i = 0;  i < n; i++){
        cout << "a[" << i << "]" << " = " << a[i] << endl;
    }

    //Duyệt phần tử mảng từ số lớn nhất
    cout << "---" << endl;
    cout << "Duyệt phần tử mảng từ số lớn nhất" << endl;
    for(int i = n - 1; i >= 0; i--){
        cout << "a[" << i << "]" << " = " << a[i] << endl;
    }
    
    //Tính tổng các phần tử trong mảng
    cout << "---" << endl;
    cout << "Tính tổng các phần tử trong mảng" << endl;
    int sum = 0;
    for(int i = 0;  i < n; i++){
        sum += a[i];
    }
    cout << "Sum = " << sum << endl;

    //In ra các số nguyên tố trong mảng
    cout << "---" << endl;
    cout << "In ra các số nguyên tố trong mảng" << endl;
    for(int i = 0; i < n; i++){
        if(prime(a[i]))
            cout << "a[" << i << "]" << " = " << a[i] << endl;
    }
     
    //Các phẩn tử trong mảng chưa đc tạo sẽ có giá trị là 0
    cout << "---" << endl;
    cout << "Các phẩn tử trong mảng chưa đc tạo sẽ có giá trị là 0" << endl;
    cout << "Mảng b có 4 phần tử và có 2 phần tử được gán giá trị lần lượt là 1, 2" << endl;
    int b[4] = {1,2};
    for(int i = 0; i < 4; i++){
        cout << "b[" << i << "]" << " = " << b[i] << endl;
    }

    //Cách duyệt/nhập các phần tử trong mảng với for each
    cout << "---" << endl;
    cout << "Cách duyệt/nhập các phần tử trong mảng với for each" << endl;
    int c[5];
    cout << "Enter value of each element in the array" << endl;
    for(int &x : c)
        cin >> x;
    
    cout << "Print out all the elements in the array" << endl;
    for(int x : c){
        cout << x << endl;
    }

    //for each sẽ duyệt tất cả các phần tử ở trong mảng
    cout << "---" << endl;
    cout << "for each sẽ duyệt tất cả các phần tử ở trong mảng" << endl;
    int d[10] = {1,2};
    for(int x : d){
        cout << x << endl;
    }
}