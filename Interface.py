from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog, ttk
from captcha.image import ImageCaptcha
import time, random, os, subprocess, Send_Email
import FirebaseAdmin as firebase


global encryptbutton_entry_rec
global encryptbutton_entry_recch

splash=Tk()
splash.title("Project")
splash.resizable(False,False)
splash.configure(background='gray14')
splash.geometry("590x200")

splash_frame=Frame(splash,width=580,height=190, bg="gray14" ,highlightbackground="gray37",highlightthickness=3)
splash_frame.place(relx=0.5,rely=0.5,anchor='center')


def encryptWindow():
    encrypt_window=Tk()
    encrypt_window.title("Encryption")
    encrypt_window.resizable(False,False)
    encrypt_window.configure(background='gray14')
    encrypt_window.geometry("1350x680")

    encrypt_mainframe=Frame(encrypt_window,width=1340,height=670, bg="gray14" ,highlightbackground="gray37",highlightthickness=3)
    encrypt_mainframe.place(relx=0.5,rely=0.5,anchor='center')

    def show():

        x = browseImage()
        img = Image.open(x)
        img.save('input/selected_img.png')
        img = img.resize((578, 540), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        encrypt_label5=Label(encrypt_subframe1,width=578,height=540,bg="black",image = img)
        encrypt_label5.image = img
        encrypt_label5.place(relx=0.25,rely=0.51,anchor='center')
        encrypt_label7=Label(encrypt_subframe1,text="Browsed Image",bg="black",fg="white",font="verdana 8 bold")
        encrypt_label7.place(relx=0.25,rely=0.03,anchor='center')


    def browseImage():
        filename = filedialog.askopenfilename(title ='Open')
        return filename


    def encryptImage():
        encryptbutton_entry_rec=encryptbutton_entry.get()
        encryptbutton_entry_recch=encryptbutton_entrych.get()
        print(encryptbutton_entry_rec)
        print(encryptbutton_entry_recch)

        if(encryptbutton_entry_rec==encryptbutton_entry_recch):
            print("Password Matched")
            with open('password.txt', 'w') as Pass:
                Pass.write(encryptbutton_entry_rec)

            subprocess.call(['python', 'Password_Genarator.py'])
            subprocess.call(['python', 'encrypt.py'])#Change req (python3)

            encrypt_label8=Label(encrypt_subframe1,text="Encrypted Image",bg="black",fg="white",font="verdana 8 bold")
            encrypt_label8.place(relx=0.75,rely=0.03,anchor='center')
            img = Image.open('encrypted_images/encrypted_result.png')
            img = img.resize((578, 540), Image.ANTIALIAS)

            img = ImageTk.PhotoImage(img)

            encrypt_label6=Label(encrypt_subframe1,width=578,height=540 ,bg="black",image = img)
            encrypt_label6.image = img
            encrypt_label6.place(relx=0.75,rely=0.51,anchor='center')

            encryptbutton_sendotp=Button(encrypt_subframe3,text="Send OTP",width=10, bg="dark slate gray",fg="white",padx=10,command=otpsend)
            encryptbutton_sendotp.place(relx=0.5,rely=0.8,anchor='center')



        else:
            win=Tk()
            win.configure(background='gray14')
            win.resizable(False,False)
            win.title("Message")
            win.geometry('400x200')

            win_frame=Frame(win,width=390,height=190, bg="gray14" ,highlightbackground="gray37",highlightthickness=3)
            win_frame.place(relx=0.5,rely=0.5,anchor='center')
            win_label=Label(win_frame,text="Password not Matched...Reset the Password",bg="gray14",fg="white",font="verdana 8 bold")
            win_label.place(relx=0.5,rely=0.5,anchor='center')

    def otpsend():
        subprocess.call(['python', 'Sendsms.py'])
        print('OTP sent')
        firebase.pushData()
        return True

    def save():
        file=filedialog.asksaveasfile(initialdir="\c",filetypes=[("Text file",".txt"),("All file",".*"),("Jpeg file",".jpg"),("Png file",".png")])
        if file:
            abs_path = os.path.abspath(file.name)
            out = Image.open('encrypted_images/encrypted_result.png')
            out.save(abs_path)

    def back():
        encrypt_window.destroy()
        mainWindow()

    def exit():
        encrypt_window.destroy()

    def reset():
        encryptbutton_entry.delete(0,"end")
        encryptbutton_entrych.delete(0,"end")

    def go():
        def send():
            myname=emailentry1.get()
            myemail=emailentry2.get()
            mypassword=emailentry3.get()
            receiveremail=emailentry4.get()
            subject=emailentry5.get()
            with open('gmail_id.txt', 'w') as Pass:
                Pass.write(receiveremail)
            Send_Email.send_gmail(myname,myemail,receiveremail,mypassword,subject)
            print(myname)
            print(myemail)
            print(receiveremail)
            print(subject)
        var=clicked.get()
        email_window=Tk()
        email_window.configure(background='gray14')
        email_window.title("Gmail")
        email_window.geometry('600x400')

        email_frame=Frame(email_window,width=590,height=390, bg="gray14" ,highlightbackground="gray37",highlightthickness=3)
        email_frame.place(relx=0.5,rely=0.5,anchor='center')

        emaillabel_1=Label(email_frame,text="Gmail Details",width=120,bg="gray37",fg="white",font="verdana 14 bold")
        emaillabel_1.place(relx=0.5,rely=0.03,anchor='center')


        emaillabel_2=Label(email_frame,text="Enter Your Name",bg="gray14",fg="white",font="verdana 10 bold")
        emaillabel_2.place(relx=0.2,rely=0.2,anchor='center')

        emaillabel_3=Label(email_frame,text="Enter Your Mail Id",bg="gray14",fg="white",font="verdana 10 bold")
        emaillabel_3.place(relx=0.2,rely=0.3,anchor='center')

        emaillabel_4=Label(email_frame,text="Enter Your Password",bg="gray14",fg="white",font="verdana 10 bold")
        emaillabel_4.place(relx=0.2,rely=0.4,anchor='center')

        emaillabel_5=Label(email_frame,text="Enter Receipent Mail Id",bg="gray14",fg="white",font="verdana 10 bold")
        emaillabel_5.place(relx=0.2,rely=0.5,anchor='center')

        emaillabel_6=Label(email_frame,text="Enter Subject",bg="gray14",fg="white",font="verdana 10 bold")
        emaillabel_6.place(relx=0.2,rely=0.6,anchor='center')

        #emaillabel_7=Label(email_frame,text="Enter Body of the Mail",bg="gray14",fg="white",font="verdana 10 bold")
        #emaillabel_7.place(relx=0.2,rely=0.7,anchor='center')

        emailentry1=Entry(email_frame,width=30, bg="gray7", fg="white", borderwidth=4)
        emailentry1.place(relx=0.7,rely=0.2,anchor='center')

        emailentry2=Entry(email_frame,width=35, bg="gray7", fg="white", borderwidth=4)
        emailentry2.place(relx=0.728,rely=0.3,anchor='center')

        emailentry3=Entry(email_frame,width=35, bg="gray7", fg="white", borderwidth=4)
        emailentry3.config(show="*")
        emailentry3.place(relx=0.728,rely=0.4,anchor='center')

        emailentry4=Entry(email_frame,width=35, bg="gray7", fg="white", borderwidth=4)
        emailentry4.place(relx=0.728,rely=0.5,anchor='center')

        emailentry5=Entry(email_frame,width=35, bg="gray7", fg="white", borderwidth=4)
        emailentry5.place(relx=0.728,rely=0.6,anchor='center')

        #emailentry6=Entry(email_frame,width=35, bg="gray7", fg="white", borderwidth=4)
        #emailentry6.place(relx=0.728,rely=0.7,anchor='center')

        email_button=Button(email_frame,text="Send",bg="dark slate gray",fg="white",padx=12,command=send)
        email_button.place(relx=0.5,rely=0.85,anchor='center')



        print(var)


#---------------------------------------------------------------------------------------------------------------------------------------#

    encrypt_subframe1=Frame(encrypt_mainframe,width=1190,height=600, bg="black" ,highlightbackground="gray14",highlightthickness=3)
    encrypt_subframe1.place(relx=0.447,rely=0.455,anchor='center')

#---------------------------------------------------------------------------------------------------------------------------------------#

    encrypt_subframe2=Frame(encrypt_mainframe,width=1190,height=65, bg="gray14" ,highlightbackground="gray37",highlightthickness=3)
    encrypt_subframe2.place(relx=0.447,rely=0.948,anchor='center')

    encryptbutton_browse=Button(encrypt_subframe2,text="Browse Image",width=10 ,bg="dark slate gray",fg="white",padx=10,command=show)
    encryptbutton_browse.place(relx=0.1,rely=0.5,anchor='center')

    encryptbutton_encrypt=Button(encrypt_subframe2,text="Encrypt Image",width=10, bg="dark slate gray",fg="white",padx=10,command=encryptImage)
    encryptbutton_encrypt.place(relx=0.3,rely=0.5,anchor='center')

    encryptbutton_back=Button(encrypt_subframe2,text="Back",width=10, bg="dark slate gray",fg="white",padx=10,command=back)
    encryptbutton_back.place(relx=0.5,rely=0.5,anchor='center')

    encryptbutton_exit=Button(encrypt_subframe2,text="Exit",width=10, bg="dark slate gray",fg="white",padx=10,command=exit)
    encryptbutton_exit.place(relx=0.7,rely=0.5,anchor='center')

    encryptbutton_save=Button(encrypt_subframe2,text="Save",width=10, bg="dark slate gray",fg="white",padx=10,command=save)
    encryptbutton_save.place(relx=0.9,rely=0.5,anchor='center')


#--------------------------------------------------------------------------------------------------------------------------------------#

    encrypt_subframe3=Frame(encrypt_window,width=139,height=660, bg="gray14" ,highlightbackground="gray37",highlightthickness=3)
    encrypt_subframe3.place(relx=0.94,rely=0.5,anchor='center')

    encrypt_label1=Label(encrypt_subframe3,text="Set a Strong",width=10, bg="gray14",fg="white",padx=10,font="verdana 8 bold")
    encrypt_label1.place(relx=0.5,rely=0.05,anchor='center')

    encrypt_label2=Label(encrypt_subframe3,text="Password",width=10, bg="gray14",fg="white",padx=10,font="verdana 8 bold")
    encrypt_label2.place(relx=0.5,rely=0.08,anchor='center')


    encryptbutton_entry=Entry(encrypt_subframe3,width=18, bg="gray7", fg="white", borderwidth=4)
    encryptbutton_entry.config(show="*")
    encryptbutton_entry.insert(0,"Set Password")
    #encryptbutton_entry_rec=encryptbutton_entry.get()
    encryptbutton_entry.place(relx=0.5,rely=0.113,anchor='center')

    encrypt_label3=Label(encrypt_subframe3,text="Confirm the",width=10, bg="gray14",fg="white",padx=10,font="verdana 8 bold")
    encrypt_label3.place(relx=0.5,rely=0.18,anchor='center')
    encrypt_label4=Label(encrypt_subframe3,text="Password",width=10, bg="gray14",fg="white",padx=10,font="verdana 8 bold")
    encrypt_label4.place(relx=0.5,rely=0.205,anchor='center')


    encryptbutton_entrych=Entry(encrypt_subframe3,width=18, bg="gray7", fg="white", borderwidth=4)
    encryptbutton_entrych.config(show="*")
    encryptbutton_entrych.place(relx=0.5,rely=0.238,anchor='center')


    encryptbutton_reset=Button(encrypt_subframe3,text="Reset",width=10, bg="dark slate gray",fg="white",padx=10,command=reset)
    encryptbutton_reset.place(relx=0.5,rely=0.3,anchor='center')


    clicked=StringVar()
    clicked.set("Send Via")
    encryptbutton_drop=OptionMenu(encrypt_subframe3,clicked,"Gmail")
    encryptbutton_drop.config(bg="gray7",fg="white",borderwidth=1,highlightbackground = "gray37", highlightcolor= "gray37")
    encryptbutton_drop["menu"].config(bg="dark slate gray",fg="white")
    encryptbutton_drop.place(relx=0.5,rely=0.6,anchor='center')

    encryptbutton_sendgo=Button(encrypt_subframe3,text="Go",width=10, bg="dark slate gray",fg="white",padx=10,command=go)
    encryptbutton_sendgo.place(relx=0.5,rely=0.7,anchor='center')


    encrypt_window.mainloop()





def decryptWindow():
    decrypt_window=Tk()
    decrypt_window.title("Decryption")
    decrypt_window.resizable(False,False)
    decrypt_window.configure(background='gray14')
    decrypt_window.geometry("1350x680")


    decrypt_mainframe=Frame(decrypt_window,width=1340,height=670, bg="gray14" ,highlightbackground="gray37",highlightthickness=3)
    decrypt_mainframe.place(relx=0.5,rely=0.5,anchor='center')

    def browseImage():
        filename = filedialog.askopenfilename(title ='Open')
        return filename

    def show():
        x = browseImage()
        img = Image.open(x)
        img.save('encrypted_images\encrypted_result.png')
        img = img.resize((578, 540), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)

        decrypt_label5=Label(decrypt_subframe1,width=578,height=540,bg="black",image = img)
        decrypt_label5.image = img
        decrypt_label5.place(relx=0.25,rely=0.51,anchor='center')
        decrypt_label7=Label(decrypt_subframe1,text="Browsed Image",bg="black",fg="white",font="verdana 8 bold")
        decrypt_label7.place(relx=0.25,rely=0.03,anchor='center')


    def decrypt_Image():
        decrypt_password=decryptbutton_entry1.get()
        decrypt_imgid=decryptbutton_entry2.get()
        decrypt_otp=decryptbutton_entry3.get()
        print(decrypt_password)
        print(decrypt_imgid)
        print(decrypt_otp)

        firebase.present = firebase.fetchData(decrypt_imgid, decrypt_password, decrypt_otp)  # 8888888
        print(firebase.present)
        if (firebase.present == True):
            print("The Image Id, Password and OTP in decryption is matched")
            subprocess.call(['python', 'decrypt.py'])#change req (python)
            decrypt_label8 = Label(decrypt_subframe1, text="Decrypted Image", bg="black", fg="white",font="verdana 8 bold")
            decrypt_label8.place(relx=0.75, rely=0.03, anchor='center')
            img = Image.open('decrypted_images/decrypted_result.png')
            img = img.resize((578, 540), Image.ANTIALIAS)

            img = ImageTk.PhotoImage(img)

            decrypt_label6 = Label(decrypt_subframe1, width=578, height=540, bg="black", image=img)
            decrypt_label6.image = img
            decrypt_label6.place(relx=0.75, rely=0.51, anchor='center')

        if (firebase.present == False):
            windec=Tk()
            windec.configure(background='gray14')
            windec.resizable(False,False)
            windec.title("Message")
            windec.geometry('400x200')

            windec_frame=Frame(windec,width=390,height=190, bg="gray14" ,highlightbackground="gray37",highlightthickness=3)
            windec_frame.place(relx=0.5,rely=0.5,anchor='center')
            windec_label=Label(windec_frame,text="OTP not Matched...Reenter the OTP",bg="gray14",fg="white",font="verdana 8 bold")
            windec_label.place(relx=0.5,rely=0.5,anchor='center')

        if (firebase.present == 'password Not Matched'):
            windec = Tk()
            windec.configure(background='gray14')
            windec.resizable(False, False)
            windec.title("Message")
            windec.geometry('400x200')

            windec_frame = Frame(windec, width=390, height=190, bg="gray14", highlightbackground="gray37",
                                 highlightthickness=3)
            windec_frame.place(relx=0.5, rely=0.5, anchor='center')
            windec_label = Label(windec_frame, text="Password not Matched...Reenter the Password", bg="gray14", fg="white",
                                 font="verdana 8 bold")
            windec_label.place(relx=0.5, rely=0.5, anchor='center')

        if(firebase.present == 'imgId Not Matched'):
            windec = Tk()
            windec.configure(background='gray14')
            windec.resizable(False, False)
            windec.title("Message")
            windec.geometry('400x200')

            windec_frame = Frame(windec, width=390, height=190, bg="gray14", highlightbackground="gray37",
                                 highlightthickness=3)
            windec_frame.place(relx=0.5, rely=0.5, anchor='center')
            windec_label = Label(windec_frame, text="Image Id not Matched...Reenter the Image Id", bg="gray14", fg="white",
                                 font="verdana 8 bold")
            windec_label.place(relx=0.5, rely=0.5, anchor='center')

        return True

    def back():
        decrypt_window.destroy()
        mainWindow()


    def exit():
        decrypt_window.destroy()
    def save():
        file=filedialog.asksaveasfile(initialdir="\c",filetypes=[("Text file",".txt"),("All file",".*"),("Jpeg file",".jpg"),("Png file",".png")])
        if file:
            abs_path = os.path.abspath(file.name)
            out = Image.open("decrypted_images\decrypted_result.png")
            out.save(abs_path)
    def reset():
        decryptbutton_entry1.delete(0,"end")
        decryptbutton_entry2.delete(0,"end")
        decryptbutton_entry3.delete(0,"end")


    decrypt_subframe1=Frame(decrypt_mainframe,width=1190,height=600, bg="black" ,highlightbackground="gray37",highlightthickness=3)
    decrypt_subframe1.place(relx=0.447,rely=0.455,anchor='center')


#---------------------------------------------------------------------------------------------------------------------------------------#

    decrypt_subframe2=Frame(decrypt_mainframe,width=1190,height=65, bg="gray14" ,highlightbackground="gray37",highlightthickness=3)
    decrypt_subframe2.place(relx=0.447,rely=0.948,anchor='center')

    decryptbutton_browse=Button(decrypt_subframe2,text="Browse Image",width=10 ,bg="dark slate gray",fg="white",padx=10,command=show)
    decryptbutton_browse.place(relx=0.1,rely=0.5,anchor='center')

    decryptbutton_decrypt=Button(decrypt_subframe2,text="Decrypt Image",width=10, bg="dark slate gray",fg="white",padx=10,command=decrypt_Image)
    decryptbutton_decrypt.place(relx=0.3,rely=0.5,anchor='center')

    decryptbutton_back=Button(decrypt_subframe2,text="Back",width=10, bg="dark slate gray",fg="white",padx=10,command=back)
    decryptbutton_back.place(relx=0.5,rely=0.5,anchor='center')

    decryptbutton_exit=Button(decrypt_subframe2,text="Exit",width=10, bg="dark slate gray",fg="white",padx=10,command=exit)
    decryptbutton_exit.place(relx=0.7,rely=0.5,anchor='center')

    decryptbutton_save=Button(decrypt_subframe2,text="Save",width=10, bg="dark slate gray",fg="white",padx=10,command=save)
    decryptbutton_save.place(relx=0.9,rely=0.6,anchor='center')


#--------------------------------------------------------------------------------------------------------------------------------------#

    decrypt_subframe3=Frame(decrypt_window,width=139,height=660, bg="gray14" ,highlightbackground="gray37",highlightthickness=3)
    decrypt_subframe3.place(relx=0.94,rely=0.5,anchor='center')

    decrypt_label1=Label(decrypt_subframe3,text="Enter The",width=10, bg="gray14",fg="white",padx=10,font="verdana 8 bold")
    decrypt_label1.place(relx=0.5,rely=0.05,anchor='center')

    decrypt_label2=Label(decrypt_subframe3,text="Password",width=10, bg="gray14",fg="white",padx=10,font="verdana 8 bold")
    decrypt_label2.place(relx=0.5,rely=0.08,anchor='center')


    decryptbutton_entry1=Entry(decrypt_subframe3,width=18, bg="gray7", fg="white", borderwidth=4)
    decryptbutton_entry1.config(show="*")
    decryptbutton_entry1.insert(0,"Set Password")
    decryptbutton_entry1.place(relx=0.5,rely=0.120,anchor='center')

    decrypt_label3=Label(decrypt_subframe3,text="Enter The",width=10, bg="gray14",fg="white",padx=10,font="verdana 8 bold")
    decrypt_label3.place(relx=0.5,rely=0.2,anchor='center')

    decrypt_label4=Label(decrypt_subframe3,text="Image Id",width=10, bg="gray14",fg="white",padx=10,font="verdana 8 bold")
    decrypt_label4.place(relx=0.5,rely=0.23,anchor='center')

    decryptbutton_entry2=Entry(decrypt_subframe3,width=18, bg="gray7", fg="white", borderwidth=4)
    decryptbutton_entry2.place(relx=0.5,rely=0.27,anchor='center')

    decrypt_label5=Label(decrypt_subframe3,text="Enter The",width=10, bg="gray14",fg="white",padx=10,font="verdana 8 bold")
    decrypt_label5.place(relx=0.5,rely=0.33,anchor='center')

    decrypt_label6=Label(decrypt_subframe3,text="Security Code",width=10, bg="gray14",fg="white",padx=10,font="verdana 8 bold")
    decrypt_label6.place(relx=0.5,rely=0.36,anchor='center')

    decryptbutton_entry3=Entry(decrypt_subframe3,width=18, bg="gray7", fg="white", borderwidth=4)
    decryptbutton_entry3.place(relx=0.5,rely=0.40,anchor='center')

    decryptbutton_reset=Button(decrypt_subframe3,text="Reset",width=10, bg="dark slate gray",fg="white",padx=10,command=reset)
    decryptbutton_reset.place(relx=0.5,rely=0.5,anchor='center')


    decrypt_window.mainloop()


def mainWindow():
    root=Tk()
    root.geometry('450x280')
    root.resizable(False,False)
    root.title("Home")
    root.configure(bg="gray14")

    def show():
        var=clicked.get()
        root_entry_rec=root_entry.get()
        root_entry_cap_rec=root_entry_cap.get()
        print("Mail: ",root_entry_rec)
        print("The Captcha is : ",captcha_text)
        print("Your Entry is : ",root_entry_cap_rec)
        if(captcha_text==root_entry_cap_rec):

            if(var=="Encryption"):
                root.destroy()
                encryptWindow()
            elif(var=="Decription"):
                root.destroy()
                decryptWindow()
            else:
                win=Tk()
                win.configure(background='gray14')
                win.title("Message")
                win.geometry('400x200')

                win_frame=Frame(win,width=390,height=190, bg="gray14" ,highlightbackground="gray37",highlightthickness=3)
                win_frame.place(relx=0.5,rely=0.5,anchor='center')
                win_label=Label(win_frame,text="Please Select Any Option(Either encryption or decryption)",bg="gray14",fg="white",font="verdana 8 bold")
                win_label.place(relx=0.5,rely=0.5,anchor='center')
        else:
            win1=Tk()
            win1.configure(background='gray14')
            win1.resizable(False,False)
            win1.title("Message")
            win1.geometry('400x200')

            win1_frame=Frame(win1,width=390,height=190, bg="gray14" ,highlightbackground="gray37",highlightthickness=3)
            win1_frame.place(relx=0.5,rely=0.5,anchor='center')
            win1_label=Label(win1_frame,text="Your have Entered a Wrong Captcha",bg="gray14",fg="white",font="verdana 8 bold")
            win1_label.place(relx=0.5,rely=0.5,anchor='center')



    number=['1','2','3','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H',
            'I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
            'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
            's','t','u','v','w','x','y','z']
    max_captcha=4

    image=ImageCaptcha(width=140,height=60,font_sizes=[30, 30, 30, 30])
    captcha_text=[]
    for i in range(max_captcha):
        c=random.choice(number)
        captcha_text.append(c)

    captcha_text=''.join(captcha_text)
    print(captcha_text)


    captcha=image.generate(captcha_text)
    captcha_image=Image.open(captcha)

    image.write(captcha_text,'captim' + '.png')

    root_frame=Frame(root,width=440,height=270, bg="gray14" ,highlightbackground="gray37",highlightthickness=3)
    root_frame.place(relx=0.5,rely=0.5,anchor='center')

    rootlabel_1=Label(root_frame,text="Image Encryption/Decreption ",width=50, bg="gray37",fg="white",font="verdana 10 bold")
    rootlabel_1.place(relx=0.5,rely=0.042,anchor='center')

    rootlabel_2=Label(root_frame,text="Enter Your Email Id  ", bg="gray14",fg="white",font="verdana 8 bold")
    rootlabel_2.place(relx=0.3,rely=0.2,anchor='center')

    root_entry=Entry(root_frame,width=25, bg="gray7", fg="white", borderwidth=4)
    root_entry.place(relx=0.742,rely=0.2,anchor='center')

    rootlabel_3=Label(root_frame,text="Enter Your Choice  ", bg="gray14",fg="white",font="verdana 8 bold")
    rootlabel_3.place(relx=0.3,rely=0.4,anchor='center')

    clicked=StringVar()
    clicked.set("Select an Option")
    root_drop=OptionMenu(root_frame,clicked,"Encryption","Decription",)
    root_drop.config(bg="gray7",fg="white",borderwidth=1,highlightbackground = "gray37", highlightcolor= "gray37")
    root_drop["menu"].config(bg="dark slate gray",fg="white")
    root_drop.place(relx=0.7,rely=0.4,anchor='center')


    picture=Image.open("captim.png")
    resize=picture.resize((90,40),Image.ANTIALIAS)
    newpic=ImageTk.PhotoImage(resize)
    rootlabel_4=Label(root_frame,width=90,height=40,image=newpic)
    rootlabel_4.place(relx=0.3,rely=0.7,anchor='center')

    root_entry_cap=Entry(root_frame,width=25, bg="gray7", fg="white", borderwidth=4)
    root_entry_cap.place(relx=0.742,rely=0.7,anchor='center')
    #root_entry_cap_rec=root_entry_cap.get()


    root_button=Button(root,text="Go",bg="dark slate gray",fg="white",padx=12,command=show)
    root_button.place(relx=0.5,rely=0.85,anchor='center')

    root.mainloop()


def loading():
    splash_progress.start(5)
def desWindow():
    splash_progress.stop()
    splash.destroy()
    mainWindow()
splash_label1=Label(splash_frame,text="Image Cryptography",width=60,bg="gray37",fg="white",font="verdana 14 bold")
splash_label1.place(relx=0.5,rely=0.05,anchor='center')
splash_label2=Label(splash_frame,text="Loading...Opening the Modules,Please wait... ",bg="gray14",fg="white",font="verdana 8 bold")
splash_label2.place(relx=0.5,rely=0.4,anchor='center')
splash_label3=Label(splash_frame,text="Created by Pratyaush Ghosh, Kausik Saha, Ankita Das",bg="gray14",fg="white",font="verdana 8 bold")
splash_label3.place(relx=0.5,rely=0.8,anchor='center')
splash_label4=Label(splash_frame,text="(B.sc., 6th Sem)",bg="gray14",fg="white",font="verdana 8 bold")
splash_label4.place(relx=0.5,rely=0.9,anchor='center')

style = ttk.Style()
style.theme_use('alt')
style.configure("green.Horizontal.TProgressbar",foreground='white', background='dark slate gray')
splash_progress=ttk.Progressbar(splash_frame,style="green.Horizontal.TProgressbar", orient=HORIZONTAL,length=200, mode="indeterminate")
splash_progress.place(relx=0.5,rely=0.55,anchor='center')
loading()

splash.after(1000,desWindow)



splash.mainloop()



