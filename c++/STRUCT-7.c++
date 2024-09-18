#include<bits/stdc++.h>

using namespace std;

struct Location{
    string country, city;
};

struct Student{
    string name, dob;
    Location lt;
    double gpa;
};

int main(){
    Student x;
    
    cout << "Enter name: ";
    cin >> x.name;
    cout << "Enter dob: ";
    cin >> x.dob;
    cout << "Enter country: ";
    cin >> x.lt.country;
    cout << "Enter city: ";
    cin >> x.lt.city;
    cout << "Enter gpa: ";
    cin >> x.gpa;
}