#include <iostream>
#include <string>

class Person {
private:
    // Instance attributes (equivalent to Python's self.name and self.address)
    std::string name;
    std::string address;

public:
    // Class attribute (equivalent to Python's species, shared by all instances)
    static std::string species;

    // Constructor (equivalent to __init__)
    Person(std::string n, std::string a) : name(n), address(a) {
        std::cout << name << " " << address << std::endl;
    }

    // Instance method (equivalent to Python's intro)
    std::string intro() {
        return "My name is " + name + " and I live in " + address;
    }

    // Class method (equivalent to Python's @classmethod)
    static std::string get_species() {
        return "All humans are " + species;
    }

    // Static method (equivalent to Python's @staticmethod)
    static void static_method() {
        std::cout << "I am a static method." << std::endl;
    }
};

// Initialize static class attribute outside the class definition
std::string Person::species = "Homo sapiens";

int main() {
    // Creating objects (instances)
    Person p1("Foysal Hossain MUnna", "Dhanmondi");
    Person p2("Rakib Sarker", "Elephant Road");
    Person p3("Tasfia", "New Market");

    // Calling the class method
    std::cout << Person::get_species() << std::endl;

    // Calling the instance method
    std::cout << p1.intro() << std::endl;

    // Calling the static method
    Person::static_method();

    return 0;
}
