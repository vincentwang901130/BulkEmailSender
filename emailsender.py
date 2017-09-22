import smtplib
import time
from configure import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import random
import re


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
    with open(filename, mode='r') as message_file:
        message_file_content = message_file.read()
    return message_file_content


def main():
    pattern = re.compile(".*\\.txt$")
    while True:
        contactlist = raw_input("Please specify contact list file (*.txt):")
        messagecontent = raw_input("Please specify message file (*.txt):")
        if not pattern.match(contactlist) or not pattern.match(messagecontent):
            print "Wrong file format"
            continue
        else:
            flag1 = os.path.isfile("./"+contactlist)
            flag2 = os.access("./"+contactlist, os.R_OK)
            flag3 = os.path.isfile("./"+messagecontent)
            flag4 = os.access("./"+messagecontent, os.R_OK)
            if flag1 and flag2 and flag3 and flag4:
                break
            else:
                print "one or more files not exist or readable"
                continue
    emails = get_contacts(contactlist)
    msgtext = read_message(messagecontent)
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
