from pyrogram import Client, Emoji, Filters
from credentials import bot_token
from datetime import datetime
from persiantools.jdatetime import JalaliDate


events = list()

app = Client(
    "reminder_bot",
    bot_token=bot_token
)


@app.on_message(Filters.regex(r'/add_event [a-zA-Z\s]* 13\d\d/\d{1,2}/\d{1,2}'))
def add_event(client, message):
    _, name, date = message.text.split()
    print(name)
    date = list(map(int, date.split('/')))
    date = JalaliDate(date[0], date[1], date[2]).to_gregorian()
    print(date)
    events.append({date : name})



if __name__ == '__main__':
	app.run()