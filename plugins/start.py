from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command('start') & filters.private)
async def start(client: Client, message: Message):
    await message.reply('**Welcome to Unknown Message Bot.**')