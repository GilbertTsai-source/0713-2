import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

sender="gilberttsai.ct@gmail.com"
receiver = ["tyler@mail.sju.edu.tw","gilberttsai.ct@gmail.com"]

msg = MIMEMultipart()
msg["From"] = sender
header = Header("Test Send Email","utf-8")
msg["Subject"] = header.encode()
body = "This is email send from python"

    
for i in receiver:
    
    msg["To"] =i
    msg.attach(MIMEText(body))
    ssl_context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=ssl_context) as server:
        server.login(sender,"eigv jjmh vcky khnn")
        server.sendmail(sender,i,msg.as_string())
        print("success send email")