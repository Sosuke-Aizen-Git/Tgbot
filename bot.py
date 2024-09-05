from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import BOT_TOKEN, MONGO_URL, OWNER_ID
from helper_func import encode, get_message_id

app = Client("my_bot", bot_token=BOT_TOKEN)

# Start Command
@app.on_message(filters.private & filters.command('start'))
async def start(client: Client, message: Message):
    user = message.from_user.first_name
    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("About", callback_data="about")],
        [InlineKeyboardButton("Close", callback_data="close")]
    ])
    await message.reply_text(f"Hello {user}! Welcome to the bot. Use /help to see available commands.", reply_markup=reply_markup)

# About Command
@app.on_callback_query(filters.regex("about"))
async def about(client: Client, callback_query):
    await callback_query.message.edit_text("This bot is developed by Your Name. For more details, visit our website: https://yourwebsite.com")

# Close Command
@app.on_callback_query(filters.regex("close"))
async def close(client: Client, callback_query):
    await callback_query.message.delete()

# Genlink Command
@app.on_message(filters.private & filters.command('genlink'))
async def genlink(client: Client, message: Message):
    if message.from_user.id != OWNER_ID:
        await message.reply("You are not authorized.")
        return

    while True:
        try:
            channel_message = await client.ask(
                text="🚀 Forward a message from DB channel...",
                chat_id=message.from_user.id,
                filters=(filters.forwarded | (filters.text & ~filters.forwarded)),
                timeout=60
            )
        except:
            return
        msg_id = await get_message_id(client, channel_message)
        if msg_id:
            break
        else:
            await channel_message.reply("🚫 Error. It must be from DB channel. Try again.", quote=True)
            continue

    base64_string = await encode(f"get-{msg_id * abs(client.db_channel.id)}")
    link = f"https://t.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("📫 Your URL", url=f'https://telegram.me/share/url?url={link}')]])
    await channel_message.reply_text(f"<b>Here is your link</b>\n\n{link}", quote=True, reply_markup=reply_markup)

# Batch Command
@app.on_message(filters.private & filters.command('batch'))
async def batch(client: Client, message: Message):
    if message.from_user.id != OWNER_ID:
        await message.reply("You are not authorized.")
        return

    while True:
        try:
            first_message = await client.ask(
                text="🚀 Forward first message from DB channel...",
                chat_id=message.from_user.id,
                filters=(filters.forwarded | (filters.text & ~filters.forwarded)),
                timeout=60
            )
        except:
            return
        f_msg_id = await get_message_id(client, first_message)
        if f_msg_id:
            break
        else:
            await first_message.reply("🚫 Error. It must be from DB channel. Try again.", quote=True)
            continue

    while True:
        try:
            second_message = await client.ask(
                text="🚀 Forward last message from DB channel...",
                chat_id=message.from_user.id,
                filters=(filters.forwarded | (filters.text & ~filters.forwarded)),
                timeout=60
            )
        except:
            return
        s_msg_id = await get_message_id(client, second_message)
        if s_msg_id:
            break
        else:
            await second_message.reply("🚫 Error. It must be from DB channel. Try again.", quote=True)
            continue

    string = f"get-{f_msg_id * abs(client.db_channel.id)}-{s_msg_id * abs(client.db_channel.id)}"
    base64_string = await encode(string)
    link = f"https://t.me/{client.username}?start={base64_string}"
    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("📫 Your URL", url=f'https://telegram.me/share/url?url={link}')]])
    await second_message.reply_text(f"<b>Here is your link</b>\n\n{link}", quote=True, reply_markup=reply_markup)

# Add more command handlers here...

# Start the bot
app.run()
