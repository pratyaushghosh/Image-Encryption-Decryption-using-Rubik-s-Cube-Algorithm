import smtplib
from tkinter import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_gmail(s_name,s_email,r_email,s_pass,e_sub):
    sfile=open("password.txt","r")
    s_code=sfile.read()
    #The mail addresses and password
    sender_address =s_email
    sender_pass =s_pass
    receiver_address =r_email
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = s_name
    message['To'] = receiver_address
    # message['Subject'] = 'A test mail sent by Python. It has an attachment.'
    message['Subject'] = e_sub
    #The subject line
    # The body and the attachments for the mail
    mail_body ="Your Password is : "+s_code
    message.attach(MIMEText(mail_body, 'plain'))


    attach_file_name = 'encrypted_images\encrypted_result.png'
    file_name = 'encrypted_result.png'
    attach_file = open(attach_file_name, 'rb')
    # attach_file = open(attach_file_name, 'rb') # Open the file as binary mode
    payload = MIMEBase('application', 'octet-stream')#octet-stream is for 8bit
    payload.set_payload((attach_file).read())#no change  when it is in read mode
    encoders.encode_base64(payload) #encode the attachment
    #add payload header with filename
    # payload.add_header('Content-Decomposition', 'attachment, filename='+attach_file_name)
    # payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
    payload.add_header('Content-Disposition', 'attachment; filename= '+file_name)
    message.attach(payload)


    attach_file_name11 = 'Kr.txt'
    attach_file11 = open(attach_file_name11, 'rb')
    payload11 = MIMEBase('application', 'octet-stream')#octet-stream is for 8bit
    payload11.set_payload((attach_file11).read())#no change  when it is in read mode
    encoders.encode_base64(payload11) #encode the attachment
    #add payload header with filename
    payload11.add_header('Content-Disposition', 'attachment; filename= '+attach_file_name11)
    message.attach(payload11)

    attach_file_name22 = 'Kc.txt'
    attach_file22 = open(attach_file_name22, 'rb')
    payload22 = MIMEBase('application', 'octet-stream')#octet-stream is for 8bit
    payload22.set_payload((attach_file22).read())#no change  when it is in read mode
    encoders.encode_base64(payload22) #encode the attachment
    #add payload header with filename
    payload22.add_header('Content-Disposition', 'attachment; filename= '+attach_file_name22)
    message.attach(payload22)

    """attach_file_name33 = 'hi.txt'
    attach_file33 = open(attach_file_name33, 'rb')
    payload33 = MIMEBase('application', 'octet-stream')#octet-stream is for 8bit
    payload33.set_payload((attach_file33).read())#no change  when it is in read mode
    encoders.encode_base64(payload33) #encode the attachment
    #add payload header with filename
    payload33.add_header('Content-Disposition', 'attachment; filename= '+attach_file_name33)
    message.attach(payload33)"""

    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    # session.sendmail(sender_address, receiver_address, text)
    session.sendmail(sender_address, receiver_address,text)
    session.quit()
    print('Mail Sent')

    meswin=Tk()
    meswin.configure(background='gray14')
    meswin.resizable(False,False)
    meswin.title("Message")
    meswin.geometry('400x200')

    meswin_frame=Frame(meswin,width=390,height=190, bg="gray14" ,highlightbackground="gray37",highlightthickness=3)
    meswin_frame.place(relx=0.5,rely=0.5,anchor='center')
    meswin_label=Label(meswin_frame,text="Mail has been sent Successfully",bg="gray14",fg="white",font="verdana 8 bold")
    meswin_label.place(relx=0.5,rely=0.5,anchor='center')
    meswin.mainloop()













