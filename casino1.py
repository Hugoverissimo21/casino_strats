from random import randint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def roullete_roll():
    df = pd.read_csv("a numbers.csv")
    #df = df.set_index('Number')
    output = randint(0, 36)
    wins = df.loc[df["Number"] == output]["Wins"]
    wins = wins.to_numpy()[0]
    wins = wins.strip("[").strip("]").split(", ")
    return wins #output = ['20', 'Even', 'Black', '2nd dozen'] & type = <class 'list'>

def strat_outcome_balance_stats(rolls = 750):
    """
    start bet + estrategia + saldo + rodar roleta
    """
    bet = [["Black", "Even", "Odd", "Red"] , [1, 1, 1, 1]]
    balance = -1*sum(bet[1])
    list_balance = [balance]
    for roll in range(rolls):
        result = roullete_roll()
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
        #############################
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
        list_balance.append(balance)
    plt.figure()
    plt.plot(range(len(list_balance)), list_balance, '-r',)
    plt.title("L*2 & W=1 - Black, Red, Odd, Even [" + str(rolls) + " rolls]", loc = "left")
    str_min_P = '('+str(list(range(len(list_balance)))[list_balance.index(min(list_balance))])+", "+str(min(list_balance))+')'
    txt_desvio = 10 if list(range(len(list_balance)))[list_balance.index(min(list_balance))] < rolls/2 else -10
    plt.text(list(range(len(list_balance)))[list_balance.index(min(list_balance))]+10, min(list_balance), str_min_P)
    plt.xlabel("Time in rolls")
    plt.ylabel("Balance")
    plt.show()
#strat_outcome_balance_stats()

def only_red_bet(rolls = 500):
    bet = [["Red"],[1]]
    balance = -1*bet[1][0]
    list_balance = [balance]
    for roll in range(rolls):
        result = roullete_roll()
        if "Red" in result:
            balance += bet[1][0]
            bet[1][0] = 1
        else:
            balance += -1*bet[1][0]
            bet[1][0] = bet[1][0]*2
        list_balance.append(balance)
    plt.figure()
    plt.plot(range(len(list_balance)), list_balance, '-r',)
    plt.title("L*2 & W=1 - Black, Red, Odd, Even [" + str(rolls) + " rolls]", loc = "left")
    str_min_P = '('+str(list(range(len(list_balance)))[list_balance.index(min(list_balance))])+", "+str(min(list_balance))+')'
    txt_desvio = 10 if list(range(len(list_balance)))[list_balance.index(min(list_balance))] < rolls/2 else -10
    plt.text(list(range(len(list_balance)))[list_balance.index(min(list_balance))]+10, min(list_balance), str_min_P)
    plt.xlabel("Time in rolls")
    plt.ylabel("Balance")
    plt.show()
#only_red_bet()

def plus_one(rolls = 750):
        bet = [["Red"] , [1]]
        balance = -1*sum(bet[1])
        list_balance = [balance]
        for roll in range(rolls):
            result = roullete_roll()
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
            list_balance.append(balance)
        plt.figure()
        plt.plot(range(len(list_balance)), list_balance, '-r',)
        final_balance_str = "Final Bal. = "+ str(list_balance[-1]) + "$"
        plt.title("W-=1 & L+=1 - only Red [" + str(rolls) + " rolls] | " + final_balance_str, loc = "left")
        str_min_P = '('+str(list(range(len(list_balance)))[list_balance.index(min(list_balance))])+", "+str(min(list_balance))+')'
        txt_desvio = 10 if list(range(len(list_balance)))[list_balance.index(min(list_balance))] < rolls/2 else -10
        plt.text(list(range(len(list_balance)))[list_balance.index(min(list_balance))]+10, min(list_balance), str_min_P)
        plt.xlabel("Time in rolls")
        plt.ylabel("Balance")
        plt.show()
#plus_one()

def fibonnaci(rolls = 750):
    fibonnaci_sequence = [1,2,3,5]
    bet = [["Red"] , [fibonnaci_sequence[0]]]
    balance = -1*sum(bet[1])
    list_balance = [balance]
    for roll in range(rolls):
        result = roullete_roll()
        if "Red" in result:
            balance += bet[1][0]
            if bet[1][0] == fibonnaci_sequence[0]:
                pass
            elif bet[1][0] == fibonnaci_sequence[1]:
                bet[1][0] == fibonnaci_sequence[0]
            else:
                bet[1][0] = fibonnaci_sequence[fibonnaci_sequence.index(bet[1][0])-2]
        else:
            balance -= bet[1][0]
            if bet[1][0] == fibonnaci_sequence[-2]:
                fibonnaci_sequence.append(fibonnaci_sequence[-1] + fibonnaci_sequence[-2])
            else:
                pass
            bet[1][0] = fibonnaci_sequence[fibonnaci_sequence.index(bet[1][0])+1]
        list_balance.append(balance)
    plt.figure()
    plt.plot(range(len(list_balance)), list_balance, '-r',)
    final_balance_str = "Final Bal. = "+ str(list_balance[-1]) + "$"
    plt.title("Fibonnaci - only Red [" + str(rolls) + " rolls] | " + final_balance_str, loc = "left")
    str_min_P = '('+str(list(range(len(list_balance)))[list_balance.index(min(list_balance))])+", "+str(min(list_balance))+')'
    txt_desvio = 10 if list(range(len(list_balance)))[list_balance.index(min(list_balance))] < rolls/2 else -10
    plt.text(list(range(len(list_balance)))[list_balance.index(min(list_balance))]+10, min(list_balance), str_min_P)
    plt.xlabel("Time in rolls")
    plt.ylabel("Balance")
    plt.show()

#####################################################
######################## RUN ########################
################ DELETE 2ND # TO RUN ################
#####################################################

# L*2 & W=1 - Black, Red, Odd, Even
#strat_outcome_balance_stats(rolls = 750)

# L*2 & W=1 - Red
#only_red_bet(rolls = 750)

# L+1 & W+1 - Red
#plus_one(rolls = 750)

# Fibonnaci - Red
fibonnaci(rolls = 750)
