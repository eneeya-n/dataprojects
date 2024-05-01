import oauth
from email.mime.text import MIMEText
import base64
import math
import random

def create_message(sender, to, subject, message_text):
  message = MIMEText(message_text)
  message['to'] = to
  message['from'] = sender
  message['subject'] = subject
  return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}

def send_message(sender,to,subject,message_text,user_id='me'):
  msg = create_message(sender,to,subject,message_text)
  try:
    service = oauth.get_g_service()
    message = (service.users().messages().send(userId=user_id, body=msg)
               .execute())
    return message
  except ValueError as e:
    print('An error occurred: %s' % e)


def send_otp(user_mail):
    digits = "0123456789"
    OTP = ""
    for i in range (6):
        OTP += digits[math.floor(random.random()*10)]
    otp = OTP + " is your One-Time-Password"
    message = otp
    send_message("iqmathindia@gmail.com",user_mail,"Your OTP for Verification",message,user_id='me')
    return OTP
