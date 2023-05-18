# from pyrogram import Client, filters
# from pyrogram.types import Message

# from models import update_user_unknown_id, get_user_with_real_id
# from utilities import md5_hash





# @Client.on_message(filters.command('revoke') & filters.private)
# async def revoke(client: Client, message: Message):
#     user_id = str(message.chat.id)

#     user = get_user_with_real_id(user_id)

#     if user:
#         # new_unknown_id = ah Shit ! hashing with md5 not gen a new md5 :| 
#         update_user_unknown_id()

#     else:
#         await message.reply('''**You dont have Unknown Id**

# Send this Command to Get Unknown Id /id''')