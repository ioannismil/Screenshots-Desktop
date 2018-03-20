from mss import mss
import ctypes
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import getpass

# Name your screenshot and save it where the script is
with mss() as sct:
    newname=input("Insert Screenshot Name: ")
    newname=newname+".png"
    #minimizes the cmd and after 1sec takes the screenshot
    ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 6 )
    time.sleep(1)
    sct.shot(output=newname)
    ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 1 )
email_user = input("Enter your email address: ")
email_password = getpass.getpass("Enter your password: ")
email_send = input("Enter recipient's email: ")

subject = 'subject'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = 'Your Desktop Screenshot'
msg.attach(MIMEText(body,'plain'))

filename=newname
attachment  =open(filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)

msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,email_password)


server.sendmail(email_user,email_send,text)
server.quit()
