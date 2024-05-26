#!/usr/bin/python3
import random
import time
import os
import sys
if os.name == 'nt':
	os.system('cls')
else:
	os.system('clear')
def end():
    print("Adiós perdedor!"u"\U0001F608")
    sys.exit()

ansers = ["No","Yes","Good choice! You need to do that!","hell NO!","I think you're going to regret...."u"\u2639","Of course Yes","Really?! leave me alone","Crossing my fingers for you"]

yepornot = input("I jes that you have a question, am I right?\nPlease make it short....(Yes or No) ")
if yepornot.lower() == "no":
    print("O.k it was nice meeting you")
    sys.exit()
elif yepornot.lower() == "yes" :
    print("O.k Just give me a second to be prepare")
    for i in range(1, 4):
        time.sleep(1)
        print(i)
    input("O.k now I am ready\nJust short...\n")
    regret = input("Now do you want to hear what I think?!\n(Yes or No)\n")
    if regret.lower() == "no":
        end()
    elif regret.lower() == "yes":
        print(random.choice(ansers))
        print(u"\u2661")
    else:
        end()
        while True:
            secend_question = input("You have more question?\n(Yes or No)\n")
            if secend_question.lower() == "no":
                print("Good by!"u"\U0001F493")
                sys.exit()
            elif secend_question.lower() == "yes":
                input("O.k shut"u"\u26BD")
                print(random.choice(ansers))
            else:
                end()
else:
    end()
