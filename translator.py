
from googletrans import Translator , LANGUAGES
trans=input("writeing evre thing :")
print( "chose any languch",LANGUAGES)
transcode= input("inter the languch to translat:")


class tran :
    
    def __init__(self , trans,transcode):
        self.trans=trans
        self.transcode=transcode
    def start (self):
        
        translator=Translator()


        result =  translator.translate(self.trans, dest=self.transcode)
        final=result.text
        print(final ) 


x=tran(trans,transcode)
x.start()