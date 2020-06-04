import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

email=EmailMessage()
email['from']='bhanu prakash'
email['to']='bpkhandelwal03@gmail.com'
email['subject']='You won 10000000000 dollars !'

html=Template(Path('index.html').read_text())
email.set_content(html.substitute({'name':'jai shree ram'}),'html')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('dummypython03@gmail.com','bpk87400')
	smtp.send_message(email)
	print('mail sent successfully!!!!!!!')