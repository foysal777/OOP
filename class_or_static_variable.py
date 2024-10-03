class Player:
    
    total_run =0 ;  #class variable can not access self & no need to call by the object
    
    def __init__(self , run) -> None:
        self.run = run    #instance variable 
      
        
    def hit_four(self):
        self.run += 4
        Player.total_run += 4  # access by class name 
        
    def hit_six(self):
        self.run +=6
        Player.total_run += 6
        
    def display(self):
        print("The run is  : " ,self.run )
    
        

habi = Player(0)
habi.hit_four()
habi.hit_four()
habi.display()



saju = Player(0)
saju.hit_six()
saju.hit_six()
saju.display()

print("Total run is : " ,Player.total_run)