class Computer:
    def __init__(self , name , brand ) -> None:
        
        self.name = name
        self._brand = brand
        self.__password = "34-65-95"

    def showName(self):
        print(f"The pc name is {self.name} and Brand is {self._brand}")


    
    def _showBrand(self):
        print(f"Brand is {self._brand}")
        
        
    def __showPassword(self):
        print(f"This is my Password : {self.__password}")


    def get_password(self):
        return self.__password
    
    
c = Computer('ViewSonic' , 'Dell')
c.showName()
c._showBrand()
print(c.get_password())
c._Computer__showPassword()  # we can't access directly bcz it was private method 




