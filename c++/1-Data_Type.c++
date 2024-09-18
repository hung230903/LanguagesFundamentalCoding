#include <iostream>
#include <iomanip>

using namespace std;

int main(){
    int Ban_Kinh = 0;
    int a, b, c;
    float d ;
    double e;
    char p;
    bool t = true, f = false;

    cout << "Enter a character: ";
    cin >> p;
    cout << p << endl;
    cout << "Enter a real number: ";
    cin >> d;
    cout << fixed << setprecision(2) << d << endl;
    cout << "Enter a real number: ";
    cin >> e;
    cout << fixed << setprecision(10) << e << endl;
    cout << "Enter 3 numbers: ";    
    cin >> a >> b >> c;
    cout << a << " " << b << " " << c << endl;
    cout << t << " " << f << endl;

    cout << Ban_Kinh << endl;
    cout << "Hello world";
    
    return 0;
}