#Python Program saw on Tik-Tok about getting a program to email all the Colleges in the United States and asks them for a T-Shirt.
#Written by Stefan Avram for my little sister

import smtplib
import time

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)

smtpObj.ehlo()

smtpObj.starttls()

textFile = open("listOfCollegeEmails.txt", 'r')

#Logging into the email account
smtpObj.login('Your Email, 'Email Account Password")

for email in textFile:

    print("Email sent to: ", email)
    smtpObj.sendmail('Your Email', email,
    'Subject: Prospect Student!\nDear Admissions Committee,\n \n My name is blank and I am currently a Junior at Dr.Phillips High School in Orlando, Florida. The reason for my email today is that I am considering applying to your esteemed University and I wanted to ask if it would be possible to have some admission and general information mailed to me! Some free merchandise such as a T-shirt in Size M or anything else, would be awesome as well! I love the mascot as well as the school colors. My address is 6230 Morning Mist ln, Orlando, Florida 32819. Thank you for taking the time to read my email! Stay Safe! \n \n Best, Brian Hughes')
    time.sleep(2)

{}

    

print("****** ALL DONE ******")


 



