#include <iostream>
using namespace std;

// Base class (Grandparent class)
class A {
public:
    void methodA() {
        cout << "This is method from class A" << endl;
    }
};

// Intermediate class (Parent class)
class B : public A {
public:
    void methodB() {
        cout << "This is method from class B" << endl;
    }
};

// Derived class (Child class)
class C : public B {
public:
    void methodC() {
        cout << "This is method from class C" << endl;
    }
};

int main() {
    // Creating an object of class C
    C obj;

    // Calling methods from all three classes
    obj.methodA();  // Inherited from class A
    obj.methodB();  // Inherited from class B
    obj.methodC();  // Defined in class C

    return 0;
}
