#include <bits/stdc++.h>

using namespace std;

struct Student{
    string name, id, date_birth, home_town;
    double gpa;

    // Khai báo hàm trong struct
    void print_info_1(){
        cout << "---\n";
        cout << "Your name is: " << name << "\n";
        cout << "Your were born in: " << date_birth << "\n";
        cout << "Your home town is: " << home_town << "\n";
        cout << "Your GPA is: " << gpa << "\n";
    }
    
    // Khai báo hàm trong struct
    void person_info_1(){
        cout << "Enter full name: ";
        getline(cin, name);
        cout << "Enter ID: ";
        cin >> id;
        cout << "Enter date of birth: ";
        cin >> date_birth;
        cout << "Enter home town: ";
        scanf("\n");
        getline(cin, home_town);
        cout << "Enter GPA: ";
        cin >> gpa;
    }

};

// Khai báo hàm ngoài struct
void print_info_2(Student a){
    cout << "---\n";
    cout << "Your name is: " << a.name << "\n";
    cout << "Your were born in: " << a.date_birth << "\n";
    cout << "Your home town is: " << a.home_town << "\n";
    cout << "Your GPA is: " << a.gpa << "\n";
}

// Khai báo hàm ngoài struct
void person_info_2(Student &a){
    cout << "---\n";
    cout << "Enter full name: ";
    scanf("\n");
    getline(cin, a.name);
    cout << "Enter ID: ";
    cin >> a.id;
    cout << "Enter date of birth: ";
    cin >> a.date_birth;
    cout << "Enter home town: ";
    scanf("\n");
    getline(cin, a.home_town);
    cout << "Enter GPA: ";
    cin >> a.gpa;    
}

int main(){
    Student x;
    
    // Khởi tạo 1 sturct có đầy đủ thuộc tính có sẵn
    Student y{"Nguyen Ngoc Son", "BI12-199", "11/02/2003", "Ha Long", 3.88};

    Student z;
    
    x.person_info_1();
    person_info_2(z);

    z.print_info_1();
    x.print_info_1();    
    print_info_2(y);
}