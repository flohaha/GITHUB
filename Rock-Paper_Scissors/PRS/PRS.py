import sys, random, os


def battle_duo(users_list, win):

    import os, getpass, datetime

    timestamp = f=datetime.datetime.utcnow()

    #os.system('clear')

    # win=""
    # win = raw_input("How many runs to win? \t")
    # while win.isalpha():
    #     win = raw_input("Please enter a valid number of runs to win? \t")

    user1 = users_list[0]

    if len(users_list) == 2:
        user2 = users_list[1]
    else:
        user2 = "RANDOM"

    choice_user1 = ''
    choice_user2 = ''
    user1_win = 0
    user2_win = 0
    i = 0
    win = int(win)
    choices = ['P', 'R', 'S']

    result = []

    while user1_win < win and user2_win < win :

        i += 1

        if user1[0:6] == 'RANDOM':
            rand = random.randint(0, 2)
            choice_user1 = choices[rand]
        else:
            choice_user1 = getpass.getpass(user1 + ": Please select your Choice: Rock [R] / Paper [P] / Scissors [S]").upper()
            while choice_user1 not in choices:
                choice_user1 = getpass.getpass("Your choice is not valid, Please select your Choice: Rock [R] / Paper [P] / Scissors [S]").upper()

        if len(users_list) == 2:
            if user2[0:6] == 'RANDOM':
                rand = random.randint(0, 2)
                choice_user2 = choices[rand]
            else:
                choice_user2 = getpass.getpass(user2 + ": Please select your Choice: Rock [R] / Paper [P] / Scissors [S]").upper()
                while choice_user2 not in choices:
                    choice_user2 = getpass.getpass("Your choice is not valid, Please select your Choice: Rock [R] / Paper [P] / Scissors [S]").upper()

        elif len(users_list) == 1:
            rand = random.randint(0,2)
            choice_user2 = choices[rand]


        print "-------------------------- RUN " + str(i) + "-----------------------------------"
        print user1 + ": " + choice_user1 + " vs " + user2 + ": " + choice_user2

        if (choice_user1 == choice_user2):
            print "It's a TIGHT"
            print user1 + ": " + str(user1_win) + " vs " + user2 + ": " + str(user1_win)
            result.append((i,choice_user1,choice_user2))


        if (choice_user1 == 'R' and choice_user2 == 'S') or (choice_user1 == 'P' and choice_user2 == 'R') or (choice_user1 == 'S' and choice_user2 == 'P'):
            user1_win = user1_win + 1
            print user1 + " WIN this Run"
            print user1 + ": " + str(user1_win) + " vs " + user2 +  ": " + str(user2_win)
            result.append((i, choice_user1, choice_user2))

        if (choice_user1 == 'S' and choice_user2 == 'R') or (choice_user1 == 'R' and choice_user2 == 'P') or (choice_user1 == 'P' and choice_user2 == 'S'):
            user2_win = user2_win + 1
            print user2 + " WIN this Run"
            print user1 + ": " + str(user1_win) + " vs " +  user2 + ": " + str(user2_win)
            result.append((i, choice_user1, choice_user2))

    if user1_win == win:
        print "\n------------------------------------------------------------"
        print user1 + " WIN " + " : " + str(user1_win)
        print user2 + " LOSE: "+ str(user2_win)
        print "-------------------------------------------------------------"
        result_final = ((user1,user2,win, timestamp),result,(i,user1))

    if user2_win == win:
        print "\n------------------------------------------------------------"
        print user2 + " WIN " + " : " + str(user2_win)
        print user1 + " LOSE: " + str(user1_win)
        print "-------------------------------------------------------------\n"
        result_final = ((user1,user2,win, timestamp),result,(i,user2))

    return result_final



