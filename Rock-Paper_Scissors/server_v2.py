
from flask import Flask, request
import requests, facebook, random, json, schedule, time

#
# app = Flask(__name__)
#

app = Flask(__name__)

# This needs to be filled with the Page Access Token that will be provided
# by the Facebook App that will be created.
PAT = 'EAAOoaZCRNGOkBAOKr8sfaV05mQl3zbQhHKjIwgCDeTCrrSXgoMmJZCDRdrboJVRfPor7W6w9pusfMzZC5y4fFDPZCWaC2FDxXGf9Blcsq1Rg6xOTYZAucts1itbDsl9JaENrI5hC6VpCz1S4ZCxPjkw0JUctv7chZCKtlRi1YmC0gZDZD'

user_dic = {'Flo Floh':1091914804213570, 'Flo Geneve':1091914804213570}

global game_dic
game_dic = {}

def get_fb_name(id):
    graph = facebook.GraphAPI(PAT)
    profile = graph.get_object(id=id)
    print profile
    user = profile['first_name'] + ' ' + profile['last_name']
    return user

def get_fb_id(name):
    graph = facebook.GraphAPI(PAT)
    profile = graph.get_object(name)
    return profile['id']

@app.route('/', methods=['GET'])
def handle_verification():
    print "Handling Verification"
    if request.args.get('hub.verify_token', '') == PAT:
      print "Verification successful!"
      return request.args.get('hub.challenge', '')
    else:
      print "Verification failed!"
      return 'Error, wrong validation token'

@app.route('/', methods=['POST'])
def handle_messages():
  print "Handling Messages"
  payload = request.get_data()
  print payload

  for sender, message in messaging_events(payload):
    fb_name = get_fb_name(sender)
    print "Incoming from %s: %s" % (fb_name, message)
    print message.split('-')

    if message.split('-')[0] in ['PRS']:
        game = message.split('-')[1]
        choice = message.split('-')[2]
        send_message(PAT, sender, 'OK you played: ' + choice)

        game_dic[sender]=[game,choice]
        print game_dic

        if len(game_dic) == 1:
            send_message(PAT, sender, 'Now Waiting for a courageous opponent...')
        elif len(game_dic) == 2:
            send_message(PAT, sender, 'You will play against ' + str(game_dic))


        #schedule.every(1).seconds.do(send_message(PAT, sender, 'Still waiting...'))

    else:
        send_message(PAT, sender, message[::-1])


  return "ok"


def messaging_events(payload):
  """Generate tuples of (sender_id, message_text) from the
  provided payload.
  """
  data = json.loads(payload)
  messaging_events = data["entry"][0]["messaging"]
  for event in messaging_events:
    if "message" in event and "text" in event["message"]:
      yield event["sender"]["id"], event["message"]["text"].encode('unicode_escape')
    else:
      yield event["sender"]["id"], "I can't echo this"


def send_message(token, recipient, text):
  """Send the message text to recipient with id recipient.
  """
  print 'response: ' + text
  r = requests.post("https://graph.facebook.com/v2.6/me/messages",
    params={"access_token": token},
    data=json.dumps({
      "recipient": {"id": recipient},
      "message": {"text": text.decode('unicode_escape')}
    }),
    headers={'Content-type': 'application/json'})
  if r.status_code != requests.codes.ok:
    print r.text



if __name__ == '__main__':
  app.run()