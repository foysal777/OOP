// n.b: Public, private and protected three method show

#include <iostream>
#include <string>

class Computer {
private:
    std::string name;        // public in Python
    std::string _brand;      // protected-like in Python (convention with single underscore)
    std::string __password;  // private in Python (name mangling)

public:
    // Constructor
    Computer(std::string pc_name, std::string pc_brand) {
        name = pc_name;
        _brand = pc_brand;
        __password = "34-65-95"; // Setting the default password
    }

    // Public method equivalent to showName
    void showName() {
        std::cout << "The PC name is " << name << " and Brand is " << _brand << std::endl;
    }

    // Protected-like method equivalent to _showBrand (accessible, but conventionally for internal use)
    void _showBrand() {
        std::cout << "Brand is " << _brand << std::endl;
    }

    // Private method equivalent to __showPassword (inaccessible directly, uses name mangling)
    void __showPassword() {
        std::cout << "This is my Password: " << __password << std::endl;
    }

    // Public method to get the private password
    std::string get_password() {
        return __password;
    }

    // Function to mimic Python's name mangling for private methods
    void access_private_showPassword() {
        __showPassword(); // Access private method within the class
    }
};

int main() {
    // Creating an object (instance) of the Computer class
    Computer c("ViewSonic", "Dell");

    // Accessing the public method
    c.showName();

    // Accessing the protected-like method (by convention in Python)
    c._showBrand();

    // Accessing private attribute via public getter method
    std::cout << "Password: " << c.get_password() << std::endl;

    // Accessing private method (workaround for Python name mangling)
    c.access_private_showPassword();

    return 0;
}
