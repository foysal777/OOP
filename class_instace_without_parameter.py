#self instance variable der call korar jonno use kora hoy 
#instance variable k object sara acess kora jabe na and self deye acess kora lagbe


class House:
    
    def __init__(self) -> None: #without parameter call the constructor 
        self.window = 6 # default variable or instance variable 
        self.door = 12 #default variable 
        
    def view(self): # for printing create a different method 
        print(" window : " , self.window , "\n Door is: "  ,self.door)
        

h1 = House()
h1.window = 20  # update the windows
h2 = House()
h1.view()
        
        
        
class Dog:
    
    def __init__(self , name , color) -> None:
        
        self.dog_name = name
        self.dog_color = color
        
    def update_color(self , color):
        self.dog_color = color
       
        
    def poke(self):
        print(self.dog_name , "color is  " , self.dog_color , "is smilling" )
        
        
d1 = Dog("Tommy" , "black")
d1.poke()
d1.update_color("BLue")

        
d12= Dog("Jemmy" , "White")
d12.update_color("yellow")
d12.poke()

print(d12.__dict__)  #show the dictonary way value and attribute
print(dir(d1)) # show the all built in fuction and attribute alos show the function 