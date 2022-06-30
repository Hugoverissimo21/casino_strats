from random import randint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def roullete_roll():
    df = pd.read_csv("a numbers.csv")
    output = randint(0, 36)
    wins = df.loc[df["Number"] == output]["Wins"]
    wins = wins.to_numpy()[0]
    wins = wins.strip("[").strip("]").split(", ")
    return wins #output = ['20', 'Even', 'Black', '2nd dozen'] & type = <class 'list'>

#####################################################
###################### STRATS. ######################
#####################################################

def L2_W1_red_even_odd_black(result,balance,bet):
    if "Black" in result:
        balance += bet[1][0]
        balance += -1*bet[1][3]
        bet[1][0] = 1
        bet[1][3] = bet[1][3]*2
    else:
        balance += -1*bet[1][0]
        balance += bet[1][3]
        bet[1][0] = bet[1][0]*2
        bet[1][3] = 1
    if "Even" in result:
        balance += bet[1][1]
        balance += -1*bet[1][2]
        bet[1][1] = 1
        bet[1][2] = bet[1][2]*2
    else:
        balance += -1*bet[1][1]
        balance += bet[1][2]
        bet[1][1] = bet[1][1]*2
        bet[1][2] = 1
    return balance


def L2_W1_red(result,balance,bet):
    if "Red" in result:
        balance += bet[1][0]
        bet[1][0] = 1
    else:
        balance += -1*bet[1][0]
        bet[1][0] = bet[1][0]*2
    return balance

def Lsum1_Wsub1_red(result,balance,bet):
    if "Red" in result:
        balance += bet[1][0]
        bet[1][0] -= 1
        if bet[1][0] == 0:
            bet[1][0] += 1
        else:
            pass
    else:
        balance -= bet[1][0]
        bet[1][0] += 1
    return balance

def Fibonnaci_normal_red(result,balance,bet): #test only
    pass
    return balance

#####################################################
"""
#####################################################
# Tentar fazer strats infinitas e dar [[[FOR strat in strats:]]] ou algo do genero
# derivadas ou % para comparar melhor as strats ????
#####################################################
"""
def rolling(strat1, strat2, strat3, rolls = 250):  #, strat4):
    """
    strat1 = (strat name , strat bet)
        strat name = string with name of function
        strat bet = [[what,who],[x,y]]
            what & who = result possiblities
            x & y = int of betting in each result possiblities
    strat parameters should be result, balance, bet
    """
    strat1_bet = strat1[1]
    strat1_current_balance = sum(strat1_bet[1])*(-1)
    strat1_balance_list = [strat1_current_balance]
    strat2_bet = strat2[1]
    strat2_current_balance = sum(strat2_bet[1])*(-1)
    strat2_balance_list = [strat2_current_balance]
    strat3_bet = strat3[1]
    strat3_current_balance = sum(strat3_bet[1])*(-1)
    strat3_balance_list = [strat3_current_balance]
    #stratN_bet = stratN[1]
    #stratN_current_balance = sum(stratN_bet[1])*(-1)
    #stratN_balance_list = [stratN_current_balance]
    for roll in range(rolls):
        result = roullete_roll()
        strat1_current_balance = strat1[0](result,strat1_current_balance,strat1_bet)
        strat1_balance_list.append(strat1_current_balance)
        strat2_current_balance = strat2[0](result,strat2_current_balance,strat2_bet)
        strat2_balance_list.append(strat2_current_balance)
        strat3_current_balance = strat3[0](result,strat3_current_balance,strat3_bet)
        strat3_balance_list.append(strat3_current_balance)
        #stratN_current_balance = stratN[0](result,stratN_current_balance,stratN_bet)
        #stratN_balance_list.append(stratN_current_balance)
    y1 = strat1_balance_list
    y2 = strat2_balance_list
    y3 = strat3_balance_list
    #yN = stratN_balance_list
    x = range(rolls+1)
    fig = plt.gcf()
    fig.set_size_inches(14, 5)
    plt.xlabel('Time (rolls)')
    plt.ylabel('Balance')
    plt.plot(x, y1, label = str(strat1[0]).split()[1])
    plt.plot(x, y2, label = str(strat2[0]).split()[1])
    plt.plot(x, y3, label = str(strat3[0]).split()[1])
    #plt.plot(x, yN, label = str(stratN[0]).split()[1])
    plt.legend()
    plt.show()

#####################################################
######################## RUN ########################
#####################################################

strat1 = (L2_W1_red_even_odd_black,[["Black", "Even", "Odd", "Red"],[1, 1, 1, 1]])
strat2 = (L2_W1_red,[["Red"],[1]])
strat3 = (Lsum1_Wsub1_red,[["Red"],[1]])
#strat4 = (Fibonnaci_normal_red,)

rolling(strat1,strat2,strat3)
