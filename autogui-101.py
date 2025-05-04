import pyautogui as pau
import pyperclip
import time
import os

def autogui_101(Pic_URL):

    #cmddef    
    DownloadCmd = f'powershell Invoke-WebRequest -Uri {Pic_URL} -OutFile Downloads/Pic.jpg'
    OpenCmd = 'C:/Users/%username%/Downloads/Pic.jpg'

    #download a pic on DL-dir
    pyperclip.copy(DownloadCmd)
    pau.hotkey('win','r')
    time.sleep(1)
    pau.hotkey('ctrl','v')
    pau.press('enter')
    time.sleep(10)

    #open the pic
    pyperclip.copy(OpenCmd)
    pau.hotkey('win','r')
    time.sleep(1)
    pau.hotkey('ctrl','v')
    pau.press('enter')
    time.sleep(2.5)

    #set it as wallpaper
    pau.hotkey('ctrl','b')
    time.sleep(2)

    #close the pic
    pau.hotkey('alt','f4')

    return 0

ExURL_Lake = 'the-public-domain-review.imgix.net/collections/campi-phlegraei/campi-phlegraei-9.jpg'

autogui_101(ExURL_Lake)