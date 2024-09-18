#include <bits/stdc++.h>

using namespace std;

bool CheckPrime(int n){
    while(n){
        int r = n % 10;
        if(r % 2 == 0)
            return false;
        n /= 10;
    }
    return true;
}

int main(){
    //Ex1: Cho 1 mảng số nguyên, đếm số lượng số nguyên tố và in ra các số nguyên tố trong dãy
    int n;
    cout << "Enter number of elements in the array: ";
    cin >> n;

    int a[n];
    for(int i = 0; i < n; i++){
        cout << "a[" << i << "] = ";
        cin >> a[i];
    }

    int cnt = 0;
    for(int i = 0; i < n; i++){
        if(CheckPrime(a[i]))
            cnt++;
    }
    cout << "Number of prime number: " << cnt;

}