
down=input("inter your video link :" )
from pytubefix import YouTube
from pytubefix.cli import on_progress
class you_t :
    
     def __init__(self,down):
         
         self.down=down
     def tu_be(self):
    
        yt = YouTube(down, on_progress_callback=on_progress)
        print(yt.title)

        ys = yt.streams.get_highest_resolution()
        ys.download() 
            
    
x=you_t(down)
x.tu_be()