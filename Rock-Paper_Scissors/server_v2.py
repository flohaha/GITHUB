
from flask import Flask, request
import requests, facebook, random, json, schedule, time
from random import randint

#
# app = Flask(__name__)
#

app = Flask(__name__)

# This needs to be filled with the Page Access Token that will be provided
# by the Facebook App that will be created.
PAT = 'EAAOoaZCRNGOkBAOKr8sfaV05mQl3zbQhHKjIwgCDeTCrrSXgoMmJZCDRdrboJVRfPor7W6w9pusfMzZC5y4fFDPZCWaC2FDxXGf9Blcsq1Rg6xOTYZAucts1itbDsl9JaENrI5hC6VpCz1S4ZCxPjkw0JUctv7chZCKtlRi1YmC0gZDZD'



global game_dic
game_dic = {}
global game_dic_histo
game_dic_histo = {}
global game_dic_score
game_dic_score = {}

player_list = {}
player_list = {'1050840511630610': 'Flo Geneve', '1081427855265472': 'Flo Floh', '1077584518990390': u'Markus M\xfcller'}

gif_lose = ['https://media.giphy.com/media/ej2dS4FUCNRJK/giphy.gif','https://media.giphy.com/media/hUKiOsbuxdXa0/giphy.gif',
            'https://media1.giphy.com/media/BEob5qwFkSJ7G/200.gif','https://media0.giphy.com/media/YuEdUiDmey8W4/200.gif',
            'https://media2.giphy.com/media/TydZAW0DVCbGE/200.gif','https://media1.giphy.com/media/LnKa2WLkd6eAM/200.gif',
            'https://media1.giphy.com/media/G3dFISzqWT8is/200.gif']

gif_win = ['https://media.giphy.com/media/3o7TKJhBfNCiispgDm/giphy.gif','https://media.giphy.com/media/8WJw9kAG3wonu/giphy.gif',
           'https://media2.giphy.com/media/MJmQapwL7ABTG/200.gif','https://media4.giphy.com/media/LXHJRRjnviw7e/200.gif',
           'https://media4.giphy.com/media/rDbelKPujYEBq/200.gif','https://media4.giphy.com/media/2ZvQhiW2dup20/200.gif',
           'https://media1.giphy.com/media/Dps6uX4XPOKeA/200.gif']


player_suggestion_1 = player_list.values()[0]
player_suggestion_2 = player_list.values()[1]
player_suggestion_3 = player_list.values()[2]

global game_choice
game_choice = ['P','R','S']

def get_fb_name(id):
    graph = facebook.GraphAPI(PAT)
    profile = graph.get_object(id=id)
    print profile
    user = profile['first_name'] ## + ' ' + profile['last_name']
    return user

def get_fb_full_name(id):
    graph = facebook.GraphAPI(PAT)
    profile = graph.get_object(id=id)
    print profile
    user = profile['first_name'] + ' ' + profile['last_name']
    return user

def get_fb_id(name):
    graph = facebook.GraphAPI(PAT)
    profile = graph.get_object(name)
    return profile['id']

def reply_img(token, user_id, url):
    data = {
        "recipient": {"id": user_id},
        "message": {
            "attachment": {
                "type": "image",
                "payload": {
                    "url": url
                }
            }
        }
    }
    resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + token, json=data)
    print(resp.content)

def reply_template_whatgame1(token, user_id, title, subtitle, button1, payload1):
    data = {
        "recipient": {"id": user_id},
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [{
                        "title": title,
                        "subtitle": subtitle,
                        #"item_url": "https://www.oculus.com/en-us/rift/",
                        # image_url: "http://messengerdemo.parseapp.com/img/rift.png",
                        "buttons": [{
                            "type": "postback",
                            "title": button1,
                            "payload": payload1
                        }]
                    }]
                }
            }
        }
    }
    resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + token, json=data)
    print(resp.content)

def reply_template_whatgame2(token, user_id, title, subtitle, button1, payload1, button2, payload2):
    data = {
        "recipient": {"id": user_id},
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [{
                        "title": title,
                        "subtitle": subtitle,
                        #"item_url": "https://www.oculus.com/en-us/rift/",
                        # image_url: "http://messengerdemo.parseapp.com/img/rift.png",
                        "buttons": [{
                            "type": "postback",
                            "title": button1,
                            "payload": payload1
                        }, {
                            "type": "postback",
                            "title": button2,
                            "payload": payload2
                        }]
                    }]
                }
            }
        }
    }
    resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + token, json=data)
    print(resp.content)

