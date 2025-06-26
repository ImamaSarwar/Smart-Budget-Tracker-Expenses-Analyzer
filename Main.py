currencySymbol = "Rs"     #default, can be changed by user
savingGoal = 10000        #default, updated by user

#Login Block
def isValidUsername(username): #Username must contain atleast 1 letter
    for char in username:
        if char.isalpha():
            return True
    return False

def isValidPassword(password): #password must contain atleast 1 digit
    for char in password:
        if char.isdigit():
            return True
    return False

def login():
    print("=========== Welcome to AuraFin: Your Own Smart Budget Tracker & Expenses Analyzer! ==========\n\nKindly Login to Begin")

    while True:     
        username = input("Enter username (must contain at least 1 letter): ")
        if isValidUsername(username):
            break
        else:
            print("Username must contain at least one letter.\n")

    while True:
        password = input("Enter password (must contain at least 1 digit): ")
        if isValidPassword(password):
            break
        else:
            print("Password must contain at least one number.\n")

    print(f"\nHello, {username}! You are now logged in.\n")
    return username
def formatCurrencySymbol(rawSymbol):
    forceUppercase = {"INR", "USD", "PKR", "EUR", "GBP", "JPY", "CAD"} #symbols in all caps

    if rawSymbol.upper() in forceUppercase: #if the entered symbol is one of the all caps one, format it correctly
        return rawSymbol.upper()
    elif rawSymbol.isalpha(): #if it is sth like Rs, capitalize just the first letter
        return rawSymbol.capitalize()  
    else:   #leave symbols like $ as-is
        return rawSymbol  

#Income and Expense Block

#initially empty lists to manage income and expenses
incomes = []
expenses = []

def addIncome():
    while True:
        try:
            rawInput = input("Enter income amount: ").replace(",", "") #handle the entries like 10,000 without error
            amount = float(rawInput) #typecasting 
            if amount > 0:
                break
            else:
                print("Income cannot be negative. Please enter a valid amount.\n")
        except ValueError:
            print("Invalid input! Please enter a valid number (e.g., 10000 or 10,000).\n")

    note = input("Enter income note (optional). Press enter to skip: ")

    incomes.append([amount, note]) #update the array
    print("Income added successfully!\n")

def addExpense():
    while True:
        try:
            rawInput = input("Enter expense amount: ").replace(",", "")
            amount = float(rawInput)
            if amount > 0:
                break
            else:
                print("Expense cannot be negative. Please enter a valid amount.\n")
        except ValueError:
            print("Invalid input! Please enter a valid number (e.g., 5000 or 5,000).\n")

    while True:
        category = input("Enter category (e.g., Food, Transport): ").strip() #entering a category is mandatory
        if category:
            break
        else:
            print("Category cannot be empty. Please enter a valid category.\n")

    note = input("Enter note (optional). Press enter to skip: ")

    expenses.append([amount, category, note]) #update the array
    print("Expense added successfully!\n")

#SUMMARY BLOCK
def categoricalAnalysis():
    print("\n=== Category Analysis ===")

    if not expenses:
        print("No expenses to analyze.\n")
        return

    categoryTotals = {}

    for amount, category, _ in expenses: #to handle cases like food, Food. Both are same so add the amounts
        lowerCat = category.lower()      #case insensitive 
        categoryTotals[lowerCat] = categoryTotals.get(lowerCat, 0) + amount #get the key, if it is already there then sum the amounts

    for lowerCat, total in categoryTotals.items(): #format the categories by making the first letter capital, all others lower case
        formattedCat = lowerCat.capitalize()

        while True:
            limit = input(f"  -> Set a limit for {formattedCat} (or press Enter to skip): ").strip() #user gets to set a limit for each category wrt which analysis will be drawn
            if not limit: #if user decides to skip
                limit = -1
                break
            try:
                limit = float(limit.replace(",", "")) #handle commas 
                if limit < 0:
                    print("Limit cannot be negative. Please enter a valid amount.\n")
                else:
                    break
            except ValueError:
                print("Invalid input! Please enter a valid number (e.g., 10000 or 10,000).\n")

        print(f"Your Spending in {formattedCat} category: {currencySymbol} {total}") #analysis 
        if limit >= 0:
            if total > limit:
                print("Analysis: Overspending in this category!\n")
            else:
                print("Analysis: Within budget.\n")
        else:
            print("No limit set for this category\n")

