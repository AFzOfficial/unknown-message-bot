import pyromod, os
from pyrogram import Client



app = Client(
    'pyrogram',
    api_id=0,          # SET YOUR API ID
    api_hash='abc',    # SET YOUR API HASH
    bot_token='token', # SET YOUR BOT TOKEN
    plugins=dict(root='plugins')
)



if __name__ == '__main__':
    os.system('clear')
    print('Starting Bot..')

    app.run()
