class Data:
    def __init__(self , x) -> None:
        self.x = x
    # Adding two object 
    def __add__(self, others):
         return self.x + others.x
     
    def __gt__(self, others):
         return self.x + others.x
    
d1 = Data(20)
d2 = Data(50)

print(d1 + d2 )
print(d1 > d2 )