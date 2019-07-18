from pyrogram import Client, Emoji, Filters, ReplyKeyboardMarkup
from credentials import bot_token
from datetime import datetime
import time
from pytz import timezone as tz
from persiantools.jdatetime import JalaliDateTime
import schedule

tehran = tz('Asia/Tehran')
MESSAGE = "Event {} at {}"


events = list()

app = Client(
    "reminder_bot",
    bot_token=bot_token
)


@app.on_message(Filters.regex(r'/add_event [a-zA-Z\s]* 13\d\d/\d{1,2}/\d{1,2} \d{2}:\d{2}'))
def add_event(client, message):
    _, name, date, hour = message.text.split()
    year, month, day = list(map(int, date.split('/')))
    hour, minute = list(map(int, hour.split(':')))
    date = JalaliDateTime(year, month, day).to_gregorian()
    # date = date.replace(hour=hour, minute=minute, tzinfo=tehran)
    date = date.replace(hour=hour, minute=minute, tzinfo=tz('UTC'))
    events.append({date : [name, message.chat.id]})
    message.reply(
		"Time",
		reply_markup = ReplyKeyboardMarkup(
			[
				["1 Week Before", "1 Day Before", "1 Hour Before"]
			],
			resize_keyboard=True
		)
	)


def remind(event):
	date = list(event.keys())[0]
	name = event[date][0]
	chat_id	= event[date][1]
	date = date.strftime("%d-%b-%Y")
	print(f"chat_id: {chat_id}")
	app.send_message(chat_id = chat_id, text=MESSAGE.format(name, date))

def check_events():
	global events
	events.sort(key=lambda e: list(e.keys())[0])
	closer = events[0]
	print("closer")
	print(closer)
	date = list(closer.keys())[0]
	# now = datetime.now(tz = tehran)
	now = datetime.utcnow().replace(tzinfo=tz('UTC'))
	print(f"date: {date}\nnow: {now}")
	if date > now and (date - now).seconds//3600 < 1:
		# events.pop(closer)
		remind(closer)
	else:
		print(f"else statement")



if __name__ == '__main__':
	# app.run()
	app.start()
	schedule.every(30).seconds.do(check_events)
	while True:
		schedule.run_pending()
		time.sleep(5)
