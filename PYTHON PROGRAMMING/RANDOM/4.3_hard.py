## BUDGET ANALYSIS (unfinished)
import sys

value = {}

def item_add(user_input):

    while user_input == 'yes' or user_input == 'y':

        #Taking two arguments the item and the cost

        entered_item, entered_cost = input("Please enter the item to add to your budget and the cost of that item: ").split()
        entered_item = str(entered_item)
        entered_cost = int(entered_cost)


        if entered_item.isalpha() == True and entered_cost >= 0:
            value[entered_item] = entered_cost
            print('ITEM \t\t COST')
            print('----------------------------------------------------------------------')
            for x, y in value.items():
                print(x,'\t\t', y)
        else:
            print(len(entered_item))
            print("ERROR")


        user_input = input("Do you want to continue entering budget items? Enter yes or no: ").lower()
        item_add(user_input)


    else:
        print('ITEM \t\t COST')
        print('----------------------------------------------------------------------')
        for x, y in value.items():
            print(x,'\t\t', y)
            for y in value.values():
                total = 0
                total = total + y
                return total
            print(total)
            sys.exit()


user_input = input("Would you like to start entering items into your budget list/calculator? Yes or no: ").lower()
item_add(user_input)
