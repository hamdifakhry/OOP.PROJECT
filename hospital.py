from abc import ABC, abstractmethod
class person(ABC) :
    def __init__(self,name,id):
        
        self.name=name
        self.id=id
    @abstractmethod   
    def details_get (self): ...
    
    
    @abstractmethod 
    def work(self): ...
    
class docter(person):
    
    def __init__(self, name, id, specialization):
        self.name = name
        self.id = id
        self.specialization = specialization
    def details_get (self): 
        print("Doctor Name:", self.name)
        print("ID:", self.id)
        print("Specialization:", self.specialization) 
        
    def work(self):
        print ("huart docter ") 
        
class nurse (person):
    
    def __init__(self, name, id, shift_time):
        self.name = name
        self.id = id
        self.shift_time = shift_time

    def details_get (self):
        print("Nurse Name:", self.name)
        print("ID:", self.id)
        print("Shift Time:", self.shift_time)

    def work(self):
        print("Nurse is taking care of patients")
        
class Patient:

    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.__balance = 0
        
    def add_bill(self, amount):
        self.__balance += amount
        print("Bill added. Current balance:", self.__balance)
    
    def pay_bill(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Payment successful. Remaining balance:", self.__balance)
        else:
            print("Not enough balance")
            
doc1=docter(name="fhahd",id=123456,specialization="fit")
nu1=nurse(name="saad",id=432345,shift_time="night")
pat1=Patient(name="mourd",id=7654321)
doc1.details_get()
doc1.work()
nu1.details_get()
nu1.work()
pat1.add_bill(100)
pat1.pay_bill(50)
