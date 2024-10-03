# You can not create an object of abstract class 
# when you inherit abstract   class you must implement the abstract method 

from abc import ABC , abstractmethod

class A(ABC):
    
    @abstractmethod
    def name(self):
        pass
    
class B(A):
    
    
    def name(self):
        print("I am from abstract class")  # override the name mehtod()
    
    def hello(self):
        print("Hello , programmer")
        
        
b = B()
b.hello()
b.name()