def showSummary():
    if not incomes:
        print("\nNo income data available. Please add income first.\n")
        return

    if not expenses:
        print("\nNo expenses recorded yet. Here's a basic summary:\n")

    totalIncome = 0
    for entry in incomes:  #entry = [amount, note]
        totalIncome += entry[0]

    totalExpense = 0
    for entry in expenses:  #entry = [amount, category, note]
        totalExpense += entry[0]

    balance = totalIncome - totalExpense

    print("\n===== Summary =====")
    print("Total Income  : Rs ", totalIncome)
    print("Total Expense : Rs ", totalExpense)
    print("Balance       : Rs ", balance)

    if totalExpense > totalIncome: #summary with a tip
        print("You are spending more than you earn. Consider cutting back on non-essential expenses.")

    elif balance > savingGoal: #10000 is the set saving goal
        print("Great job! You're saving well.\nConsider moving some of your savings into a fixed deposit or investment plan.")
    else:
        print("Keep tracking to reach your savings goal.")

    if balance < 1000: #intelligent tip
        print("Your balance is running low. Try setting a weekly spending limit.")

    if expenses:
        choice = input("\nDo you want category-wise analysis? (y/n): ")
        if choice.lower() == 'y':
            categoricalAnalysis()

def listAllIncomes():
    if not incomes:
        print("\nNo incomes recorded yet.\n")
    else:
        print("\n===== All Incomes =====")
        i = 1
        for entry in incomes:
            amount = entry[0] #entry[income, note]
            note = entry[1]
            print(f"{i}. {currencySymbol} {amount}  |  Note: {note}")
            i += 1

def listAllExpenses():
    if not expenses:
        print("\nNo expenses logged yet.\n")
    else:
        print("\n========= All Expenses =========")

        categoryTotals = {}
        categoryNotes = {}

        for amount, category, note in expenses:
            key = category.lower()       #case insensitive
            categoryTotals[key] = categoryTotals.get(key, 0) + amount #total the amount for each category
            if key not in categoryNotes: #empty notes
                categoryNotes[key] = []
            if note.strip():             #if different notes are there for same category, concatenate them
                categoryNotes[key].append(note.strip())

        i = 1
        for key in categoryTotals: #list = [expense, category, note]
            formattedCat = key.capitalize()
            total = categoryTotals[key]
            notes = ", ".join(categoryNotes.get(key, [])) or "No note"
            print(f"{i}. {currencySymbol} {total} | Category: {formattedCat} | Note: {notes}")
            i += 1

def editIncome():
    if not incomes:
        print("\nNo incomes recorded yet.\n")
        return

    listAllIncomes()
    try:
        index = int(input("Enter the number of the income to edit: ")) - 1 #indices are from 1-last
        if index < 0 or index >= len(incomes): #invalid input handling
            print("Invalid entry number.\n")
            return

        while True:
            newIncome = input(f"Enter new amount (or press Enter to keep {currencySymbol} {incomes[index][0]}): ").strip() #.strip just in case user presses a space then enter, still original amount will be saved 
            if not newIncome:
                newAmount = incomes[index][0] #new amount is the original amount in case of skipping
                break
            try:
                newAmount = float(newIncome.replace(",", "")) #else the new amount with removed commas is considered
                if newAmount < 0:                             #negative amount entry edge case
                    print("Income cannot be negative. Please enter a valid amount.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number (e.g., 10000 or 10,000).")

        newNote = input(f"Enter new note (or press Enter to keep '{incomes[index][1]}'): ").strip() or incomes[index][1] #either new or the original note is kept based on the short circuit evaluation

        incomes[index] = [newAmount, newNote] #updating the incomes array
        print("Income updated successfully!\n")
    except ValueError:
        print("Invalid input. Please enter a valid number.\n")

def editExpense():
    if not expenses:
        print("\nNo expenses recorded yet.\n")
        return

    print("\n========= Individual Expenses =========")
    i = 1
    for entry in expenses: #displaying the expenses array
        amount = entry[0]
        category = entry[1]
        note = entry[2]
        print(f"{i}. {currencySymbol} {amount} | Category: {category.capitalize()} | Note: {note}")
        i += 1

    try:
        index = int(input("Enter the number of the expense to edit: ")) - 1
        if index < 0 or index >= len(expenses):
            print("Invalid entry number.\n")
            return

        current = expenses[index]

        while True:
            newExpense = input(f"Enter new amount (or leave blank to keep {currencySymbol} {current[0]}): ").strip()
            if not newExpense: #if nothing is typed, original one is kept
                newAmount = current[0]
                break
            try:
                newAmount = float(newExpense.replace(",", "")) #else the new amount with correct formatting is stored
                if newAmount < 0:                              #handle negative entries edge case
                    print("Expense cannot be negative. Please enter a valid amount.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number (e.g., 10000 or 10,000).")

        #ask if category and note for the corresponding expense are to be modified
        newCategory = input(f"Enter new category (or leave blank to keep '{current[1]}'): ").strip() or current[1] 
        newNote = input(f"Enter new note (or leave blank to keep '{current[2]}'): ").strip() or current[2]

        expenses[index] = [newAmount, newCategory, newNote] #update the array 
        print("Expense updated successfully!\n")
    except ValueError:
        print("Invalid input. Please enter valid numbers.\n")

