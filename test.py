from pyrogram import Client, MessageHandler

app = Client(
    "my_bot",
    bot_token="623394207:AAHCJBxemok-kZqDSLv2Z89LykGXehMZnOo"
)

def my_function(client, message):
    message.reply(message.text)

my_handler = MessageHandler(my_function)
app.add_handler(my_handler)


if __name__ == '__main__':
	app.run()