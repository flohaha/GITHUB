# -*- coding: UTF-8 -*-

import itertools
import pynder
import csv, os
import Pynder_Get_Authentication
import urllib
import stat
import datetime
from random import randint
from time import sleep
import math
import sys

print os.getcwd()

list = []
with open('FaceBook_Authentication_Aurelie21.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        list.append(row)

#print list[0][0]


email = list[0][2]
password='17flo0481'
FBID = list[0][3]
FBTOKEN = list[0][4]

print FBID
#print FBTOKEN

try:
    session = pynder.Session(facebook_id=FBID, facebook_token=FBTOKEN)

except:
    print 'get new token'
    token_new = Pynder_Get_Authentication.get_access_token(email, password)

    # Read in the file
    with open('FaceBook_Authentication_Aurelie21.csv', 'r') as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace(FBTOKEN, token_new)

    # Write the file out again
    with open('FaceBook_Authentication_Aurelie21.csv', 'w') as file:
        file.write(filedata)

    FBTOKEN = token_new


session = pynder.Session(facebook_id=FBID, facebook_token=FBTOKEN)

print FBTOKEN

# https://www.facebook.com/dialog/oauth?client_id=464891386855067&redirect_uri=fbconnect://success&scope=basic_info%2Cemail%2Cpublic_profile%2Cuser_about_me%2Cuser_activities%2Cuser_birthday%2Cuser_education_history%2Cuser_friends%2Cuser_interests%2Cuser_likes%2Cuser_location%2Cuser_photos%2Cuser_relationship_details&response_type=token&__mref=message


message_dic = {}

try:
    with open('message_list') as csvfile:
        readCSV = csv.reader(csvfile, delimiter='\t')

        for row in readCSV:

            if row[0] == FBID:

                if row[2] in message_dic:
                    #print message_dic[row[2]]
                    #print row[5]
                    if int(row[5]) > int(message_dic[row[2]]) :
                        message_dic[row[2]] = row[5]
                else:
                    message_dic[row[2]] = row[5]

except:
    message_dic = {}

print message_dic


response_dic = {}

with open('response_list') as csvfile:
    readCSV = csv.reader(csvfile, delimiter='\t')

    for row in readCSV:
        #print FBID
        #print row[0]
        #print str(row[0].strip()) == str(FBID.strip())

        if str(row[0].strip()) == str(FBID.strip()) :

            #print row[2]

            if row[2] in response_dic:

                #print response_dic[row[2]]

                try:
                    #print row[7]

                    if int(row[7]) > int(response_dic[row[2]]):
                        response_dic[row[2]] = row[7]
                except:
                    continue

            else:
                #print 'not in dic yet'
                try:
                    response_dic[row[2]] = row[7]
                except:
                    continue

            #print response_dic[row[2]]

            #print response_dic

            #print 'max resp = ' + str(response_dic[row[2]] )

print response_dic

#sys.exit("Error message")



tmstp = datetime.datetime.today().strftime('%Y%m%d_%H%M%S')

response = ['Coucou! Je suis nouvelle sur ce site et pour etre honnete, je cherche plutot a m amuser, et toi alors que fais tu ici?'.decode('utf-8')]
response.append('Moi je  suis sur Geneve, mais donne moi un peu envie avant ;)'.decode('utf-8'))
response.append('Ah  bien, tu m excites bien la! Dis moi ce que tu aimes le plus ... '.decode('utf-8'))
response.append('Allez je suis sure q tu peux faire mieux! Moi je suis une vraie cochonne! '.decode('utf-8'))
response.append('Dis moi la taille de ta bite et je te dis si on peut se rencontrer... '.decode('utf-8'))
response.append('Et toi tu voudrais savoir quoi sur moi alors??? '.decode('utf-8'))
response.append('Moi tous les mecs que je me suis fait me disent q je suis super bonne! ;) et surtout jadore le sexe... '.decode('utf-8'))
response.append('Envoi moi une photo un peu plus privee et si j aime on se fait un whatsapp? '.decode('utf-8'))
response.append('Allez une petite photo, j en peux plus! et apres on se fait une session whatsap! :) '.decode('utf-8'))
response.append('Ok cool, c est quoi ton numero whatsapp??? '.decode('utf-8'))
response.append('Bon j en peux plus, je me suis touchee et je tombe de fatigue. Je t ajoute demain alors. Mais hesite pas si tu veux m envoyer une photo en attendant... '.decode('utf-8'))
#print  response[0]


matches = session.matches()

count=0
for m in matches:
    count +=  1
print count

#count = 55

matches = session.matches()

loop = 50

loop_cnt = 1.0 * count / loop
print loop_cnt
loop_cnt = math.ceil(loop_cnt)
loop_cnt = int(loop_cnt)
print loop_cnt


for l in range(0,loop_cnt):

    print l
    loop_s = 0 + l
    loop_e = loop_s + loop


    for match in itertools.islice(matches,loop_s,loop_e):

        id = match.id
        name = match.user.name
        match_date = str(match.match_date)
        #print dir(match)
        print name


        message = match.messages

        m_numb = 0

        for m in message:

            result = [FBID, email, id, name, match_date]

            m = str(m)

            #print m_numb
            #print m

            if id in message_dic:
                cnt = message_dic[id]
                #print 'cnt_message log: ' + str(message_dic[id])
            else:
                cnt=0

            #print cnt

            #print m_numb + 1

            #print int(m_numb + 1) > int(cnt)

            #print m
            #print response[0]
            #print m == response[0]

            #print response
            #print m
            #print m.decode('utf-8') not in response


            if (int(m_numb ) > int(cnt) and m.decode('utf-8') not in response ) :
                print m
                result.append(str(m_numb))
                result.append(m.decode('utf-8'))

                result = '\t'.join(result)

                with open('message_list', 'a') as f:
                    f.write(result.encode('utf8') + '\n')
                    print 'writen messages'

                with open('Messages_Archive/message_list_' + tmstp, 'a') as f:
                    f.write(result.encode('utf8') + '\n')
                    print 'writen messages'

            m_numb = m_numb + 1
            #print m_numb

        #print m_numb

        #print response_dic[id]

        if id in response_dic:
            cnt_resp = response_dic[id]
        else:
            cnt_resp = -1

        print 'cnt_resp = ' + str(cnt_resp)

        if m_numb >= 1 and m.decode('utf-8') not in response :

            #print cnt_resp

            if  int(cnt_resp) == -1 :
                response_adapted = response[0]
                cnt_resp = 0

            elif int(cnt_resp) == 0:
                response_adapted = response[1]
                cnt_resp =1

            elif int(cnt_resp) == 1:
                response_adapted = response[2]
                cnt_resp = 2

            elif int(cnt_resp) == 2:
                response_adapted = response[3]
                cnt_resp = 3

            elif int(cnt_resp) == 3:
                response_adapted = response[4]
                cnt_resp = 4

            elif int(cnt_resp) == 4:
                response_adapted = response[5]
                cnt_resp = 5

            elif int(cnt_resp) == 5:
                response_adapted = response[6]
                cnt_resp = 6

            elif int(cnt_resp) == 6:
                response_adapted = response[7]
                cnt_resp = 7

            elif int(cnt_resp) == 7:
                response_adapted = response[8]
                cnt_resp = 8

            elif int(cnt_resp) == 8:
                response_adapted = response[9]
                cnt_resp = 9

            elif int(cnt_resp) == 9:
                response_adapted = response[10]
                cnt_resp = 10

            else:
                print 'response_adapted not defined: ' + str(cnt_resp)
                continue



            print 'cnt_resp new = ' + str(cnt_resp)

            response_log = []
            response_log = [FBID, email, id, name, match_date, str(cnt_resp), m.decode('utf-8')]
            #print str(m_numb)

            response_log.append(str(cnt_resp))
            response_log.append(response_adapted)
            response_log.append(tmstp)

            if cnt_resp <= 10 :
                print response_adapted

                response_log = '\t'.join(response_log).encode('utf-8').strip()

                with open('response_list', 'a') as f:
                    f.write(response_log + '\n')

                with open('Response_Archive/response_list_' + tmstp, 'a') as f:
                    f.write(response_log + '\n')

                match.message(response_adapted)

                print 'sent messages'

    print 'sleep a bit more : ' + str(l)
    sleep(randint(10, 20))

print 'this is the end  my friend'


