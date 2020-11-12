import os
from twilio.rest import Client
from dotenv import load_dotenv


def send_sms(text_message):
    load_dotenv()

    TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
    TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    message = client.messages.create(
              body=text_message,
              from_=os.getenv('TELEPHONE_NUMBER_FROM_TWILIO'),
              to=os.getenv('YOUR_TELEPHONE_NUMBER'),
              )

    if message.sid:
        return print('Сообщение успешно отправлено.')
    else:
        return print('Невозможно отправить сообщение.')
