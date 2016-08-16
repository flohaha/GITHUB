from flask import Flask, request
import requests, facebook, random

#
# app = Flask(__name__)



app = Flask(__name__)

ACCESS_TOKEN = "EAAOoaZCRNGOkBAOKr8sfaV05mQl3zbQhHKjIwgCDeTCrrSXgoMmJZCDRdrboJVRfPor7W6w9pusfMzZC5y4fFDPZCWaC2FDxXGf9Blcsq1Rg6xOTYZAucts1itbDsl9JaENrI5hC6VpCz1S4ZCxPjkw0JUctv7chZCKtlRi1YmC0gZDZD"

def reply(user_id, msg):
    data = {
        "recipient": {"id": user_id},
        "message": {"text": msg}
    }
    resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + ACCESS_TOKEN, json=data)
    print(resp.content)

def reply_template_whatgame(user_id, title, subtitle, button1, payload1, button2, payload2, button3, payload3):
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
    resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + ACCESS_TOKEN, json=data)
    print(resp.content)

def get_fb_name(id):
    graph = facebook.GraphAPI(ACCESS_TOKEN)
    profile = graph.get_object(id=id)
    return profile['first_name']

#
#
# @app.route('/', methods=['GET'])
# def handle_verification():
#     print "Verification Successful!"
#     return request.args['hub.challenge']
#
# #


@app.route('/', methods=['POST'])

def handle_incoming_messages():

    print 'HI'
    #
    # data = request.json
    #
    # print data
    #
    # sender = data['entry'][0]['messaging'][0]['sender']['id']
    #
    # try:
    #     message = data['entry'][0]['messaging'][0]['message']['text']
    # except:
    #     message = 'no message'
    #
    # try:
    #     messageAttachments = data['entry'][0]['messaging'][0]['message']['attachments']
    # except:
    #     messageAttachments = 'no attachment'
    #
    #
    # try:
    #     name = get_fb_name(sender)
    # except:
    #     message = 'Yo! Sorry I didn''t get your name right... ;{ '
    #     reply(sender, message)
    #     return "ok"
    #
    # if 'PRS' in message:
    #     reply_template_whatgame(sender, 'Paper Rock Scissors', 'Chose your Game:', 'Solo Training', 'Solo Training',
    #                             'Heads-Up', 'Heads-Up', 'Multi-Player', 'Multi-Player')
    #
    # elif message <> 'no message':
    #     reply(sender, 'Sorry something got wrong... :{ ')
    #
    #
    # elif name == 'Rachael':
    #
    #     try:
    #
    #         message1 = 'Hi ' + name + ', Flo is gonna miss you a lot'
    #         message2 = 'Hi ' + name + ', Flo had a great weekend with you'
    #         message3 = 'Hi ' + name + ', Flo likes you BJs a lot'
    #         message4 = 'Hi ' + name + ', Flo enjoys getting you ass'
    #         message5 = 'Hi ' + name + ', Flo is happy he came this weekend'
    #         message6 = 'Hi ' + name + ', Flo is looking forward to your nex weekends'
    #
    #         rand = random.randint(1,6)
    #
    #         exec("%s = %s" % ('message','message'+str(rand)))
    #
    #
    #     except:
    #         message = 'Yo! Sorry something went wrong... ;{ '
    #
    #     reply(sender, message)
    #
    # elif name == 'Flo' :
    #
    #     try:
    #         name = get_fb_name(sender)
    #         #message = 'Hi ' + name +' JE REPETE: '+ data['entry'][0]['messaging'][0]['message']['text']
    #         reply_template_whatgame(sender, 'Paper Rock Scissors','Chose your Game:', 'Solo Training', 'Solo Training', 'Heads-Up', 'Heads-Up', 'Multi-Player','Multi-Player')
    #
    #     except:
    #         message = 'Yo! Sorry something went wrong... ;{ '

    return "ok"



if __name__ == '__main__':
    app.run(debug=True)