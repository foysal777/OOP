# Single Inheritance 

class X:
    def __init__(self , name , age , id) -> None:
        
        self.name= name
        self.age = age
        self.id = id
        
    
    def display(self):
        print(self.name)
        
    def show(self ):
        print(self.age)
        print(self.id)
        
        
class Y(X):
    
   def city(self):
       print("Bonani") 
    
   def __init__(self, name, age, id) -> None:
       super().__init__(name, age, id) #it means the person class all of attribute and method are inherite 
    
y = Y('robi' , 33 ,111)  #make a object for child class or subclass 
y.display()
y.show()
y.city()



