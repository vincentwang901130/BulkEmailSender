import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random


FROM_ADDRESS = "biblesforcarleton@gmail.com"
SMTP_SERVER = "smtp.gmail.com:587"
SMTP_USER = "biblesforcarleton@gmail.com"
SMTP_PASS = "gtca2017"
SUBJECT = "Bible Study - Bibles for Carleton"

def mail(msg):
    server = smtplib.SMTP(SMTP_SERVER)
    server.starttls()
    server.login(SMTP_USER, SMTP_PASS)
    server.sendmail(FROM_ADDRESS, msg['To'], msg.as_string())
    server.quit()

def get_contacts(filename):
    emails = []
    with open(filename, mode='r') as contacts_file:
        for contact in contacts_file:
            emails.append(contact)
    return emails

def read_message(filename):
    with open(filename, mode ='r') as message_file:
        message_file_content = message_file.read()
    return message_file_content

def main():
    emails = get_contacts('testcontact.txt')
    msgtext = read_message('message.txt')
    random.seed(time.time())
    for email in emails:
        msg = MIMEMultipart()
        msg['Subject'] = SUBJECT
        msg['To'] = email
        msg['From'] = FROM_ADDRESS
        msg.attach(MIMEText(msgtext, 'html'))
        print msg.as_string()
        mail(msg)
        del msg
        sleeptime = random.randint(1, 2)
        print sleeptime
        time.sleep(sleeptime)


if __name__ == '__main__':
    main()