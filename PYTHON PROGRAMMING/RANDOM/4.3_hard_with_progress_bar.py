## BUDGET ANALYSIS (v2)

import sys
import time

stored = {}
total_list = [0]
budget_store = [0]

def updt(total, progress):

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

def chart(stored):
    print('ITEM \t\t COST')
    print('-------------------------')
    for item in stored:
        print(item, '\t\t',stored[item])

def item_add(item_input, cost_input):

    if item_input.isalpha() == True and cost_input >= 0:
        stored[item_input] = cost_input

        print('___________________________________________________________________________')
        user_input = input("Do you want to continue entering budget items? Enter yes or no: ").lower()

        print(user_input)
        print('___________________________________________________________________________')

        loop(user_input)

    else:
        print("ERROR1")

def loop(user_input):

    while user_input == 'yes':
        print('___________________________________________________________________________')
        item_input, cost_input = input("Please enter the item to add to your budget and the cost of that item: ").split()
        print('___________________________________________________________________________')

        item_input = str(item_input).lower()
        cost_input = int(cost_input)

        chart(stored)
        item_add(item_input, cost_input)

    if user_input == 'no':
        print('___________________________________________________________________________')
        print("Program ENDED")
        print('___________________________________________________________________________')
        chart(stored)
        budget_check()

    else:
        print('___________________________________________________________________________')
        print("You did not select Yes or No. Program ENDED")
        print('___________________________________________________________________________')
        chart(stored)
        sys.exit()

def budget(budget_store):
    print('___________________________________________________________________________')
    budget_input = input("Please enter your budget for this month: ")
    print("You entered: ","$",budget_input)
    print('___________________________________________________________________________')

    try: #  ---------------------- INTEGER CHECK -----------------------
        val = int(budget_input)
        budget_store.append(int(budget_input))

        print('___________________________________________________________________________')
        user_input = input("Do you want to continue entering budget items? Enter yes or no: ").lower()
        print("You entered: ",user_input)
        print('___________________________________________________________________________')
        loop(user_input)
    except ValueError:
        print("You did no enter an integer. Program ENDED")
        sys.exit()



def budget_check():
    for val in stored.values():
        total_list.append(int(val))
    for val in stored.values():
        total = sum(total_list)
        total = int(total)

        print('-------------------------')
        print("Calculating your total")
        print('-------------------------')

        for run_num in range(runs):
            time.sleep(.1) #  ---------------------- PROGRESS BAR -----------------------
            updt(runs, run_num + 1)

        print('-------------------------')
        print("Total: ",'\t', total)
        print('-------------------------')
        break

    budget_store.remove(int(0))

    if budget_store[0] < total:
        difference = total - budget_store[0]
        print("Over budget by: ", difference)
        print('-------------------------')
        sys.exit()
    elif budget_store[0] > total:
        difference = budget_store[0] - total
        print("Under budget by: ", difference)
        print('-------------------------')
        sys.exit()
    else:
        print("ERROR3")


budget(budget_store)
