# Subscribe to https://www.youtube.com/channel/UCdx1l5V8xQjHHsnhNr2dWLg lol
import cv2
from PIL import Image
from pytesseract import pytesseract
from pynput.keyboard import Key, Controller
import time
import pyautogui
from pynput.mouse import Listener
path_to_tesseract = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe" #Set your tesseract location here
pytesseract.tesseract_cmd = path_to_tesseract
def shit():
    ss = pyautogui.screenshot(region=(on_click.rx, on_click.ry, abs(on_click.rx - on_click.rx2), abs(on_click.ry - on_click.ry2)))
    ss.save(r"text.png")
    img = cv2.imread('text.png', cv2.IMREAD_GRAYSCALE)
    text = pytesseract.image_to_string(img)
    newtext = text.replace('|', 'I')
    newtext = newtext.replace('\n', ' ')
    
    keyboard = Controller()
    def split (words):
        return[char for char in words]
        time.sleep(3)
    for i in split(newtext):
        keyboard.type(i)
        time.sleep(.07) #change to change speed
def on_click(x, y, button, pressed):
    print(x, y)
    if pressed == True:
        on_click.rx = x
        on_click.ry = y
    else:
        on_click.rx2 = x
        on_click.ry2 = y
        listener.stop()
with Listener(on_click = on_click) as listener:
    listener.join()
    
shit()