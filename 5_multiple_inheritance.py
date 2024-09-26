
# Multiple Inheritance 

class j:
    def displayj(self):
        print("i am j method")
    
class k:
    def displayk(self):
        print("i am k method")
class L(j , k):
    
    def __init__(self) -> None:
        super().__init__()
    
    def displayL(self):
        print("I am L method")
        
l = L()
l.displayj()
l.displayk()
l.displayL()































class person:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
    def personalInfo(self):
        print(self.name," - ",self.age)


class company:
    def __init__(self,cname,cloc) -> None:
        self.cloc = cloc
        self.cname = cname
    def companyInfo(self):
        print(self.cname," - ",self.cloc)


class employee(person,company):
    def __init__(self, name, age,cname,cloc) -> None:
        person.__init__(self,name,age)
        company.__init__(self,cname,cloc)

obj = employee("sayed",24,"Google","USA")
obj.companyInfo()
obj.personalInfo()

print(employee.mro()) #method resolution order
