from abc import ABC, abstractmethod

class Product(ABC):

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def calculate_tax(self):...

class Electronics(Product):
    def __init__(self, name, price, warranty):
        self.name = name
        self.price = price
        self.warranty = warranty
        
    def calculate_tax(self):
        return self.price * 0.14  

class Clothing(Product) : 
    
    def __init__(self, name, price, size):
        self.name = name
        self.price = price
        self.size= size
    def calculate_tax(self):
        return self.price * 0.10
    
class Books(Product):
    
    def __init__(self, name, price, pages):
        self.name = name
        self.price = price
        self.pages= pages
    def calculate_tax(self):
        return self.price * 0.05
    
class customer:
    def __init__(self,name,cridet_info):
        
        self.name=name
        self.__cridet_inf=cridet_info 
        
    def pay(self):
        print("Payment done successfully")
        
        
elec = Electronics(name="fahd", price=100, warranty="tv")
clo = Clothing(name="ahmed", price=1000, size="xxl")
boo = Books(name="mohamed", price=200, pages=400)

print(elec.calculate_tax())
print(clo.calculate_tax())
print(boo.calculate_tax())

cust1 = customer(name="radwan", cridet_info=123456789)
cust1.pay()