def battle_multi(users_list):

    import os, getpass, datetime

    timestamp = f=datetime.datetime.utcnow()

    #os.system('clear')

    i = 0
    choices = ['P', 'R', 'S']
    choices_dic = {}

    win_list = users_list


    while len(win_list) > 2:

        i += 1

        print "-------------------------- RUN " + str(i) + "-----------------------------------"

        r=0
        choices_dic = {}

        for u in win_list:

            if u[0:6]  == 'RANDOM':
                rand = random.randint(0, 2)
                choice = choices[rand]
                choices_dic[u] = choice
            else:
                choice = getpass.getpass(u + ": Please select your Choice: Rock [R] / Paper [P] / Scissors [S]").upper()
                while choice not in choices:
                    choice = getpass.getpass("Your choice is not valid, Please select your Choice: Rock [R] / Paper [P] / Scissors [S]").upper()

                choices_dic[u] = choice

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
        _
        print "Paper: " + str(P_count) + " - Victories: " + str(R_count)
        print "Rock: " + str(R_count) + " - Victories: " + str(S_count)
        print "Scissor: " + str(S_count) + " - Victories: " + str(P_count)

        if (P_count == R_count and R_count ==  S_count) or (P_count == R_count and S_count == 0) or (P_count == S_count and R_count == 0) or (Sz_count == R_count and P_count == 0)  :
            print "IT'S A TIGHT - KEEP PLAYING"
            winner = "NULL"

        elif P_count > S_count and P_count > R_count:
            if S_count > 0:
                print "SCISSOR WINS (" + str(S_count) + ")"
                winner = "S"
            else :
                print "PAPER WINS (" + str(P_count) + ")"
                winner = "P"

        elif R_count > S_count and R_count > S_count:
            if P_count > 0:
                print "PAPER WINS (" + str(P_count) + ")"
                winner = "P"
            else:
                print "ROCK WINS (" + str(R_count) + ")"
                winner = "R"

        elif S_count > P_count and S_count > R_count:
            if R_count > 0:
                print "ROCK WINS (" + str(R_count) + ")"
                winner = "R"
            else:
                print "SCISSOR WINS (" + str(S_count) + ")"
                winner = "S"



        win_dic = {}
        for c in choices_dic:
            win=0
            for d in choices_dic:
                if  c == d:
                    continue
                else:
                    if (choices_dic[c] == choices_dic[d]):
                        continue
                    elif (choices_dic[c] == 'R' and choices_dic[d] == 'S') or (choices_dic[c] == 'P' and choices_dic[d] == 'R') or (choices_dic[c] == 'S' and choices_dic[d] == 'P'):
                        win += 1
                win_dic[c] = win
            print c + " Victories: " + str(win)


        if len(win_dic) == 0:
            max_win = 0
            win_list = users_list
            lose_list = []
        else:
            win_list_tmp = []
            lose_list_tmp = []
            max_win = max(win_dic.values())

            for u in win_list:
                if win_dic[u] == max_win:
                    win_list_tmp.append(u)
                elif win_dic[u] < max_win:
                    lose_list_tmp.append(u)

        print "Still in the Game (" + str(len(win_list_tmp)) + "): \n" # + str(win_list_tmp)
        print "Go home (" + str(len(lose_list_tmp)) + "): \n " #+ str(lose_list_tmp)

        non_random = 0
        for w in win_list_tmp:
            if len(w)<6 or w[0:6]<>"RANDOM":
                non_random += 1

        if non_random == 0:
            print "\n-----------------------------------------------------------"
            print "SORRY YOU'VE LOST"
            print "-----------------------------------------------------------\n"
            return


        win_list = win_list_tmp
        lose_list = lose_list_tmp

    if len(win_list) == 1:
        if str(win_list[0][0:6]) <> "RANDOM":
            print "\n-----------------------------------------------------------"
            print "CONGRATS " + str(win_list[0]).upper() + " YOU WIN !!!"
            print "-----------------------------------------------------------\n"
        else:
            print "\n-----------------------------------------------------------"
            print "SORRY YOU'VE LOST"
            print "-----------------------------------------------------------\n"
            return


    if len(win_list) == 2:
        print "\n-----------------------------------------------------------"
        if win_list[0][0:6] == "RANDOM" and win_list[1][0:6] == "RANDOM":
            print "SORRY YOU'VE LOST"
            print "-----------------------------------------------------------\n"
            return
        else:
            print "\n-----------------------------------------------------------"
            print str(win_list[0]).upper() + " and " + str(win_list[1]).upper() + " have reached the final in battle mode"
            print "-----------------------------------------------------------\n"
            win = ""
            win = raw_input("How many runs to win the final? \t")
            while win.isalpha():
                win = raw_input("Please enter a valid number of runs to win? \t")
            battle_duo(win_list)


#
# os.system('clear')
#
# user_games_list = []
# more = "Y"
#
#
# while more == "Y":
#     user = raw_input("Enter your user name\t")
#     while user in [u[0] for u in user_games_list]:
#         user = raw_input("This user name is already selected, please enter another one\t")
#     #pwd = raw_input("Hi " + user + ", Can you please give me the Game Password\t")
#     pwd = 'Game1'
#
#     user_games_list.append((user, pwd))
#
#     more = raw_input("Will there be another player joining?[Y/N] \t")
#
# games_list = [g[1] for g in user_games_list]
#
# games_list_unique = []
#
# for g in games_list:
#     if g not in games_list_unique:
#         games_list_unique.append(g)
#
# #print games_list_unique
#
# print "\nThere will be " + str(len(user_games_list)) + " player(s) in the Game: "
# all_users = ""
# users_list = []
# for u in [u[0] for u in user_games_list]:
#     users_list.append(u)
#     all_users = all_users + ", " + u
# print all_users[2:]
# print "May the best one win!!! \n"



## testing


os.system('clear')

#users_list = ['Flo','JC','Bernard','Charles','Marc']


game = raw_input("Please enter the type of game want to play: \n"
                 "(1) Duel (1 vs 1) \n"
                 "(2) Championship (multi-player) \n"
                 "(3) Battle Royal (multi-player) \n")

opponent = raw_input("Please enter the type of opponent you want to play against: \n"
                 "(1) Man vs Machine \n"
                 "(2) Man vs Man \n")



users_list=[]
for i in range(0,200):
    users_list.append('RANDOM_'+str(i))
users_list.append('Flo')

if len(users_list) <= 2:
    more = "Y"
    while more == "Y":
        log = battle_duo(users_list)
        #print result
        more = raw_input("Do you want to play again? [Y/N]\t").upper()
        os.system('clear')
    print "Thanks for playing, see you soon"


elif len(users_list) > 2:
    more = "Y"
    while more == "Y":
        log = battle_multi(users_list)
        #print result
        more = raw_input("Do you want to play again? [Y/N]\t").upper()
        os.system('clear')
    print "Thanks for playing, see you soon"











