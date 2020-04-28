## BUDGET ANALYSIS (v2)

value = {}

def chart(value):
    for item, cost in value.items():
        print('ITEM \t\t COST')
        print('----------------------------------------------------------------------')
        print(x, '\t\t', y)

def item_add(input_item, input_cost):

    if input_item.isalpha() == True and input_cost >= 0:
        value[input_item] = input_cost
        chart(value)
    else:
        print("ERROR1")

def loop(user_input):
    while user_input == 'yes' or user_input == 'y':

        input_item, input_cost = input("Please enter the item to add to your budget and the cost of that item: ").split()

        input_item = str(input_item).lower()
        input_cost = str(input_cost)
        item_add(input_item, input_cost)

    else:
        print('ITEM \t\t COST')
        print('----------------------------------------------------------------------')
        total = 0
        for x, y in inputed_values.items():
            print(x,'\t\t', y)
            for y in inputed_values.values():
                total = total + y
                print(total)

user_input = input("Do you want to continue entering budget items? Enter yes or no: ").lower()
loop(user_input)
