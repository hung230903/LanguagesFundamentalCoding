#include <bits/stdc++.h>

using namespace std;

struct Student{
    string name, id, date_birth, home_town;
    double gpa;

    // Constructor(Hàm khởi tạo): ko có kiểu dữ liệu trả về, tên hàm là tên struct
    Student(){
        name = "Nguyen Van A";
        id = "BI12-999";
        date_birth = "1/1/2023";
        home_town = "Ha Noi";
        gpa = 3.0;  
    }

    // Truyền tham số vào Constructor
    Student(string name, string id, string date_birth, string home_town, double gpa){
        // (this -> Student x)
        this -> name = name; 
        this -> id = id;
        this -> date_birth = date_birth;
        this -> home_town = home_town;
        this -> gpa = gpa;        
    }

    // Truyền tham số vào Constructor
    Student(double gpa){
        name = "Nguyen Van D";
        id = "BI12-22";
        date_birth = "3/1/2023";
        home_town = "Hai Phong";
        this -> gpa = gpa;
    }
};

void print_info(Student a){
    cout << "---\n";
    cout << "Your name is: " << a.name << endl;
    cout << "Your were born in: " << a.date_birth << endl;
    cout << "Your home town is: " << a.home_town << endl;
    cout << "Your GPA is: " << a.gpa << endl;
}

int main(){
    // Truyền tham trị vào Constructor
    Student x("Nguyen Van B", "BI12-000", "2/02/2023", "Sai Gon", 4.0);
    Student z(3.8);
    
    // Không truyền tham trị
    Student y;

    print_info(x);
    print_info(y);
    print_info(z);
}

