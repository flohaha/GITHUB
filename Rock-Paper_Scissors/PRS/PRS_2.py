import sys, random, os


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




choices_dic = {'flo':'P', 'jc':'R','flo2':'S'}

battle = battle_multi(choices_dic)

if len(battle[1]) == 0:
    print "IT'S A TIGHT - EVERYBODY HAS TO RE-PLAY"

else:
    for u in battle[0]:
        print u + ' (' + choices_dic[u] + ')' + ' KEEPS PLAYING'
    for u in battle[1]:
        print u + ' (' + choices_dic[u] + ')' + ' GO HOME'

#print battle







