from twilio.rest import Client
from dotenv import load_dotenv
from pydantic import ValidationError
import os
import logging
from .model.message_model import MessageData

load_dotenv()

# Setup logging
logging.basicConfig(level=logging.INFO)

# Validate env vars
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")

if not account_sid or not auth_token:
    raise ValueError("Twilio credentials not found in environment variables.")

def send_whatsapp_message(sender_contact: str, message_text: str, receiver_contact: str):
    try:
        # Validate msg data
        msg_data = MessageData(
            from_=f"whatsapp:{sender_contact}",
            to=f"whatsapp:{receiver_contact}",
            body=message_text,
        )

        # Create twilio client
        client = Client(account_sid, auth_token)

        # send messages
        message = client.messages.create(
            from_=msg_data.from_,
            body=msg_data.body,
            to=msg_data.to,
        )

        logging.info(f"Message sent successfully: {message.sid}")
        return message.sid

    except ValidationError as e:
        logging.error(f"Validation Error: {e}")
    except Exception as e:
        logging.error(f"Failed to send message: {e}")





