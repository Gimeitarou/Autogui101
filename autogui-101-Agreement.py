from sys import exit
import pyautogui as pau
import pyperclip
import tkinter as tk
import tkinter.messagebox as messagebox
import time
import os

tk.Tk().withdraw()
TorF = messagebox.askokcancel('<Agreement>', 'This code will automatically download a picture, and set the picture as your wallpaper.\nDo you accept that?')
if TorF == False:
    exit()

DownloadCmd = 'powershell Invoke-WebRequest -Uri gahag.net/img/201608/26s/gahag-0119154009-1.jpg -OutFile Downloads/Lake.jpg'
OpenCmd = 'C:/Users/%username%/Downloads/Lake.jpg'

#download a pic on DL-dir
pyperclip.copy(DownloadCmd)
pau.hotkey('win','r')
time.sleep(1)
pau.hotkey('ctrl','v')
pau.press('enter')
time.sleep(4)

#open the pic
pyperclip.copy(OpenCmd)
pau.hotkey('win','r')
time.sleep(1)
pau.hotkey('ctrl','v')
pau.press('enter')
time.sleep(2)

#set it as wallpaper
pau.hotkey('ctrl','b')
time.sleep(2)

#close the pic
pau.hotkey('alt','f4')

os.remove('Downloads/Lake.png')