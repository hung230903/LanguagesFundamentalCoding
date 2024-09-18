#include <iostream>

using namespace std;

int main(){
    // Mathematical operators: +, -, *, /, %
    // Assignment operators: =
    int a = 5, b = 2;
    int sum = a + b;
    int hieu = a - b;
    int tich = a * b;
    //Ép kiểu dữ liệu a thanh float để giá trị thuong trả về là float
    float thuong = float(a) / b;
    int du = a % b;

    cout << "Tong: " << sum  << endl;
    cout << "Hieu: " << hieu  << endl;
    cout << "Tich: " << tich  << endl;
    cout << "Thuong: " << thuong  << endl;
    cout << "Du: " << du  << endl;

    int c = 5;
    int f = 5;
    // giá trị c được tăng lên 1 sau khi câu lệnh được tạo
    int d = c++;
    // giá trị f được tăng lên 1 khi tạo câu lệnh
    int e = ++f;
    cout << "---" << endl;
    cout << "d = " << d << endl;
    cout << "c = " << c << endl;
    cout << "e = " << e << endl;

    //Comparison operators:  <, >, == , >=, <=, !=
    int i = 2, g = 1;
    int k = 2, l = 2;
    bool compare_1 = i > g;
    bool compare_2 = k >= l;
    bool compare_3 =  k < l;

    cout << "---" << endl;
    cout << compare_1 << endl;
    cout << compare_2 << endl;
    cout << compare_3 << endl;

    // Logical operators: &&(AND), ||(OR), !(NOT)
    cout << "---" << endl;
    int p = 2, h = 2, q = 3, w = 4;
    int res_1 = (p <= h) && (q < w);
    int res_2 = (p <= h) && (q > w);
    int res_3 = (p > h) || (q < w);
    int res_4 = (p > h) || (q > w);
    int res_5 = !(p > w);
    
    cout << res_1 << endl;
    cout << res_2 << endl;
    cout << res_3 << endl;
    cout << res_4 << endl;
    cout << res_5 << endl;

    //Conditional operator
    int x = 10 > 20 ? 10 : 20;
    cout << x;

    return 0;
}