#include <iostream>
using namespace std;

// Function to add two integers
int add(int a, int b) {
    return a + b;
}

// Function to add three integers
int add(int a, int b, int c) {
    return a + b + c;
}

// Function to add two floating-point numbers
float add(float a, float b) {
    return a + b;
}

int main() {
    
    cout << "Sum of 2 and 3 (int): " << add(2, 3) << endl;               // Calls the int version (two parameters)
    cout << "Sum of 2, 3, and 4 (int): " << add(2, 3, 4) << endl;        // Calls the int version (three parameters)
    cout << "Sum of 2.5 and 3.7 (float): " << add(2.5f, 3.7f) << endl;   // Calls the float version

    return 0;
}
