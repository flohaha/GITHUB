import pynder

FBID = "658958662"
FBTOKEN= "EAAGm0PX4ZCpsBANCbQdIqUAz6UmZBRKpbgjYsQjB5yDoZCmaA030N4CxVb5rkDgqZCWQEQ4Lo9Pa53HYkW4RNZAm3B9yrPNQkOPQQWcONZCtpjxZBZBbb9NnNdJGgdffqnSTzRQ7fRwGeo5DQxjdjCcMtIvSNLQRDx6G8JZCWZCDpS8o7LIcasQl6ZCWZAIz5JYOQTXzMOcqREXvwYYXGwbQJZCDT87ztxZAeApyfawhLeUM9kZAiDh4AAooUK1os85wVmOpLQZD"

session = pynder.Session(facebook_id=FBID, facebook_token=FBTOKEN)
friends = session.get_fb_friends()

print(", ".join([x.name for x in friends]))