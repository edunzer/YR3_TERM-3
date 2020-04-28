## BUDGET ANALYSIS (v3)

budget_input = 0

values = {}

def budget_check(values):
    total_list = []
    for cost in values.values():
        total_list.append(cost)

        print(total_list)

        total = sum(total_list)
        print("Here is your total: ", total)
        break


def chart(values):
    print('ITEM \t\t COST')
    print('-------------------------')
    for item in values:
        print(item, '\t\t',values[item])

def item_add(item_input, cost_input):

    if item_input.isalpha() == True and cost_input >= 0:
        values[item_input] = cost_input

        user_input = input("(2)Do you want to continue entering budget items? Enter yes or no: ").lower()
        print(user_input)
        loop(user_input)
    else:
        print("ERROR1")

def loop(user_input):

    while user_input == 'yes':
        item_input, cost_input = input("(1)Please enter the item to add to your budget and the cost of that item: ").split()
        item_input = str(item_input).lower()
        cost_input = int(cost_input)

        chart(values)
        item_add(item_input, cost_input)
    else:
        chart(values)
        budget_check(values)
        break

def budget(budget_input):
    budget_input = int(input("Please enter your budget for this month: "))
    print(budget_input)
    user_input = input("(1)Do you want to continue entering budget items? Enter yes or no: ").lower()
    print(user_input)
    loop(user_input)


budget(budget_input)
