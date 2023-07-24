from django.conf import settings
from twilio.rest import Client
import random
import string


class MessageHandler:
    def __init__(self, phone_number, otp):
        self.phone_number = phone_number
        self.otp = otp

    def send_otp(self):
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=f"Your OTP is {self.otp}",
            from_=settings.TWILIO_NUMBER,
            to=self.phone_number
        )
        return message.sid

def generate_user_id(length=5):
    characters = string.ascii_letters + string.digits
    user_id = ''.join(random.choices(characters, k=length))
    return user_id
