import itertools
import pynder
import csv, os
#import Pynder_Get_Authentication
import urllib
import stat
import datetime
from random import randint
from time import sleep
import sys
import  robobrowser, re


print os.getcwd()


def get_access_token(email, password):
    MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; U; en-gb; KFTHWI Build/JDQ39) AppleWebKit/535.19 (KHTML, like Gecko) Silk/3.16 Safari/535.19"
    FB_AUTH = "https://www.facebook.com/v2.6/dialog/oauth?redirect_uri=fb464891386855067%3A%2F%2Fauthorize%2F&display=touch&state=%7B%22challenge%22%3A%22IUUkEUqIGud332lfu%252BMJhxL4Wlc%253D%22%2C%220_auth_logger_id%22%3A%2230F06532-A1B9-4B10-BB28-B29956C71AB1%22%2C%22com.facebook.sdk_client_state%22%3Atrue%2C%223_method%22%3A%22sfvc_auth%22%7D&scope=user_birthday%2Cuser_photos%2Cuser_education_history%2Cemail%2Cuser_relationship_details%2Cuser_friends%2Cuser_work_history%2Cuser_likes&response_type=token%2Csigned_request&default_audience=friends&return_scopes=true&auth_type=rerequest&client_id=464891386855067&ret=login&sdk=ios&logger_id=30F06532-A1B9-4B10-BB28-B29956C71AB1&ext=1470840777&hash=AeZqkIcf-NEW6vBd"

    s = robobrowser.RoboBrowser(user_agent=MOBILE_USER_AGENT, parser="lxml")

    s.open(FB_AUTH)
    ##submit login form##
    f = s.get_form()

    f["pass"] = password
    f["email"] = email
    s.submit_form(f)

    ##click the 'ok' button on the dialog informing you that you have already authenticated with the Tinder app##
    f = s.get_form()

    s.submit_form(f, submit=f.submit_fields['__CONFIRM__'])
    ##get access token from the html response##

    access_token = re.search(r"access_token=([\w\d]+)", s.response.content.decode()).groups()[0]
    # print  s.response.content.decode()
    return access_token


def pynder_connect(token_file):

    list = []
    with open(token_file) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            list.append(row)

    print list[0][0]


    email = list[0][2]
    password='17flo0481'
    FBID = list[0][3]
    FBTOKEN= list[0][4]

    print FBID
    print email
    #print FBTOKEN

    try:
        session = pynder.Session(facebook_id=FBID, facebook_token=FBTOKEN)

    except:
        print 'session expired - get new token'
        token_new = get_access_token(email, password)

        # Read in the file
        with open(token_file, 'r') as file:
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace(FBTOKEN, token_new)

        # Write the file out again
        with open(token_file, 'w') as file:
            file.write(filedata)

        FBTOKEN = token_new


    session = pynder.Session(facebook_id=FBID, facebook_token=FBTOKEN)

    print 'Connection Successful'

    return {'FBID':FBID, 'FBTOKEN': FBTOKEN, 'email':email, 'session':session}


