
import pynder

FBID = "658958662"
FBTOKEN= "EAAGm0PX4ZCpsBANCbQdIqUAz6UmZBRKpbgjYsQjB5yDoZCmaA030N4CxVb5rkDgqZCWQEQ4Lo9Pa53HYkW4RNZAm3B9yrPNQkOPQQWcONZCtpjxZBZBbb9NnNdJGgdffqnSTzRQ7fRwGeo5DQxjdjCcMtIvSNLQRDx6G8JZCWZCDpS8o7LIcasQl6ZCWZAIz5JYOQTXzMOcqREXvwYYXGwbQJZCDT87ztxZAeApyfawhLeUM9kZAiDh4AAooUK1os85wVmOpLQZD"

FBTOKEN = "EAAGm0PX4ZCpsBANdaPCJ1ZCtV4LZBZBsQenMS7PqZCt9TzSTjrHBvVvwEnPOpSrrjAeBpxXpAR9V83LQrceJVBdImDPnvoaZBPqb7rmhVhoKZAr9BaNbMYxhfl9F6DI5Jmd8l40oivhijo0OB0dx5o1R5ZBiSM1zHiVIKUxPvfnRbfuuszWqJ7JkTFBICf5U5sgZD"

# https://www.facebook.com/dialog/oauth?client_id=464891386855067&redirect_uri=fbconnect://success&scope=basic_info%2Cemail%2Cpublic_profile%2Cuser_about_me%2Cuser_activities%2Cuser_birthday%2Cuser_education_history%2Cuser_friends%2Cuser_interests%2Cuser_likes%2Cuser_location%2Cuser_photos%2Cuser_relationship_details&response_type=token&__mref=message

session = pynder.Session(facebook_id=FBID, facebook_token=FBTOKEN)
friends = session.get_fb_friends()

# Print the names of all facebook friends using Tinder Social.
print("Friends with Tinder:")
print(", ".join([x.name for x in friends]))

# Get the user_info of these facebook friends.
user_info_objects = []
for friend in friends:
    user_info_objects.append(friend.get_tinder_information())

# Print the bios.
print("im here")
for user_info, friend in zip(user_info_objects, friends):
    print("=" * 50)
    # Use Friend.name, as user_info.name only contains first name.
    print(friend.name)
    print(friend.facebook_link)
    print("-" * 50)
    print(user_info.bio)
    print("=" * 50)
