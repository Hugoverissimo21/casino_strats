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
# derivadas ou % para comparar melhor as strats ????
#####################################################
"""
def rolling(*strats, rolls = 250):
    """
    strat1 = (strat name , strat bet)
        strat name = string with name of function
        strat bet = [[what,who],[x,y]]
            what & who = result possiblities
            x & y = int of betting in each result possiblities
    strat parameters should be result, balance, bet
    """
    stratN_bet = []
    stratN_current_balance = []
    stratN_balance_list = []
    for strat in strats:
        stratN_bet.append(strat[1])
        stratN_current_balance.append(sum(strat[1][1])*(-1))
        stratN_balance_list.append([sum(strat[1][1])*(-1)])
    for roll in range(rolls):
        strat_index = 0
        result = roullete_roll()
        for strat in strats:
            stratN_current_balance[strat_index] = strat[0](result,stratN_current_balance[strat_index],stratN_bet[strat_index])
            stratN_balance_list[strat_index].append(stratN_current_balance[strat_index])
            strat_index += 1
    strat_index = 0
    for strat in strats:
        x = range(rolls+1)
        y = stratN_balance_list[strat_index]
        plt.plot(x, y, label = str(strat[0]).split()[1])
        strat_index += 1
    fig = plt.gcf()
    fig.set_size_inches(14, 5)
    plt.xlabel('Time (rolls)')
    plt.ylabel('Balance')
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
