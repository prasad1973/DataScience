from loaddata import DataLoadAndStore as DLS
from datetime import datetime
import os

data = []
budget = 0

def addexpense():
    amount = input('Please enter an amount: ')
    try:
        amount = int(amount.strip())
    except ValueError:
        print("Invalid input: not an integer, please retry adding expense.")
        return
    description = input('Please give a description: ')
    category = input('Please give a category: ')
    today_date = datetime.today()
    date = today_date.strftime('%Y-%m-%d')
    add = {}
    add['date'] = date.strip()
    add['category'] = category.strip()
    add['amount'] = str(amount)
    add['description'] = description.strip()
    data.append(add)

def viewexpenses():
    for entry in data:
        if ((entry['date'] != None) and (entry['category'] != None) and (entry['amount'] != None) and (entry['description'] != None)):
            print("Date: " + entry['date'])
            print("Category: " + entry['category'])
            print("Amount: " + entry['amount'])
            print("Description: " + entry['description'])
        else:
            print("Error: missing information in one of the entries")
        print("-------------------------------------------------------")

def setbudget():
    budget = input('Please enter your desired budget: ')
    try: 
        budget = int(budget.strip())
    except ValueError:
        print("Invalid input: not an integer, please retry setting budget.")
        return
    expenses = 0
    for entry in data:
        try:
            expenses += int(entry['amount'].strip())
        except ValueError:
            print("Invalid expense entry, please repair before attempting to track budget.")
            return
    if(budget - expenses >= 0):
        print(f"You are within budget, with ${str(budget - expenses)} to spare.")
    else:
        print(f"Warning, you are ${str(expenses - budget)} over your budget!")

run = True
filepath = os.getcwd() + "/PersonalExpenseTracker/budgetdata.csv"
loader = DLS(filepath)
data = loader.load()

while run:
    menu = "Select a number from 1 to 5 to perform an action:\n"
    menu += "1: Add an expense\n"
    menu += "2: View expenses\n"
    menu += "3: Track budget\n"
    menu += "4: Save expenses to file\n"
    menu += "5: Save and quit\n"
    menu += "-------------------------------------\n"
    selection = input(menu)
    try:
        selection = int(selection.strip())
        if selection < 6 and selection > 0:
            if selection == 1:
                addexpense()
            elif selection == 2:
                viewexpenses()
            elif selection == 3:
                setbudget()
            elif selection == 4:
                loader.store(data)
            elif selection == 5:
                loader.store(data)
                print("Goodbye!")
                run = False
            else:
                print("Unrecognized input, please try again")
    except ValueError:
        print("Unrecognized input, please try again")