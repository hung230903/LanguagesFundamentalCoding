    // Mảng 2 chiều

#include <iostream>

using namespace std;

// Khi tạo hàm vào đưa vào 1 param là array 2 chiều thì phần tử của cột phải được khai báo số phần tử
void nhap(char c[100][100], int n, int m){
    cout << "Enter elements of the array(character): " << endl;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cin >> c[i][j];
        }
    }
}

int main(){
    int n, m;
    cout << "Enter elements of the row: ";
    cin >> n;
    cout << "Enter elements of the column: ";
    cin >> m;
    
    int a[100][100]; // 10000 phần tử: 100 hàng, 100 cột
    cout << "Enter elements of the array: " << endl;
    // Nhập phần tử theo hàng
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cin >> a[i][j];
        }
    }
    
    cout << endl;
    cout << "Array: " << endl;
    // In phần tử trong mảng theo từng hàng
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cout << a[i][j] << " ";
        }
        cout << endl;
    }
    
    cout << endl;
    cout << "Array: " << endl;
    // In phần tử trong mảng theo từng cột
    for(int i = 0; i < m; i++){
        for(int j = 0; j < n; j++){
            cout << a[j][i] << " ";
        }
        cout << endl;
    }

    cout << "---" << endl;
    char c[100][100];
    nhap(c ,n, m);
    cout << endl;
    cout << "Array: " << endl;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            cout << c[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}