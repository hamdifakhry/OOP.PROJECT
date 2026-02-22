from abc import ABCMeta,abstractmethod
class human(metaclass=ABCMeta):
    def __init__(self , name):
        self.name=name
        
    @abstractmethod    
    def talk(self): ...
        
       
    @abstractmethod    
    def walk(self): ...
    
    # @abstractmethod 
    def hello(self):
        print("helloooo")
        

class person(human):
    def walk(self):
        print("walk 2")
    def talk(self):
        print("kfkff")
x=person(name="hamdi")
           
x.talk()
x.walk()

class man(human): 
    def talk(self):
        print("jfkkff")
    def walk(self):
        print("jfkkffffffffff")

x=man( name="kkdk")
x.walk()
x.talk()

class hamdi(human):

    def talk(self):
        print("jfkkff")
    def walk(self):
        print("jfkkffffffffff")

x=hamdi(name="hamdi")