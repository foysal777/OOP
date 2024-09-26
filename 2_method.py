class Person:  #class name 
    
    species = "Homo sapiens"  # Class attribute (shared by all instances)
    def __init__(self , name , address) -> None: #constructor 
        
        self.name = name     #attribute
        self.address = address   #attribute
        print(self.name , self.address )
        
    def intro(self):  #Instance methods
        return (f"My name is {self.name} and I live in {self.address}")



        # Class method  
    @classmethod
    def get_species(cls):
        return f"All humans are {cls.species}"
    
    #This is the static method  and A static method is a method that belongs to a class but does not access or modify the class or instance state.
    @staticmethod  
    def static_method():
        print("I am a static Method")


p = Person('Foysal Hossain MUnna' , 'Dhonmondi')  # object or instance 
p = Person('Rakib sarker' , 'Elephant Road')  # object or instance 
p = Person('Tasfia' , 'new Market')  # object or instance 
print(p.get_species())
print(p.intro())
p.static_method()






















class A:
    pass

def display():
    print("I am Methods")

obj = A()
obj.value = display

print(obj.value)
print(obj)
