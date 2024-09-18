    // if-else statement
#include <iostream>

using namespace std;

int main(){
    int n;
    int m;

    cout << "Enter month: ";
    cin >> n;
    cout << "Enter year: ";
    cin >> m;

    cout << "---"  << endl;
    if((n == 1) || (n == 3) || (n == 5) || (n == 7) || (n == 8)){
        cout << "Thang " << n << " co 31 ngay";
    }
    else if((n == 4) || (n == 6) || (n == 9) || (n == 11)){
        cout << "Thang " << n << " co 30 ngay";
    }
    else if(n == 2)
        if((m % 2 == 0) || ((m % 400) == 0 && (m % 100 == 0)))
            cout << "Thang " << n << " co 29 ngay";
        else
            cout << "Thang " << n << " co 28 ngay"; 
    else{
        cout << "Invalid input";
    }
     
    return 0;
}