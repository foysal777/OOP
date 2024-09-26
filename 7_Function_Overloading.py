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