    //Thư viện <math.h> và một số hàm toán học 
#include <iostream>
#include <math.h>

using namespace std;

int main(){
    // pow(a, b): tính a^b
    // pow(a, b) trả về số double
    int a = 2;
    int b = 10;
    int res = pow(a,b);

    cout << res << endl;
    cout << "---" << endl;

    // abs(x): Trị tuyệt đối
    int c = -100;
    cout << abs(c) << endl;

    // sqrt(n): tính căn bậc 2 của n
    // sqrt(n) trả về số double
    int d = 4;
    int temp = sqrt(d);
    
    cout << temp << endl;
    cout << "---" << endl;

    // round(a): làm tròn số a
    float i = 2.213656;
    float g = 2.995656;
    int round_1 = round(i) ;
    int round_2 = round(g);

    cout << round_1 << endl; 
    cout << round_2; 
}