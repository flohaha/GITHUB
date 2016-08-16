from flask import Flask, request
import requests


app = Flask(__name__)

ACCESS_TOKEN = "EAAOoaZCRNGOkBAOKr8sfaV05mQl3zbQhHKjIwgCDeTCrrSXgoMmJZCDRdrboJVRfPor7W6w9pusfMzZC5y4fFDPZCWaC2FDxXGf9Blcsq1Rg6xOTYZAucts1itbDsl9JaENrI5hC6VpCz1S4ZCxPjkw0JUctv7chZCKtlRi1YmC0gZDZD"


def get_fb_name(id):
    graph = facebook.GraphAPI(ACCESS_TOKEN)
    profile = graph.get_object(id=id)
    return profile['first_name']


def reply(user_id, msg):
    data = {
        "recipient": {"id": user_id},
        "message": {"text": msg}
    }
    resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + ACCESS_TOKEN, json=data)
    print(resp.content)


@app.route('/', methods=['POST'])
def handle_incoming_messages():
    print 'post request received'
    data = request.json
    print data
    sender = data['entry'][0]['messaging'][0]['sender']['id']
    message = data['entry'][0]['messaging'][0]['message']['text']
    reply(sender, message[::-1])

    return "ok"


if __name__ == '__main__':
    app.run(debug=True)