import random
from flask import Flask, request
from pymessenger import Bot
from NLP import wit_response
from tabulate import tabulate
import pandas
import csv

app = Flask("Schedule Bot")

ACCESS_TOKEN = "EAAesOYFlRUwBAFZAAW3XGpWQgvliso6FYtL0YtBjZAhYVoqIACBBC0vOoPE0ZCCA3cc6eIOmv541LexG06jaKV0EwAPb6pwe8dZAtjb0Na9zzTvgRQW9MZCQQ3zZA1OruowbC6rqMShW8R8G8lt2Ds9v3ZBWWUe7TDqd9QPcrx2WewqeAHeO0mQ"
bot = Bot(ACCESS_TOKEN)

VERIFY_TOKEN = "schedule_bot"

sections = ['s1','section1','s 1','section 1']
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
times = ['8am', '9am', '10am', '11am', '12pm', '1pm', '2pm', '3pm']
timetable=['timetable','tt','routine','schedule']



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
				# recipient_id = messaging_event['recipient']['id']
				if messaging_event.get('message'):
					message_text = messaging_event['message'].get('text').lower()
					if messaging_event['message'].get('attachments'):
						response_sent_nontext = get_attachments()
						send_message(sender_id, response_sent_nontext)

					elif message_text in sections:
						response_sent_text = "Please enter Day and Time :)"
						send_message(sender_id, response_sent_text)

					elif messaging_event['message'].get('text'):
						daystime=list(map(str,message_text.split()))

						if len(daystime) == 2 and daystime[0] in days and daystime[1] in times:
							index_of_day = days.index(daystime[0])
							index_of_time = times.index(daystime[1]) + 1
							df = pandas.read_csv('s1.csv')
							response_sent_text = "You have " + df.loc[index_of_day][index_of_time] + ". :)"
							send_message(sender_id, response_sent_text)
						# else:
							# response_sent_text = "I didn't understand what you meant. Give me sometime. I'm still learning :)"
							# send_message(sender_id, response_sent_text)
					
					response = None

					entity, value = wit_response(message_text)
					if entity == 'developer':
						response = "Nikhil Gupta created me :)"
					if entity == 'user_greetings':
						response = "Welcome to Schedule Chatbot! :D \nPlease enter your section :)"
					if entity == 'timetable':
						df = pandas.read_csv('timetable.csv')
						response = "Here is your time table :D\n\n" + tabulate(df, tablefmt="grid")
					if entity == 'datetime':
						response = "Here is {0}".format(str(value))
						# response = "datetime detected"
					if response == None:
						response = "I have no idea what you are saying. I'm still learning :)"

					bot.send_text_message(sender_id, response)

					# else:
					# 	response_sent_text = "I didn't understand what you meant. Give me sometime. I'm still learning :)"
					# 	send_message(sender_id,response_sent_text)
					# if user sends us a GIF, photo,video, or any other non-text item
					
	return "ok", 200


def get_attachments():
	return "I've no idea what to do with it :("

def send_message(sender_id, response):
	# sends user the text message provided via input response parameter
	bot.send_text_message(sender_id, response)
	return "success"


if __name__ == "__main__":
	app.run(port=8000, use_reloader=True)
