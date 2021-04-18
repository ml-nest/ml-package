## Need to enable "Less secure app access" in google account settings from the reciever end

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#The mail addresses and password
sender_address = 'bharat3214@gmail.com'
sender_pass = 'passwords'
receiver_address = 'bharat3214@gmail.com'

# Content
mail_content = """content"""
subject = """subject"""

def send_email_gmail(sender_address, sender_pass, receiver_address, mail_content, subject):
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = subject   #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    # session = smtplib.SMTP('smtp-mail.outlook.com', 587)
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()

send_email_gmail(sender_address, sender_pass, receiver_address, mail_content, subject)