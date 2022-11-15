# Subscribe to https://www.youtube.com/channel/UCdx1l5V8xQjHHsnhNr2dWLg lol

from PIL import Image  
from pytesseract import pytesseract  
from pynput .keyboard import Key ,Controller  
import time  
import pyautogui  
from pynput .mouse import Listener  
###############
path_to_tesseract =r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe" #put your tesseract location here
###############
pytesseract .tesseract_cmd =path_to_tesseract  
def shit():
    OOOO000O0OO00000O =pyautogui .screenshot (region =(on_click .rx ,on_click .ry ,abs (on_click .rx -on_click .rx2 ),abs (on_click .ry -on_click .ry2 ))) 
    OOOO000O0OO00000O .save (r"text.png") 
    OO000OOOOOO0O0O00 =Image .open (r"text.png") 
    OO00O0O0OOO0O000O =pytesseract .image_to_string (OO000OOOOOO0O0O00 ) 
    OO00000O0OOOOOOO0 =Controller () 
    def OO0O00O0OO000O00O (O00O0O0O000OOOO0O ): 
        return [O00O00O0OOOO00O0O for O00O00O0OOOO00O0O in O00O0O0O000OOOO0O ] 
        time .sleep (3 ) 
    for O000OOO0O000OO000 in OO0O00O0OO000O00O (OO00O0O0OOO0O000O ): 
        OO00000O0OOOOOOO0 .type (O000OOO0O000OO000 ) 
        time .sleep (.03 ) #change to change speed
def on_click (OO0OO0O00OOO000O0 ,O0OO0O000OO000O00 ,OOO0O0OO0OOOOOO00 ,O00OOOO0O00OO0O00 ): 
    print (OO0OO0O00OOO000O0 ,O0OO0O000OO000O00 ) 
    if O00OOOO0O00OO0O00 ==True : 
        on_click .rx =OO0OO0O00OOO000O0  
        on_click .ry =O0OO0O000OO000O00  
    else : 
        on_click .rx2 =OO0OO0O00OOO000O0  
        on_click .ry2 =O0OO0O000OO000O00  
        listener .stop () 
with Listener (on_click =on_click )as listener : 
    listener.join () 
shit ()
