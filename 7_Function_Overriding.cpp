


#include <iostream>
using namespace std;

class A {
public:
    // Member function to display a message
    virtual void display() {
        cout << "I am A class" << endl;
    }
};

class B : public A {
public:
    // Overridden member function to display a different message
    void display() override {
        cout << "I am B class" << endl;
    }
};

class C : public A {
public:
    // Overridden member function to display another message
    void display() override {
        cout << "I am C class" << endl;
    }
};

int main() {
    // Creating objects of the classes
    A a;
    B b;
    C c;

    // Calling the display function for each object
    a.display();  // Output: I am A class
    b.display();  // Output: I am B class
    c.display();  // Output: I am C class

    return 0;
}
