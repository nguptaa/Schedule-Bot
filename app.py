#Python libraries that we need to import for our bot
import os
import random
from flask import Flask, request
from pymessenger.bot import Bot

app = Flask(__name__)
ACCESS_TOKEN = 'EAAesOYFlRUwBAFZAAW3XGpWQgvliso6FYtL0YtBjZAhYVoqIACBBC0vOoPE0ZCCA3cc6eIOmv541LexG06jaKV0EwAPb6pwe8dZAtjb0Na9zzTvgRQW9MZCQQ3zZA1OruowbC6rqMShW8R8G8lt2Ds9v3ZBWWUe7TDqd9QPcrx2WewqeAHeO0mQ'
VERIFY_TOKEN = 'schedule_bot'
bot = Bot(ACCESS_TOKEN)

@app.route("/", methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return request.args.get("hub.challenge")
        return 'Invalid verification token'
    return 'Hello World', 200

    else:
       output = request.get_json()
       for event in output['entry']:
          messaging = event['messaging']
          for message in messaging:
            if message.get('message'):
                #Facebook Messenger ID for user so we know where to send response back to
                recipient_id = message['sender']['id']
                if message['message'].get('text'):
                    response_sent_text = get_text()
                    send_message(recipient_id, response_sent_text)
                #if user sends us a GIF, photo,video, or any other non-text item
                if message['message'].get('attachments'):
                    response_sent_nontext = get_attachments()
                    send_message(recipient_id, response_sent_nontext)
    return "Message Processed"

def get_text():
    sample_responses = ["You are stunning!", "We're proud of you.",
                        "Keep on being you!", "We're grateful to know you :)"]

    return random.choice(sample_responses)

def get_attachments():
    return "I've no idea what to do with a image or attachments :("

def send_message(recipient_id, response):
    bot.send_text_message(recipient_id, response)
    return "success"

if __name__ == "__main__":
    app.run()
