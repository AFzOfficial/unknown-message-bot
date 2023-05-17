from pyrogram import Client, filters
from pyrogram.types import Message

from models import get_unknown_with_unknown_id








@Client.on_message(filters.command('send') & filters.private)
async def send(client: Client, message: Message):
    unknown_id = await message.chat.ask('**Enter User ID:**')
    unknown_message = await message.chat.ask('**Enter Message : **')

    user = get_unknown_with_unknown_id(unknown_id.text)

    if user:
        await Client.send_message(client, chat_id=user[0], text=unknown_message.text)

        await message.reply('**Message Sent.**')
    else:
        await message.reply('**User Not Found!**')