## BUDGET ANALYSIS (v2)

import sys
import time

stored = {}
total_list = [0]
budget_store = [0]

def updt(total, progress): # -------------------- PROGRESS BAR CODE ------------------------

    barLength, status = 20, ""
    progress = float(progress) / float(total)
    if progress >= 1.:
        progress, status = 1, "\r\n"
    block = int(round(barLength * progress))
    text = "\r[{}] {:.0f}% {}".format(
        "■" * block + "-" * (barLength - block), round(progress * 100, 0),
        status)
    sys.stdout.write(text)
    sys.stdout.flush()

runs = 50 # -------------------- TIME SELECT ---------------------------

def chart(stored): # -------------------- CHART ------------------------
    print('ITEM \t\t COST')
    print('-'*25)
    for item in stored:
        print(item, '\t\t',stored[item])

def item_add(item_input, cost_input): # -------------------- ITEM ADD ------------------------

    if item_input.isalpha() == True and cost_input >= 0:
        stored[item_input] = cost_input

        print('_'*75)
        user_input = input("Do you want to continue entering budget items? Enter yes or no: ").lower()

        print(user_input)
        print('_'*75)

        loop(user_input)

    else:
        print("ERROR1")

def loop(user_input): # -------------------- CONTINUE ENTER CHECK ------------------------

    while user_input == 'yes' or user_input == 'y':
        print('_'*75)
        item_input, cost_input = input("Please enter the item to add to your budget and the cost of that item: ").split()
        print('_'*75)

        item_input = str(item_input).lower()
        cost_input = int(cost_input)

        chart(stored)
        item_add(item_input, cost_input)

    if user_input == 'no' or user_input == 'n':
        print('_'*75)
        print("Program ENDED")
        print('_'*75)
        chart(stored)
        budget_check()

    else:
        print('_'*75)
        print("You did not select Yes or No. Program ENDED")
        print('_'*75)
        chart(stored)
        sys.exit()

def budget(budget_store): # -------------------- BUDGET ENTER ------------------------
    print('_'*75)
    budget_input = input("Please enter your budget for this month: ")
    print("You entered: ","$",budget_input)
    print('_'*75)

    try: #  ---------------------- INTEGER CHECK -----------------------
        val = int(budget_input)
        budget_store.append(int(budget_input))

        print('_'*75)
        user_input = input("Do you want to continue entering budget items? Enter yes or no: ").lower()
        print("You entered: ",user_input)
        print('_'*75)
        loop(user_input)
    except ValueError:
        print("You did no enter an integer. Program ENDED")
        sys.exit()

def budget_check(): # -------------------- BUDGET CHECK ------------------------
    for val in stored.values():
        total_list.append(int(val))
    for val in stored.values():
        total = sum(total_list)
        total = int(total)

        print('-'*25)
        print("Calculating your total")
        print('-'*25)

        for run_num in range(runs):
            time.sleep(.1) #  ---------------------- PROGRESS BAR -----------------------
            updt(runs, run_num + 1)

        print('-'*25)
        print("Total: ",'\t', total)
        print('-'*25)
        break

    budget_store.remove(int(0))

    if budget_store[0] < total:
        difference = total - budget_store[0]
        print("Over budget by: ", difference)
        print('-'*25)
        sys.exit()
    elif budget_store[0] > total:
        difference = budget_store[0] - total
        print("Under budget by: ", difference)
        print('-'*25)
        sys.exit()
    else:
        print("ERROR3")


budget(budget_store)
