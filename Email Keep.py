import gkeepapi
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email address, password, and list id (which can be found in the url of the note in a browser) go here
email = 
password = 
noteid = "yeet"


smtp_server = "smtp.gmail.com"
port = 587

context = ssl.create_default_context()

try:
    server = smtplib.SMTP(smtp_server,port)
    server.starttls(context=context)
    server.login(email, password)

    keep = gkeepapi.Keep(noteid)
    keep.login(email, password)
    note = keep.get()
    uncheckedItems = note.unchecked
    subject = note.title

    text = ""

    for x in uncheckedItems:
        text = text + str(x)[2:len(str(x))] + "\r\n"
    
    msg = MIMEMultipart()
    msg["From"] = email
    msg["To"] = email
    msg["Subject"] = subject

    msg.attach(MIMEText(text.rstrip(), "plain"))

    server.sendmail(email,email,msg.as_string())
except Exception as e:
    print(e)
finally:
    server.quit()