from mss import mss
import ctypes
import time

# Name your screenshot and save it where the script is
with mss() as sct:
    newname=input("Insert Screenshot Name: ")
    newname=newname+".png"
    #minimizes the cmd and after 1sec takes the screenshot
    ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 6 )
    time.sleep(1)
    sct.shot(output=newname)
