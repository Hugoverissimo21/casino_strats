import pandas as pd # library for data analysis
import requests # library to handle requests
from bs4 import BeautifulSoup # library to parse HTML documents

def numbers_and_wins():
    filename = "a numbers.csv"
    file = open(filename,"w")
    file.write("Number,Wins\n")
    for b in range(37):
        wins = []
        string = str(b)+","
        wins.append(b)
        if b != 0:
            if b%2 == 0:
                wins.append("Even")
            else:
                wins.append("Odd")
                """Red,"32, 19, 21, 25, 34, 27, 36, 30, 23, 5, 16, 1, 14, 9, 18, 7, 12, 3",1 to 1
                Black,"15, 4, 2, 17, 6, 13, 11, 8, 10, 24, 33, 20, 31, 22, 29, 28, 35, 26",1 to 1"""
            if str(b) in "32, 19, 21, 25, 34, 27, 36, 30, 23, 5, 16, 1, 14, 9, 18, 7, 12, 3".split(", "):
                wins.append("Red")
            else:
                wins.append("Black")
            if b <13:
                wins.append("1st dozen")
            elif b>24:
                wins.append("3rd dozen")
            else:
                wins.append("2nd dozen")
        if b == 36:
            string += '"' + str(wins).replace("'","") + '"'
        else:
            string += '"' + str(wins).replace("'","") + '"' + "\n"
        file.write(string)
    file.close()
numbers_and_wins()

def win_to_payout():
    x = "a payouts.csv"
    file = open(x,"w")
    file.write("Win,Payout\n")
    file.write("1st dozen,2:1\n")
    file.write("2nd dozen,2:1\n")
    file.write("3rd dozen,2:1\n")
    file.write("Black,1:1\n")
    file.write("Red,1:1\n")
    for a in range(37):
        if a == 36:
            string = str(a) + "," + "35:1"
            file.write(string)
        else:
            string = str(a) + "," + "35:1" +"\n"
            file.write(string)
    file.close()
"""
# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/Roulette"
table_class="wikitable"
response=requests.get(wikiurl)
print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find('table',{'class':"wikitable"})
df=pd.read_html(str(indiatable))

# convert list to dataframe
df=pd.DataFrame(df[0])
print(df.head())
print("")
print(df)
««»»""""""""""""
url="https://en.wikipedia.org/wiki/Roulette"
table = pd.read_html(url)[1]
#Bet name,Winning spaces,Payout,Odds against winning (French),
#Expected value(on a $1 bet) (French),Odds against winning (American),Expected value(on a $1 bet) (American)
table = table[["Bet name","Winning spaces","Payout"]]
print(table)
table.to_csv("odds.csv" , index = False)

#a = pd.read_csv("odds.csv")
#print(a)
"""
"""df = pd.read_csv("numbers.csv")
#df["Number"] = range(37)
print(df)
#df.to_csv("numbers.csv" , index = False)"""
