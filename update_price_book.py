class Book:
    def __init__(self, name , author ) -> None:
        
        self.name = name 
        self.author = author
        self.price = 0
        
        
    def set_price(self , price): # for update the price 
        self.price = price
        
    def get_price(self): # show the price of book 
        return self.price
    
    def deatils(self):
        print("Book Name : " , self.name ,
                "\n Author : " , self.author ,
                   "\n price : " , self.price
              
              )
    
b = Book('Dehokabbo' , 'Faizul')
b.deatils()
b.set_price(1200)
b.deatils()
print(b.get_price())
        
        
class Cat:
    
    def __init__(self , color , action) -> None:
        self.color = color
        self.action = action
        
    def view(self):
        print(self.color , "is " , self.action)
        
    def compare(self , ct):
        if self.action == ct.action:
            print("They are same action" , self.action)
            
        else:
            print("The are not same action perform")

c1 = Cat("White" , 'Jump')
c2 = Cat("blue" , 'Jumping')

c1.view()
c2.view()
c1.compare(c2)
        
     