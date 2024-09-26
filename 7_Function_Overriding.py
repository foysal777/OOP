class A:
    def display(self):
        print("i am A class")


class B(A):
    def display(self):
        print("I am B class")
        
class C(A): 
    def display(self):
        print("I am C class")
        

a = A()
b= B()
c= C()

a.display()
b.display()
c.display()
        
        















# Runtime Polymorphism -> Dynamic Binding | Overriding | Late Binding

# CompileTime Polymorphism-> Static Binding | Overloading | Early Binding