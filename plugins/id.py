from pyrogram import Client, filters
from pyrogram.types import Message

from models import add_user, get_user_with_real_id
from utilities import md5_hash





@Client.on_message(filters.command('id') & filters.private)
async def id(client: Client, message: Message):
    user_id = str(message.chat.id)

    user = get_user_with_real_id(user_id)

    if user:
        await message.reply(f'''**Unknown ID:** `{user[1]}`

**Others can send you unknown messages with this ID**
''')

    else:
        unknown_id = md5_hash(user_id)

        if add_user(user_id, unknown_id):
            await message.reply(f'''**Unknown ID:** `{unknown_id}`

**Others can send you unknown messages with this ID**
''')
        else:
            await message.reply('Database Error!')