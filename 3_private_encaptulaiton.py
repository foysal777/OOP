class Person:
    def __init__(self, name, age):
        self.name = name             # Public attribute
        self._age = age              # Protected attribute
        self.__ssn = "123-45-6789"    # Private attribute

    # Public method
    def introduce(self):
        print(f"My name is {self.name} and I am {self._age} years old.")

    # Protected method
    def _display_age(self):
        print(f"I am {self._age} years old.")

    # Private method (name mangling prevents direct access)
    def __display_ssn(self):
        print(f"My SSN is {self.__ssn}")

    # Getter for private attribute
    def get_ssn(self):
        return self.__ssn

# Creating an object of the Person class
p = Person("Alice", 30)

# Accessing the public attribute and method
print(p.name)  
p.introduce()  

# Accessing the protected attribute and method (convention suggests not to)
print(p._age)  
p._display_age()  

# Accessing the private attribute and method (not directly accessible)
# print(p.__ssn)       
print(p.get_ssn())        

# Accessing private methods using name mangling
# print(p.__display_ssn())  # AttributeError: 'Person' object has no attribute '__display_ssn'
# However, you can access it using the name-mangled version:
p._Person__display_ssn()  # Output: My SSN is 123-45-6789
