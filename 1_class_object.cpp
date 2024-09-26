
#include <iostream>
#include <string>
using namespace std;

class Person {  // class name
public:
    // Attributes
    string name;
    string address;

    // Constructor
    Person(string name, string address) {
        this->name = name;         // Assigning the name attribute
        this->address = address;   // Assigning the address attribute
        cout << name << " " << address << endl;  // Printing name and address in constructor
    }

    // Method to introduce the person
    string intro() {
        return "My name is " + name + " and I live in " + address;
    }
};

int main() {
    // Creating objects (instances) of the Person class
    Person p1("Foysal Hossain Munna", "Dhanmondi");
    Person p2("Rakib Sarker", "Elephant Road");
    Person p3("Tasfia", "New Market");

    // Accessing the intro method of the last object (p3)
    cout << p3.intro() << endl;

    return 0;
}






























// #include<bits/stdc++.h>
// using namespace std;

// // class A{
// //     public:
// //     int value;
// //     //constructor
// //     A(int value){
// //         this->value = value;
// //         cout<<"Constructor Called"<<endl;
// //     }

// //     //method
// //     void display(){
// //         cout<<"Hello\n";
// //     }

// //     //destructor
// //     ~A(){
// //         cout<<"Desonstructor Called"<<endl;
// //     }
// // };
                    
// // int main(){
// //     A obj(8);
// //     obj.display();
// //     // obj.value = 5;
// //     cout<<obj.value<<endl;
            
              
// //     return 0;
// // }








// class A{
// public:
//     A(){
//         printf("I am Constructor\n");
//     }

//     void display(){
//         cout<<"I am Display Method\n";
//     }

//     ~A(){
//         cout<<"I am Destructor\n";
//     }

// };

// int main(){
//     A obj;
//     obj.display();

// }