"""This is the Welcome Bot in @PyrogramChat.

It uses the Emoji module to easily add emojis in your text messages and Filters
to make it only work for specific messages in a specific chat.
"""

from pyrogram import Client, Emoji, Filters
from credentials import bot_token

# TARGET = "nnojish"  # Target chat. Can also be a list of multiple chat ids/usernames
MENTION = "[{}](tg://user?id={})"  # User mention markup
MESSAGE = "{} Welcome to [Pyrogram](https://docs.pyrogram.org/)'s group chat {}!"  # Welcome message

app = Client("my_account", bot_token = bot_token)



@app.on_message(Filters.new_chat_members)
def welcome(client, message):
    new_members = [MENTION.format(i.first_name, i.id) for i in message.new_chat_members]
    # print(new_members)

    text = MESSAGE.format(Emoji.SPARKLES, ", ".join(new_members))
    # print(text)
    message.reply(text)



app.run()  # Automatically start() and idle()

