import smtplib
from email.message import EmailMessage

email=EmailMessage()
email['from']='bhanu prakash'
email['to']='khandelwalbhanuprakash@gmail.com'
email['subject']='You won 10000000000 dollars !'

email.set_content('I am a python master and a full stack developer!!!')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('dummypython03@gmail.com','bpk87400')
	smtp.send_message(email)
	print('mail sent successfully !') 