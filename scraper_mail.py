import smtplib
from email.mime.text import MIMEText #Email module
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders



from_ ='krushnakulkarni17@gmail.com'
password_= 'nvcxwweqnuexufky' #app password in gmail 
to_ = 'krushnakulkarni18@gmail.com'
subject= "Today's Fianance Report"



def send(filename):
    msg= MIMEMultipart()
    msg['From']= from_
    msg['To'] = to_
    msg['Subject']= subject


    body = "<b>Today's Fianance Report Attached. <b>"
    msg.attach(MIMEText(body, 'html'))  

    my_file = open(filename, 'rb') #reading file using open and read binary(rb)
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((my_file).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename= ' + filename)
    msg.attach(part)




    message= msg.as_string() #combining .msg and giving the message as string


    server = smtplib.SMTP('smtp.gmail.com',587) #port no for gmail is 587
    server.starttls()
    server.login(from_,password_) #login credentials i.e. email and password


    server.sendmail(from_, to_, message) #sending mail using from to and message
    print("Mail sent")
    server.quit()