from tkinter import *
import random,time

number=['0','1','2','3','3','4','5','6','7','8','9','A','B','C','D','E','F','G',
        'H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y',
        'Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
        'r','s','t','u','v','w','x','y','z','@','&','*','#','@','%','&','*']
max_passgen=10

passgen_text=[]
for i in range(max_passgen):
    c=random.choice(number)
    passgen_text.append(c)

passgen_text=''.join(passgen_text)
print(passgen_text)
with open('securitycode.txt', 'w') as Pass:
    Pass.write(passgen_text)

win=Tk()
win.configure(background='gray14')
win.resizable(False,False)
win.title("Message")
win.geometry('400x200')

def des():
    win.destroy()

win_frame=Frame(win,width=390,height=190, bg="gray14" ,highlightbackground="gray37",highlightthickness=3)
win_frame.place(relx=0.5,rely=0.5,anchor='center')
win_label=Label(win_frame,text="Security Code Generated",bg="gray14",fg="white",font="verdana 8 bold")
win_label.place(relx=0.5,rely=0.5,anchor='center')

win.after(2000,des)

mainloop()








