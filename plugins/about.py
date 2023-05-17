from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command('about') & filters.private)
async def start(client: Client, message: Message):
    await message.reply('**Maintainer:** pycloud.space')