# Base class super class
class A:
    def method_a(self):
        print("This is method from class A")

# Intermediate class (Parent class)
class B(A):
    def method_b(self):
        print("This is method from class B")

# Derived class (Child class)
class C(B):
    def method_c(self):
        print("This is method from class C")

# Creating an instance of the child class C
obj = C()

# Calling methods from all three classes
obj.method_a()  # Inherited from class A
obj.method_b()  # Inherited from class B
obj.method_c()  # Defined in class C
