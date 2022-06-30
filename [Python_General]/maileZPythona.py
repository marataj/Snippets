import smtplib

emailFrom="Python"
emailTo="jatar.elektronika@gmail.com"
emailAdress="jatar.elektronika@gmail.com"
emailPassword="Jatarek1234"

emailSubject="Test of pythons ability to sending emails"
emailContent="Python is able to sending emails"
emailMessage='''From:{}
Subject:{}

{}
'''.format(emailFrom,emailSubject,emailContent)
try:
    EmailCon=smtplib.SMTP_SSL('smtp.gmail.com',465)
    EmailCon.ehlo()
    EmailCon.login(emailAdress,emailPassword)
    EmailCon.sendmail(emailFrom,emailTo,emailMessage)
    EmailCon.close()
except:
    print("error")
else:
    print("email sent sucesfuly")
