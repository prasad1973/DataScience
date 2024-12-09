from loaddata import DataLoadAndStore as DLS
from datetime import datetime

data = []
budget = 0

def addexpense():
    amount = input('Please enter an amount:')
    description = input('Please give a description:')
    category = input('Please give a category:')
    today_date = datetime.today()
    date = today_date.strftime('%Y-%m-%d')
    add = {}
    add['date'] = date.strip()
    add['category'] = category.strip()
    try:
        amount = int(amount.strip())
    except ValueError:
        print("Invalid input: not an integer, please retry adding expense.")
        return
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
    budget = input('Please enter your desired budget:')
    try: 
        budget = int(budget.strip())
    except ValueError:
        print("Invalid input: not an integer, please retry setting budget.")
        return
    expenses = 0
    for entry in data:
        try:
            expenses += int(entry.strip())
        except ValueError:
            print("Invalid expense entry, please repair before attempting to track budget.")
            return
    if(budget - expenses >= 0):
        print(f"You are within budget, with ${str(budget - expenses)} to spare.")
    else:
        print(f"Warning, you are ${str(expenses - budget)} over your budget!")