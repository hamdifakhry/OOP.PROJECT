name= input("inter your name: ")

class human :

    def __init__(self,name):
        self.name=name
    def talk (self ):
     
        print("i aam talking" ,self.name)
class person(human) :
    def walk (self):
        print("iam walkine",self.name)  
# x=person(name)
# x.talk()
# x.walk()
class man(person) : 
    def talk(self):
        # return super().talk()
        print("h am man and ham tolking")

x=man(name)
x.walk()
x.talk()