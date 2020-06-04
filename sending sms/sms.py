# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC96e4efd68d94d7247a5670c8d798db4f'
auth_token = '301c9067473806b8a4395b6903e8db97'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='wOOOOww its working man!!',
                              from_='+17856694015',
                              to='+918740044348'
                          )

print(message.sid)
