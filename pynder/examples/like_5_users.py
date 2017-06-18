import itertools
import pynder

FBID = "658958662"
FBTOKEN= "EAAGm0PX4ZCpsBADiU48wUTvAudSNOXSVlWyFjfopeAKGgaISj4JZA4GZAM0QCbKZAfW2nwnyFoUzz2GUtYUTDdL17NLZBEuTDw41hLA3j2MiPLcQc8dQZCAlV194gEjxUWWrbjF8Ri7L1WeEMsZBGKZB7neuTObha4hpQzIhVbfKRHGTFN2uZCF59CoNR2Nx8slIZD"


# https://www.facebook.com/dialog/oauth?client_id=464891386855067&redirect_uri=fbconnect://success&scope=basic_info%2Cemail%2Cpublic_profile%2Cuser_about_me%2Cuser_activities%2Cuser_birthday%2Cuser_education_history%2Cuser_friends%2Cuser_interests%2Cuser_likes%2Cuser_location%2Cuser_photos%2Cuser_relationship_details&response_type=token&__mref=message


session = pynder.Session(facebook_id=FBID, facebook_token=FBTOKEN)




users = session.nearby_users()
print users

for user in itertools.islice(users,1):
    print user.name
    print user.bio
    print user.age
    print user.ping_time
    print user.jobs
    for i in user.get_photos(width="640"):
        print i

    #print user.like()

matches = session.matches()
print matches
print dir(matches)

# for user in itertools.islice(matches,5):
#     print dir(user)
#     print user.id
#     print user.user.name
#     print user.match_date
#     print user.user.bio
#     #user.user.photos
#     user.user.thumbnail #a list of thumbnails of photo URLS