def reply_template_whatgame3(token, user_id, title, subtitle, button1, payload1, button2, payload2, button3, payload3):
    data = {
        "recipient": {"id": user_id},
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [{
                        "title": title,
                        "subtitle": subtitle,
                        #"item_url": "https://www.oculus.com/en-us/rift/",
                        # image_url: "http://messengerdemo.parseapp.com/img/rift.png",
                        "buttons": [{
                            "type": "postback",
                            "title": button1,
                            "payload": payload1
                        }, {
                            "type": "postback",
                            "title": button2,
                            "payload": payload2
                        }, {
                            "type": "postback",
                            "title": button3,
                            "payload": payload3
                        }]
                    }]
                }
            }
        }
    }
    resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + token, json=data)
    print(resp.content)

def battle_multi(choices_dic):

    import os, getpass, datetime

    timestamp = datetime.datetime.utcnow()

    #os.system('clear')

    P_count = 0
    R_count = 0
    S_count = 0

    for c in choices_dic:
        if choices_dic[c] == 'P':
            P_count += 1
        elif choices_dic[c] == 'R':
            R_count += 1
        elif choices_dic[c] == 'S':
            S_count += 1

    #print "Paper: " + str(P_count)
    #print "Rock: " + str(R_count)
    #print "Scissor: " + str(S_count)

    win_dic = {}
    for c in choices_dic:
        win = 0
        for d in choices_dic:
            if c == d:
                continue
            else:
                if (choices_dic[c] == choices_dic[d]):
                    continue
                elif (choices_dic[c] == 'R' and choices_dic[d] == 'S') or (
                        choices_dic[c] == 'P' and choices_dic[d] == 'R') or (
                        choices_dic[c] == 'S' and choices_dic[d] == 'P'):
                    win += 1
            win_dic[c] = win
        print c + " Victories: " + str(win)

    if len(win_dic) == 0:
        max_win = 0
        win_list = choices_dic.keys()
        lose_list = []
    else:
        win_list = []
        lose_list = []
        max_win = max(win_dic.values())

        for u in win_dic:
            if win_dic[u] == max_win:
                win_list.append(u)
            elif win_dic[u] < max_win:
                lose_list.append(u)

    return [win_list,lose_list]


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

    print message

    fb_name = get_fb_name(sender)
    fb_full_name = get_fb_full_name(sender)

    player_list[sender] = fb_full_name
    print player_list

    print "Incoming from %s: %s" % (fb_name, message)


    ## Heads-Up
    if message == 'Heads-Up':
        game_dic[sender] = ''
        game_dic_score[sender] = 0
        game_dic_histo[sender] = []

        if len(game_dic) == 1:
            send_message(PAT, sender, 'Now Waiting for a courageous opponent...')
            send_message(PAT, sender, 'You can invite an opponent by typing @ and its full name (first and last) or click on our suggestion below:')
            reply_template_whatgame3(PAT, sender, 'Paper Rock Scissors', 'Opponent suggestions:', player_suggestion_1, '@'+player_suggestion_1, player_suggestion_2,
                                     '@'+player_suggestion_2, player_suggestion_3, '@'+player_suggestion_3)


        elif len(game_dic) == 2:
            for player in game_dic:
                players_list = game_dic.keys()
                opponent = [x for x in game_dic if x != player]
                opponent = opponent[0]
                send_message(PAT, player, 'You will play against ' + get_fb_name(opponent))
                reply_template_whatgame3(PAT, player, 'Paper Rock Scissors', 'What do you chose:', 'Paper', 'P', 'Rock','R', 'Scissors', 'S')

        else:
            send_message(PAT, sender, 'Sorry I dont handle multi-player yet, you will  have to wait...')


    ## TRASH TALK All: Starting with #
    elif message[0:1] == '#':
        for u in game_dic:
            if u != sender:
                send_message(PAT, u, message[1:])


    ## Player plays P-R-S
    elif message in game_choice:
        game_dic[sender] = message
        game_dic_histo[sender].append(message)

        print 'game_dic : ' + str(game_dic)

        if '' in game_dic.values():
            send_message(PAT, sender, 'Waiting for your opponent to chose...')
            send_message(PAT, sender, 'You can Trash Talk using # and your message')

        else:

            battle = battle_multi(game_dic)
            print 'battle result : ' + str(battle)

            if len(battle[1]) == 0:

                for u in battle[0]:
                    print 'Answer Player: ' + u
                    send_message(PAT, u, 'ITs A TIE - KEEP PLAYING')

                    score = ''
                    for s in game_dic_score:
                        score = score + '\n' + player_list[s] + ' : ' + str(game_dic_score[s])

                    send_message(PAT, u, 'Scores: ' + score )

                    reply_template_whatgame3(PAT, u, 'Paper Rock Scissors', 'What do you chose:', 'Paper', 'P',
                                             'Rock', 'R', 'Scissors', 'S')

                    game_dic[u] = ''

                    #   time.sleep(5)

                    print 'finished to answer to: ' + u

                battle = [[], []]





            elif len(battle[1]) > 0 :

                for u in battle[0]:
                    send_message(PAT, u, 'CONGRATS YOU WON')
                    url = gif_win[randint(0,5)]
                    reply_img(PAT, u, url)

                    time.sleep(3.5)

                    print game_dic_score[u]
                    game_dic_score[u] = 1 + game_dic_score[u]
                    print game_dic_score[u]

                    score=''
                    for s in game_dic_score:
                        score = score + '\n' + player_list[s] + ' : ' + str(game_dic_score[s])

                    send_message(PAT, u,
                                 'Scores: ' + score )

                    #time.sleep(0.5)

                    reply_template_whatgame2(PAT, u, 'Paper Rock Scissors', 'Play again?:', 'Yes, of course',
                                             'Yes, of course', 'No, later maybe', 'No, later maybe')

                    game_dic[u] = ''

                    #time.sleep(0.5)

                for u in battle[1]:
                    send_message(PAT, u, 'TOO BAD YOU LOSE')
                    url = gif_lose[randint(0, 5)]
                    reply_img(PAT, u, url)

                    #time.sleep(3.5)

                    score = ''
                    for s in game_dic_score:
                        score = score + '\n' + player_list[s] + ' : ' + str(game_dic_score[s])

                    send_message(PAT, u,
                                 'Scores: ' + score )

                    #time.sleep(0.5)

                    reply_template_whatgame2(PAT, u, 'Paper Rock Scissors', 'Play again?:', 'Yes, of course',
                                             'Yes, of course', 'No, later maybe','No, later maybe')

                    game_dic[u] = ''

                    #time.sleep(0.5)

                battle = [[], []]


    ## Invite Somebody to play with you
    elif message[0:1] == '@':
        if message[1:] in player_list.values():
            for p in player_list:
                if message[1:]  == player_list[p]:
                    send_message(PAT, p, fb_full_name + ' Challenges you! Are you ready to play?')
                    reply_template_whatgame1(PAT, p, 'Paper Rock Scissors', 'Chose your Game:', 'Heads-Up',
                                             'Heads-Up')

        else:
            send_message(PAT, sender, 'Sorry I don\'t know ' + message[1:] )
            send_message(PAT, sender, 'You Can tell him to like our page and send us a message')

        for u in game_dic:
            if u != sender:
                send_message(PAT, u, message[1:])


    ## SOLO
    elif message == 'Solo Training':
        send_message(PAT, sender, 'SOLO')

    ## Yes, of course
    elif message == 'Yes, of course':

        game_dic[sender] = message[0:1]

        if game_dic.values() == ['Y','Y'] :
            for u in game_dic:
                reply_template_whatgame3(PAT, u, 'Paper Rock Scissors', 'What do you chose:', 'Paper', 'P', 'Rock',
                                     'R', 'Scissors', 'S')


        else :
            send_message(PAT, sender, 'Now Waiting for your opponent...')
            send_message(PAT, sender, 'You can Trash Talk using # and your message')

    ## No, later maybe
    elif message == 'No, later maybe':
        send_message(PAT, sender, 'See you soon... ')
        game_dic.clear()
        game_dic_score.clear()
        game_dic_histo.clear()



    # new in game
    elif sender not in game_dic.keys() and message != 'Heads-Up':
        send_message(PAT, sender, 'Hi ' + fb_name)
        reply_template_whatgame1(PAT, sender, 'Paper Rock Scissors', 'Chose your Game:', 'Heads-Up', 'Heads-Up')


    else:
        send_message(PAT, sender, 'I\'m a bit lost sorry...')
        #reply_template_whatgame1(PAT, sender, 'Paper Rock Scissors', 'Chose your Game:', 'Heads-Up', 'Heads-Up')

  return "ok"


def messaging_events(payload):
  """Generate tuples of (sender_id, message_text) from the
  provided payload.
  """
  data = json.loads(payload)
  print data
  messaging_events = data["entry"][0]["messaging"]

  for event in messaging_events:

    if "message" in event and "text" in event["message"]:
      yield event["sender"]["id"], event["message"]["text"]

    elif "postback" in event and "payload" in event["postback"]:
      yield event["sender"]["id"], event["postback"]["payload"]

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
      "message": {"text": text}    #text.decode('unicode_escape')
    }),
    headers={'Content-type': 'application/json'})
  if r.status_code != requests.codes.ok:
    print r.text



if __name__ == '__main__':
  app.run()