import random
from flask import Flask, request
from datetime import datetime
from pymessenger import Bot
from NLP import wit_response
from tabulate import tabulate
import pandas

app = Flask("Schedule Bot")

ACCESS_TOKEN = ""
bot = Bot(ACCESS_TOKEN)

VERIFY_TOKEN = ""

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
times = ['08', '09', '10', '11', '12', '13', '14', '15']

@app.route('/', methods=['GET'])
def verify():
	if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
		if not request.args.get("hub.verify_token") == VERIFY_TOKEN:
			return "Verification token mismatch", 403
		return request.args["hub.challenge"], 200
	return "BUILD SUCCEEDED", 200

@app.route('/', methods=['POST'])
def webhook():
	print(request.data)
	data = request.get_json()

	if data['object'] == "page":
		entries = data['entry']

		for entry in entries:
			messaging = entry['messaging']

			for messaging_event in messaging:
				sender_id = messaging_event['sender']['id']

				if messaging_event.get('message'):
					message_text = messaging_event['message'].get('text')

					if messaging_event['message'].get('attachments'):
						response_sent_nontext = get_attachments()
						send_message(sender_id, response_sent_nontext)

					response = None
					entity, value = wit_response(message_text)

					if entity == 'developer':
						response = "Nikhil Gupta created me :)"

					if entity == 'S1':
						response = "Cool! :D \n Enter time :)"

					if entity == 'timetable':
						df = pandas.read_csv('timetable.csv')
						response = "Here is your time table :D\n\n" + tabulate(df, tablefmt="grid")

					if entity == 'user_greetings':
						response = "Welcome to Schedule Chatbot! :D\nPlease enter your section :)"

					if entity == 'datetime':
						dt = "{0}".format(str(value))
						u = datetime.strptime(dt, '%Y-%m-%dT%H:%M:%S.000+05:30')
						v = u.strftime('%A %H:%M %Y-%m-%d').split()
						index_of_day = days.index(v[0])
						x = v[1][0:2]
						if x in times:
							index_of_time = times.index(x) + 1
							df = pandas.read_csv('s1.csv')
							response = "You have " + df.loc[index_of_day][index_of_time] + " :)"
						else:
							response = "You don't have any class at that time!"

					if response == None:
						response = "I have no idea what you are saying. I'm still learning :)"

					bot.send_text_message(sender_id, response)
					
	return "ok", 200

def get_attachments():
	return "I've no idea what to do with it :("

def send_message(sender_id, response):
	# sends user the text message provided via input response parameter
	bot.send_text_message(sender_id, response)
	return "success"

if __name__ == "__main__":
	app.run(port=8000, use_reloader=True)
