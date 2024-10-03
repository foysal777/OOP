from multipledispatch import dispatch
class Example:
    def greet(self, name="Guest", greeting="Hello"):
        print(f"{greeting}, {name}!")


ex = Example()
ex.greet() 
ex.greet("John") 
ex.greet("John", "Good morning") 






class Calculator:
    def sum(self,num1,num2,num3=None):
       if num3 is None:
           return num1+num2
       return num1+num2+num3
    
    
cal = Calculator()
print(cal.sum(1,2,3))
print(cal.sum(1,2))


class Cal():
    
    def mul(self, *num):
        sum = 1
        for x in num:
            sum = sum*x 
        print(sum)
c = Cal()
c.mul(4)
c.mul(64,2)


class Calculator:
    
    @dispatch(int , int)
    def product(self, a , b):
        print(a*b)
        
    @dispatch(int , int , int )
    def product(self, a , b  , c):
        print(a*b*c)
        
c = Calculator()
c.product(30, 3)
c.product(30, 3 , 2)