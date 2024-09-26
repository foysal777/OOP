class Person:  #class name 
    
    species = "Homo sapiens"  # Class attribute (shared by all instances)
    def __init__(self , name , address) -> None: #constructor 
        
        self.name = name     #attribute
        self.address = address   #attribute
        print(self.name , self.address )
        
    def intro(self):  #methods
        return (f"My name is {self.name} and I live in {self.address}")



        # Class method
    @classmethod
    def get_species(cls):
        return f"All humans are {cls.species}"

p = Person('Foysal Hossain MUnna' , 'Dhonmondi')  # object or instance 
p = Person('Rakib sarker' , 'Elephant Road')  # object or instance 
p = Person('Tasfia' , 'new Market')  # object or instance 
print(p.get_species())
print(p.intro())


    





























# *************************************************

class A:
    value = 5 #class variable
    def __init__(self) -> None:
        print("I am Constructor")
    
    def display(self):
        print("I am method")

    def __del__(self):
        print("I am destructor")

    def __str__(self) -> str:
        return "I am ClasS A"




obj = A()
obj1 = A()
obj.display()
obj.value = 5

print(obj.__dict__)





print(obj.value)
print(A.value)






