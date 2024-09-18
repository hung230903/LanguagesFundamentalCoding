// typedef và define

#include <iostream>

using namespace std;

// typedef có thể định nghĩa tên kiểu dữ liệu thành 1 tên mới mà người dùng muốn
// typedef được xử lý bởi compiler
typedef long long ll;
typedef int songuyen;
typedef float st;

// define có thể định nghĩa được nhiều hơn
// define được xử lý bởi pre-processor
#define kitu char
#define pi 3.14
#define FOR(i, a, b) for(int i = (a); i < (b); i++)

// using có thể dùng thay cho typedef
using db = double;

int main(){
    songuyen a = 3;
    ll b = 3;
    st n = 2.3;

    cout << "a = " << a << endl;
    cout << "b = " << b << endl;
    cout << "n = " << n << endl;

    kitu c = 'a';
    cout << "c = " << a << endl;
    cout << pi << endl;
    FOR(i, 0, 5){
        cout << i << " ";
    }

    cout << endl;
    db u = 3.12321;
    cout << "u = " << u;
}