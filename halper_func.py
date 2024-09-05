import base64
from pyrogram import Client
from pyrogram.types import Message
import pymongo
from config import MONGO_URL

# Initialize MongoDB client
mongo_client = pymongo.MongoClient(MONGO_URL)
db = mongo_client['bot_db']  # Replace 'bot_db' with your actual database name
collection = db['messages']  # Replace 'messages' with your actual collection name

async def encode(data: str) -> str:
    """Encode a string using base64 encoding."""
    encoded_bytes = base64.urlsafe_b64encode(data.encode('utf-8'))
    return encoded_bytes.decode('utf-8')

async def get_message_id(client: Client, message: Message) -> int:
    """Extract the message ID from a forwarded message or link."""
    if message.forward_from:
        return message.message_id
    elif message.reply_to_message:
        return message.reply_to_message.message_id
    return None

async def store_message_id(user_id: int, message_id: int):
    """Store the message ID in MongoDB."""
    collection.update_one(
        {"user_id": user_id},
        {"$set": {"message_id": message_id}},
        upsert=True
    )

async def get_stored_message_id(user_id: int) -> int:
    """Retrieve the stored message ID from MongoDB."""
    document = collection.find_one({"user_id": user_id})
    return document['message_id'] if document else None
