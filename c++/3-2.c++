    // switch-case statement
#include <iostream>

using namespace std;

int main(){
    int n;

    cout << "Enter number: ";
    cin >> n;

    switch(n){
        case 2:
            cout << "Monday";
            break;
        case 3:
            cout << "Tuesday";
            break;
        case 4:
            cout << "Wednesday";
            break;
        case 5:
            cout << "Thurstday";
            break;
        case 6:
            cout << "Friday";
            break;
        case 7:
            cout << "Saturday";
            break;
        case 8:
            cout << "Sunday";
            break;
        default:
            cout << "Invalid input";
    }
    
    int m;

    cout << "\n";
    cout << "Enter number: ";
    cin >> m;
    switch(m){
        case 1: case 3: case 5: case 7: case 8 : case 10: case 12:
            cout << "Thang " << m << " co 31 ngay";
            break;
        case 4: case 6: case 9: case 11:
            cout << "Thang " << m << " co 30 ngay";
            break;
        case 2:
            cout << "Thang " << m << " co 28 ngay";
            break;
        default:
            cout << "Invalid input";
    }
}