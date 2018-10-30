#Python libraries that we need to import for our bot
import os
import random
from flask import Flask, request
from pymessenger.bot import Bot

app = Flask(__name__)
ACCESS_TOKEN = 'EAAesOYFlRUwBAFZAAW3XGpWQgvliso6FYtL0YtBjZAhYVoqIACBBC0vOoPE0ZCCA3cc6eIOmv541LexG06jaKV0EwAPb6pwe8dZAtjb0Na9zzTvgRQW9MZCQQ3zZA1OruowbC6rqMShW8R8G8lt2Ds9v3ZBWWUe7TDqd9QPcrx2WewqeAHeO0mQ'
VERIFY_TOKEN = 'schedule_bot'
bot = Bot(os.environ[ACCESS_TOKEN])



@app.route("/", methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        if request.args.get("hub.verify_token") == os.environ[VERIFY_TOKEN]:
            return request.args.get("hub.challenge")
        else:
            return 'Invalid verification token'

    elif request.method == 'POST':

       output = request.get_json()
       for event in output['entry']:
          messaging = event['messaging']
          for message in messaging:
            if message.get('message'):
                #Facebook Messenger ID for user so we know where to send response back to
                recipient_id = message['sender']['id']
                if message['message'].get('text'):
                    response_sent_text = get_message()
                    send_message(recipient_id, response_sent_text)
                #if user sends us a GIF, photo,video, or any other non-text item
                if message['message'].get('attachments'):
                    response_sent_nontext = get_message()
                    send_message(recipient_id, response_sent_nontext)
    return "Message Processed"

# def verify_fb_token(token_sent):
#     if token_sent == VERIFY_TOKEN:
#         return request.args.get("hub.challenge")
#     return 'Invalid verification token'

def get_message():
    sample_responses = ["You are stunning!", "We're proud of you.",
                        "Keep on being you!", "We're grateful to know you :)"]

    return random.choice(sample_responses)

def send_message(recipient_id, response):
    bot.send_text_message(recipient_id, response)
    return "success"

if __name__ == "__main__":
    app.run()
