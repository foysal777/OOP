#include <iostream>
using namespace std;

class J {
public:
    void displayJ() {
        cout << "I am J method" << endl;
    }
};

class K {
public:
    void displayK() {
        cout << "I am K method" << endl;
    }
};

class L : public J, public K {  // Multiple inheritance: L inherits from both J and K
public:
    L() {
        // Constructor equivalent to Python's __init__
        // In C++, you don't need to explicitly call a constructor like 'super()'
    }

    void displayL() {
        cout << "I am L method" << endl;
    }
};

int main() {
    L l;  // Create an instance of class L
    l.displayJ();  // Call the method from class J
    l.displayK();  // Call the method from class K
    l.displayL();  // Call the method from class L

    return 0;
}
