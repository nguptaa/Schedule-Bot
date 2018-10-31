import random
from flask import Flask, request
from pymessenger import Bot

app = Flask("Schedule Bot")

ACCESS_TOKEN = "EAAesOYFlRUwBAFZAAW3XGpWQgvliso6FYtL0YtBjZAhYVoqIACBBC0vOoPE0ZCCA3cc6eIOmv541LexG06jaKV0EwAPb6pwe8dZAtjb0Na9zzTvgRQW9MZCQQ3zZA1OruowbC6rqMShW8R8G8lt2Ds9v3ZBWWUe7TDqd9QPcrx2WewqeAHeO0mQ"
bot = Bot(ACCESS_TOKEN)

VERIFY_TOKEN = "schedule_bot"

greetings = ['Hi', 'Hello', 'Hey', "What's up"]


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
					if messaging_event['message'].get('text'):
						response_sent_text = get_message()
						send_message(sender_id, response_sent_text)
					# if user sends us a GIF, photo,video, or any other non-text item
					if messaging_event['message'].get('attachments'):
						response_sent_nontext = get_message()
						send_message(sender_id, response_sent_nontext)

				# if messaging_event.get('message'):
				# 	# HANDLE NORMAL MESSAGES HERE
				# 	if messaging_event['message'].get('text'):
				# 		# HANDLE TEXT MESSAGES
				# 		query = messaging_event['message']['text']
				# 		# ECHO THE RECEIVED MESSAGE
				# 		bot.send_text_message(sender_id, query)
	return "ok", 200


def get_message():
	sample_responses = ["You are stunning!", "We're proud of you.",
						"Keep on being you!", "We're grateful to know you :)"]

	return random.choice(sample_responses)


def send_message(recipient_id, response):
	# sends user the text message provided via input response parameter
	bot.send_text_message(recipient_id, response)
	return "success"


if __name__ == "__main__":
	app.run(port=8000, use_reloader=True)
