class human :
    tall = int (input("your tall is : " ))
    weight = int (input("your weight is :" ))
    
    def __init__(self , name):
        self.name =name
    def print_info(self):
        print("your tall is :",self.tall )
        print("your weight is :",self.weight )
        print("yourname is :" , self.name)
     
   
huma=human( "hamdii")
huma.print_info()

