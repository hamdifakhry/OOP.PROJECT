

class bank :


    def __init__(self,name,age,countr,monay):
        self.name =name
        self.age =age
        self.countr=countr
        self.monay=monay
     
        
    def witdthdraw(self,price ) :
        

        if price <  self.monay :
            self.monay-=price
            print ("sucssesfuly" ,self.monay )
        else :
            print("rejected")
            
    def deposit(self,price) :
         self.monay+=price 
         
         if price > 0 :
            self.monay+=price
            print("sucsess",self.monay)   
         else :
            
             print("rejected")
            
    def finall(self):
        
        print("your name is " ,self.name)
        print("your age is " ,self.age)
        print("your country is " ,self.countr)
        print("your sallary is " ,self.monay)
x=bank(name="hamdi",age="20",countr="egypt",monay=1000)
x.finall()
x.witdthdraw(500)
x.deposit(100)
x.finall()