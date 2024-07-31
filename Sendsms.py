from tkinter import *
import requests
import FirebaseAdmin as firebase
#C4qBmsb9OviwGFxnE6RDVIp7Sl8hoQJPu1ajZyLYUzTeAfHtk5q25KRLsw8OiIoJMzgZ6YvUTFtla4QN(9836176456)
#T97LbyB8IR2HeZ6OcjiDhpqPaUNwEVWFrn45CStAoJfXk0GMYuvMWIDOyKTVx1Flj0gLimrq5UZ8JC4d(6291020762)
#6Kq9cw5Rk2b8J85oBQWM3I1v8I8uhObp84syadyQsm4zxSvEc9WUUETyWrqq(7003300190)

def send():
    #sfile=open("securitycode.txt","r")
    #security_code=sfile.read()
    #print(security_code)
    phone_num=sendwinentry1.get()
    pic_id = sendwinentry2.get()
    firebase.present = firebase.checkImgId(pic_id)
    if(firebase.present == True):
        #print('image id already available in the database. Please try another image id')
        sendmes=Tk()
        sendmes.configure(background='gray14')
        sendmes.resizable(False,False)
        sendmes.title("Messa")
        sendmes.geometry('450x250')

        sendmes_frame=Frame(sendmes,width=240,height=240, bg="gray14" ,highlightbackground="gray37",highlightthickness=3)
        sendmes_frame.place(relx=0.5,rely=0.5,anchor='center')

        sendmes_label1=Label(sendmes_frame,text="Your Entered Image Id is Allready Exist...",bg="gray14",fg="white",font="verdana 8 bold")
        sendmes_label1.place(relx=0.5,rely=0.4,anchor='center')

        sendmes_label2=Label(sendmes_frame,text="Please Selact Another One",bg="gray14",fg="white",font="verdana 8 bold")
        sendmes_label2.place(relx=0.5,rely=0.45,anchor='center')

    else:
        print(phone_num)
        print(pic_id)
        with open('phone_no.txt', 'w') as Pass:
            Pass.write(phone_num)
        with open('image_id.txt', 'w') as Pass:
            Pass.write(pic_id)
        pfile=open("securitycode.txt","r")
        scode=pfile.read()
        print(scode)
        url = "https://www.fast2sms.com/dev/bulkV2"
        var=123654

        querystring = {"authorization":"6Kq9cw5Rk2b8J85oBQWM3I1v8I8uhObp84syadyQsm4zxSvEc9WUUETyWrqq",
                        "message":"Your Security code is: "+scode+" and Photo Id is : "+pic_id,
                        "language":"english","route":"q",
                        "numbers":phone_num}

        headers = {
        'cache-control': "no-cache"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        print(response.text)
        sendwin.destroy()
        meswin=Tk()
        meswin.configure(background='gray14')
        meswin.resizable(False,False)
        meswin.title("Message")
        meswin.geometry('400x200')

        meswin_frame=Frame(meswin,width=390,height=190, bg="gray14" ,highlightbackground="gray37",highlightthickness=3)
        meswin_frame.place(relx=0.5,rely=0.5,anchor='center')
        meswin_label=Label(meswin_frame,text="OTP has been sent Successfully",bg="gray14",fg="white",font="verdana 8 bold")
        meswin_label.place(relx=0.5,rely=0.5,anchor='center')
        meswin.mainloop()


        return True

sendwin=Tk()
sendwin.configure(background='gray14')
sendwin.resizable(False,False)
sendwin.title("Send Sms")
sendwin.geometry('400x250')

sendwin_frame=Frame(sendwin,width=390,height=240, bg="gray14" ,highlightbackground="gray37",highlightthickness=3)
sendwin_frame.place(relx=0.5,rely=0.5,anchor='center')

sendwin_label1=Label(sendwin_frame,text="Enter The Phone Number",bg="gray14",fg="white",font="verdana 8 bold")
sendwin_label1.place(relx=0.5,rely=0.2,anchor='center')

sendwin_label2=Label(sendwin_frame,text="Enter The Image Id",bg="gray14",fg="white",font="verdana 8 bold")
sendwin_label2.place(relx=0.5,rely=0.45,anchor='center')

sendwinentry1=Entry(sendwin_frame,width=35, bg="gray7", fg="white", borderwidth=4)
sendwinentry1.place(relx=0.5,rely=0.3,anchor='center')

sendwinentry2=Entry(sendwin_frame,width=35, bg="gray7", fg="white", borderwidth=4)
sendwinentry2.place(relx=0.5,rely=0.55,anchor='center')

sendwin_button=Button(sendwin_frame,text="Send",bg="dark slate gray",fg="white",padx=12,command=send)
sendwin_button.place(relx=0.5,rely=0.8,anchor='center')


mainloop()

