from pyrogram import Client, MessageHandler
from credentials import bot_token

app = Client(
    "my_bot",
    bot_token=bot_token
)

def my_function(client, message):
    message.reply(message.text)

my_handler = MessageHandler(my_function)
app.add_handler(my_handler)


if __name__ == '__main__':
	app.run()