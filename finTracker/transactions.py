from datetime import datetime, timedelta
from categories import categories

# total income/expense on home page
total_income = 0
total_expenses = 0
# empty list to store transactions
transactions = [] 


# total balance on home page
def calculate_balance():
    return total_income - total_expenses


# Home summary
def show_home_summary():
    print("\n-----------------------------------------------------------------------------------------------------------")
    print("Personal Finance Tracker - Home Summary")
    print("-----------------------------------------------------------------------------------------------------------")
    # display the summary balance
    print(f"Total Income: ${total_income}")
    print(f"Total Expenses: ${total_expenses}")
    print(f"Remaining Balance: ${calculate_balance()}")
    # explanation to introduce app
    print("\nMonitor your finances: Quickly see your income, expenses, and balance to make better financial decisions.")
    print("-----------------------------------------------------------------------------------------------------------")


# add user income/expense
def add_transaction():
    # to update the summary
    global total_income, total_expenses

    print("\n-----------------------------------------------------------------------------------------------------------")
    print("Add a Transaction")
    print("-----------------------------------------------------------------------------------------------------------")
    # display transaction type to add
    print("1. Income")
    print("2. Expense")
    # get user input for transaction type
    transaction_type = input("\nEnter transaction type: ")
    print("-----------------------------------------------------------------------------------------------------------")

    # invalid input, display error message
    if transaction_type not in ["1", "2"]:
        print("Invalid type!")
        return

    # get input from user
    amount = float(input("Enter amount: $"))
    date = input("Enter transaction date (MM/DD/YYYY): ")

    # select the transaction category
    print("\nSelect a category:")
    categories_list = categories["Income"] if transaction_type == "1" else categories["Expense"]
    # display category types with nunber options 
    i = 1
    for category in categories_list:
        print(f"{i}. {category}")
        i += 1
    # display at last
    print(f"{len(categories_list) + 1}. Add a new category")

    # get and store category
    category_choice = int(input("\nSelect a option: "))

    # add a new category along with transaction
    if category_choice == len(categories_list) + 1:
        # get new category input without extra whitespace
        new_category = input("Enter new category name: ").strip()
        # add to the list
        categories_list.append(new_category)
        category = new_category
    # save category
    else:
        category = categories_list[category_choice - 1]

    # save the transaction
    transaction = {
        "type": "Income" if transaction_type == "1" else "Expense",
        "amount": amount,
        "date": date,
        "category": category
    }

    # confirm before save
    print("\n*Note: Once saved, this transaction cannot be directly edited. You will need to manually adjust or re-add if needed.*")
    confirm = input("Confirm and save transaction? (Y/N): ").strip().lower()

    if confirm == "y":
        # add transaction at the end of the list
        transactions.append(transaction)
        print(f"\nTransaction saved successfully!")

        # update the total amount
        if transaction_type == "1":
            total_income += amount
        else:
            total_expenses += amount
    else: 
        print("Transaction discarded.")


# display all the transactions 
def view_transactions():
    print("\n-----------------------------------------------------------------------------------------------------------")
    print("Transactions Overview")
    print("-----------------------------------------------------------------------------------------------------------")

    # if no transaction to display
    if not transactions:  
        print("No transactions available.")
        return
    
    # transaction range options
    print("1. Last 7 days")
    print("2. Last 30 days")
    print("3. Custom date range")
    # get user input
    choice = input("\nSelect a time range: ")
    print("-----------------------------------------------------------------------------------------------------------")

    # current date
    today = datetime.today()
    # default end date
    end_date = today
    
    # filter dates
    if choice == "1":
        start_date = today - timedelta(days=7) 
    elif choice == "2":
        start_date = today - timedelta(days=30) 
    elif choice == "3":
        start_date = datetime.strptime(input("Enter start date (MM/DD/YYYY): "), "%m/%d/%Y")
        end_date = datetime.strptime(input("Enter end date (MM/DD/YYYY): "), "%m/%d/%Y")
    else:
        print("Invalid choice!")
        return
    
    # filter options
    print("\nView transactions:")
    print("1. All Transactions")
    print("2. Filter by Income")
    print("3. Filter by Expense")
    print("4. Return to Home Summary")
    # get input from user
    filter_option = input("\nSelect an option: ")
    
    # store filtered transactions
    filtered_transactions = []
    
    # go through each transaction to filter
    for transaction in transactions:
        transaction_date = datetime.strptime(transaction['date'], "%m/%d/%Y")
        
        # filter by dates 
        if start_date <= transaction_date <= end_date:
            # filter by type 
            if filter_option == "1":  
                filtered_transactions.append(transaction)
            elif filter_option == "2" and transaction["type"] == "Income":
                filtered_transactions.append(transaction)
            elif filter_option == "3" and transaction["type"] == "Expense":
                filtered_transactions.append(transaction)
    
    # sort transaction by most recent first
    filtered_transactions.sort(key=lambda x: datetime.strptime(x['date'], "%m/%d/%Y"), reverse=True)

    # display filtered transactions
    if not filtered_transactions:
        print("No transactions found.")
    else:
        for transaction in filtered_transactions:
            print(f"Date: {transaction['date']} | {transaction['type']}: ${transaction['amount']} | Category: {transaction['category']}")
