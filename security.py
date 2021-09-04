import getpass
import cv2
import datetime
import os
import random
import pymsgbox
import time
import tkinter
from PIL import ImageTk, Image
#ToDo:
#modules -> token,chatid,location,user,telegram url,file name:
import requests
TOKEN = '<Telegram token>'
CHAT_ID = '<Telegram chat id>'
#password importing
h = open('<Your file location>', 'r')
content = h.readlines()
key = ''.join(str(e) for e in content)
count = 4 # number of password attempts
checkuser = getpass.getuser()# Cheks user who Logged in
#alert message sending part to admin through telegram
def send_message(msg):
    payload = {
        'chat_id': CHAT_ID,
        'text'   :msg,
        'parse_mode': 'HTML'
    }
    return requests.post('https://api.telegram.org/bot{tok}/sendMessage'.format(tok=TOKEN),
                         data=payload).content
#Sending image to telegram bot
def sendImage(pat):
    url = "https://api.telegram.org/bot1211941964:AAGDfH8ejTABFgKBCeAtDeFPtg-7MHzcOjw/sendPhoto"
    files = {'photo': open('{}'.format(pat), 'rb')}
    data = {'chat_id' : "1150055270"}
    r= requests.post(url, files=files, data=data)
    #print(r.status_code, r.reason, r.content)

#Checking the user who log in
if checkuser == 'srira':

    current_time = datetime.datetime.now() # import date and time
    date = str(current_time)[:10] #date
    time_current = str(current_time)[10:19] #time
    send_message("Alert From Your PC , Someone Loged In ⚠ TIME ={}".format(time_current))

    camera = cv2.VideoCapture(0) #capture picture
    #Number of frames to capture
    for i in range(1):
        a = random.randint(1,99999999999999999999999999999999999999)# generate randome value for the image file
        return_value, image = camera.read()
        path = 'D:\System Security Project\captured pictures' # location where image should be saved
        cv2.imwrite(os.path.join(path , str(a) +'.jpg'), image ) # save the image captured



    del(camera)
    sendImage('D:\System Security Project\captured pictures\{}.jpg'.format(str(a)))
   #Writing The Obtained Details in a file
    f = open('Login_Details.txt', 'a')
    f.write("\t\tLOGIN DETAILS   {}".format(date) + '\n')
    f.write("_________________________________________________" + '\n')
    f.write("Login Date (yyyy-MM-DD):\t{}".format(date) + '\n')
    f.write("Login Time(24 HRS) :\t\t{}".format(time_current) + '\n')
    f.write("Logged in as :\t\t\t{}".format(checkuser) + '\n')
    f.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + '\n')
    f.close()
    # Alert User Interface
    pymsgbox.alert('This is the second step verification ! \n Your mouse is disabled \n Please use your keyboard',
                   'SECURITY ALERT ⚠️', timeout=3000)
    #password collecting infinite loop

    while count <= 4:
        response = pymsgbox.password("Enter the password ↓{} out of 4 ⁉️ 👀".format(count),
                                     "You Loose Chance Every 10 Seconds...", timeout=10000)

        if response == key: #password check area
            pymsgbox.alert("Access Granted 😊",timeout=2000)
            break



        else:
            count -= 1 # reduce the changes
            if count == 0:
                send_message("Unauthorized Login System ShutDown......🤐")

                pymsgbox.alert("Access Denied 🤬 🖕 \n You are not the system admin \nThis system will get locked and shutdowned soon....",timeout=2000)
                root = tkinter.Tk()

                img = ImageTk.PhotoImage(Image.open("D:\System Security Project\emojiimages\DENY.jpg"))
                panel = tkinter.Label(root,image=img)
                panel.pack(side="bottom", fill="both",
                           expand="yes")

                time.sleep(3)
                #Shutdown after 5 seconds
                os.system("shutdown /s /t 1")
                #


                root.mainloop()
                break