def swipes(FBID, FBTOKEN, email, session, swipeby, loopby):

    if session.likes_remaining ==  0:
        print 'no more likes'
        #sys.exit("Error message")
        return 0


    for j in range(0, loopby):

        users = session.nearby_users()

        tmstp = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')

        if session.likes_remaining == 0:
            print 'no more likes'
            #sys.exit("Error message")
            return int( j * (k+1) )

        k = 0

        for user in itertools.islice(users, swipeby):

            result = []

            try:
                name= user.name.encode('utf-8').replace('\n',' ').replace('\t',' ')
                print name
            except:
                name = 'NA'
            try:
                bio = user.bio.encode('utf-8').replace('\n',' ').replace('\t',' ')
                print bio
            except:
                bio = 'NA'
            try:
                age = str(user.age).encode('utf-8').replace('\n',' ').replace('\t',' ')
                print age
            except:
                age = 0
            try:
                last_ping = str(user.ping_time).encode('utf-8').replace('\n',' ').replace('\t',' ')
                print last_ping
            except:
                last_ping = 'NA'
            try:
                job = '|'.join(user.jobs).encode('utf-8').replace('\n',' ').replace('\t',' ')
                print job
            except:
                job='NA'

            photolist1=[]

            try:
                for i in user.get_photos(width="640"):
                    photolist1.append(i)
                photolist = '|'.join(photolist1).encode('utf-8').replace('\n',' ').replace('\t',' ')
                print photolist

            except:
                photolist = 'NA'

            try:
                connections = '|'.join(user.common_connections).encode('utf-8').replace('\n',' ').replace('\t',' ')
                print connections
            except:
                connections = 'NA'
            try:
                interests = '|'.join(user.common_interests).encode('utf-8').replace('\n',' ').replace('\t',' ')
                print interests
            except:
                interests = 'NA'
            try:
                schools = '|'.join(user.schools).encode('utf-8').replace('\n',' ').replace('\t',' ')
                print schools
            except:
                schools = 'NA'
            try:
                insta = '|'.join(user.instagram_username).encode('utf-8').replace('\n',' ').replace('\t',' ')
                print insta
            except:
                insta = 'NA'
            try:
                insta_pic = '|'.join(user.instagram_photos).encode('utf-8').replace('\n',' ').replace('\t',' ')
                print insta_pic
            except:
                insta_pic = 'NA'

            try:
                insta_name = user.instagram_username.encode('utf-8').replace('\n',' ').replace('\t',' ')
            except:
                insta_name = 'NA'

            gender = user.gender.encode('utf-8')
            id = str(user.id).encode('utf-8')

            #print dir(user)

            result = [FBID, email, id, name, bio, gender, age, last_ping,  job, photolist, connections, interests, schools, insta_name, insta, insta_pic ]

            result = '\t'.join(result)
            result = result + '\n'

            print result

            #print os.getcwd()

            with open('like_list', 'a') as f:
                f.write(result)

            with open('Like_List_Archive/like_list_' + tmstp , 'a') as f:
                f.write(result)

            print 'writen likes'

            #from glob import glob
            #print glob('*/')

            print str(stat.S_IMODE(os.stat('Pics').st_mode))

            if not os.path.exists('Pics/' + str(id) ):
                os.makedirs('Pics/' + str(id) , mode=0755)
            if oct(stat.S_IMODE(os.stat('Pics/' + str(id) ).st_mode)) != 0775:
                os.chmod('Pics/' + str(id) , 0775)

            with open('pic_list', 'a') as f:
                for i in photolist1:
                    print i
                    f.write(str(id) + '\t' + i + '\n')

                    urllib.urlretrieve(i, 'Pics/' + str(id) + '/' + i.replace('http://images.gotinder.com/','').replace('/','-'))


                print 'writen pic'


            print 'ok'


            if k == 13 and swipeby >= 20 :
                user.dislike()
                print 'ramdom swipe left'
            else:
                user.dislike()
                print 'swipe right'

            k = k + 1

            print 'sleep a bit : ' + str(k)
            sleep(randint(1, 7))

        #j = j+1
        print j

        print 'sleep a bit more : ' + str(j)
        sleep(randint(7, 21))

    return int( ( k * (j+1) ) )



# Connect using token csv file
token_file = 'FaceBook_Authentication_Aurelie21.csv'
pynder_connect = pynder_connect(token_file)

# Connected
session = pynder_connect['session']
FBID = pynder_connect['FBID']
FBTOKEN = pynder_connect['FBTOKEN']
email = pynder_connect['email']

print email
print session

swipeby = 2 # k
loopby = 1 # j
swipe = swipes(FBID, FBTOKEN, email, session, swipeby, loopby)

print 'Total Swipes: ' + str(swipe)





