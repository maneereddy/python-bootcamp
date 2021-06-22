#banking concept
class account:
    def __init__(self,name,address):
        self.name = name
        self.address = address
    def printname(self):
         print(self.name,self.address)
class bank(account):
    def __init__(self,name,address,acnumber):
     super().__init__(name,address)
     self.number = acnumber
    def welcome(self):
        print("welcome",self.name,"to your account number",self.number)

a = bank("manee","hyd",1234)
a.welcome()

#Ecommerce concept
class account:
    def __init__(self,name,address):
        self.name = name
        self.address = address
    def printname(self):
         print(self.name,self.address)
class flipcart(account):
    def __init__(self,name,address,acnumber):
     super().__init__(name,address)
     self.number = acnumber
    def welcome(self):
        print("welcome",self.name,"to your order id is ",self.number)

a = flipcart("ram","chennai","ID321")
a.welcome()
