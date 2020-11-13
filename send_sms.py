import os
import twilio
from twilio.rest import Client
from dotenv import load_dotenv

from logger_settings import logging


load_dotenv()

TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
FROM = os.getenv('TELEPHONE_NUMBER_FROM_TWILIO')
TO = os.getenv('YOUR_TELEPHONE_NUMBER')
CLIENT = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)


def send_sms(text_message):
    try:
        message = CLIENT.messages.create(body=text_message, from_=FROM, to=TO)

        if message.sid:
            logging.info(f'The message: "{text_message}" is sent.')
            return print('The message is sent successfully.')
        else:
            return print('Failed to send the message.')

    except twilio.base.exceptions.TwilioRestException:
        return print('Not a valid telephone number.')
