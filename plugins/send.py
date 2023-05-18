from pyrogram import Client, filters
from pyrogram.types import Message

from models import get_user_with_unknown_id, get_user_with_real_id






@Client.on_message(filters.command('send') & filters.private)
async def send(client: Client, message: Message):
    reciver_unknown_id = await message.chat.ask('**Enter User ID:**')
    sender_message = await message.chat.ask('**Enter Message : **')

    sender  = get_user_with_real_id(str(message.chat.id))
    reciver = get_user_with_unknown_id(reciver_unknown_id.text)

    if reciver:

        text = f'''**Message From:** `{sender[1] if sender else 'Unknown'}`

{sender_message.text}
'''

        await Client.send_message(client, chat_id=reciver[0], text=text)

        await message.reply('**Message Sent.**')
    else:
        await message.reply('**User Not Found!**')