def deleteIncome(): #enabling the user to delete any income entry 
    if not incomes:
        print("\nNo incomes recorded yet.\n")
        return

    listAllIncomes() #display the array to correctly select the entry
    try:
        index = int(input("Enter the number of the income to delete: ")) - 1 #input index
        if index < 0 or index >= len(incomes):
            print("Invalid entry number.\n")
            return

        confirm = input(f"Are you sure you want to delete this income (Rs {incomes[index][0]})? (y/n): ").lower() #confirmation
        if confirm == 'y':
            incomes.pop(index)
            print("Income entry deleted successfully!\n")
        else:
            print("Deletion cancelled.\n")
    except ValueError:
        print("Invalid input. Please enter a valid number.\n")

def deleteExpense():
    if not expenses:
        print("\nNo expenses recorded yet.\n")
        return

    print("\n========= Individual Expenses =========")
    i = 1
    for entry in expenses: #displaying the expenses array
        amount = entry[0]
        category = entry[1]
        note = entry[2]
        print(f"{i}. {currencySymbol} {amount} | Category: {category.capitalize()} | Note: {note}")
        i += 1
    try:
        index = int(input("Enter the number of the expense to delete: ")) - 1
        if index < 0 or index >= len(expenses):
            print("Invalid entry number.\n")
            return

        confirm = input(f"Are you sure you want to delete this expense (Rs {expenses[index][0]} - {expenses[index][1]})? (y/n): ").lower()
        if confirm == 'y':
            expenses.pop(index)
            print("Expense entry deleted successfully!\n")
        else:
            print("Deletion cancelled.\n")
    except ValueError:
        print("Invalid input. Please enter a valid number.\n")

def exportReport(username):
    if not incomes and not expenses:
        print("Nothing to export! Add income or expenses first.\n")
        return

    filename = f"{username}.txt"  # Automatically use username
    try:
        with open(filename, 'w') as file: #opening file in write mode
            file.write(f"===== {username}'s Budgeting Report =====\n\n")

            file.write(">> Incomes:\n") #Heading
            if incomes:
                for amount, note in incomes:
                    file.write(f"  - Rs {amount} | Note: {note or 'N/A'}\n") #write incomes and corresponsing notes into the file
            else:
                file.write("  No income data.\n")

            file.write("\n>> Expenses:\n")
            if expenses:
                for amount, category, note in expenses: #writing expenses with their details into the file
                    file.write(f"  - Rs {amount} | Category: {category} | Note: {note or 'N/A'}\n")
            else:
                file.write("  No expense data.\n")

            totalIncome = sum(entry[0] for entry in incomes) #exporting the summary as well
            totalExpense = sum(entry[0] for entry in expenses)
            balance = totalIncome - totalExpense

            file.write("\n>> Summary:\n")
            file.write(f"  Total Income  : Rs {totalIncome}\n")
            file.write(f"  Total Expense : Rs {totalExpense}\n")
            file.write(f"  Balance       : Rs {balance}\n")

            if totalExpense > totalIncome: #writing analysis
                file.write(f"  Status        : {username} is overspending!\n")
            elif balance > savingGoal:
                file.write(f"  Status        : {username} is saving well.\n")
            else:
                file.write(f"  Status        : {username} needs to keep tracking.\n")

        print(f"\nReport exported successfully to '{filename}'!\n")
    except Exception as e:
        print(f"Error exporting report: {e}\n")

def menu():
    #displaying options
    while True:
        print("\n1. Add Income")
        print("2. Add Expense")
        print("3. Show Summary")
        print("4. List All Incomes")
        print("5. List All Expenses")
        print("6. Edit Income")
        print("7. Edit Expense")
        print("8. Delete an Income")
        print("9. Delete an Expense")
        print("10. Exit")

        choice = input("Choose an option: ")

        #calling the required functions
        if choice == '1':
            addIncome()
        elif choice == '2':
            addExpense()
        elif choice == '3':
            showSummary()
        elif choice == '4':
            listAllIncomes()
        elif choice == '5':
            listAllExpenses()
        elif choice == '6':
            editIncome()
        elif choice == '7':
            editExpense()
        elif choice == '8':
            deleteIncome()
        elif choice == '9':
            deleteExpense()
        elif choice == '10':
            print("\nExiting the program... \nGoodbye!")
            exportReport(username)
            break
        else:
            print("Invalid option. Try again.\n")
username=login()

#ask user for their preferred currency and saving goal
rawSymbol = input("Enter your preferred currency symbol (e.g., $, Rs, INR): ") or "Rs"
currencySymbol = formatCurrencySymbol(rawSymbol)
while True:
    try:
        goal = input("Set your savings goal: ").strip()
        savingGoal = float(goal.replace(",", ""))
        if savingGoal < 0:
            print("Savings goal cannot be negative. Please enter a valid amount.\n")
            continue
        break
    except ValueError:
        print("Invalid amount. Please enter a valid number (e.g., 10000 or 10,000).\n")
menu()