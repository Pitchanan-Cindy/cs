categories = {
    "Income": ["Salary", "Freelance", "Bonus"],
    "Expense": ["Groceries", "Rent", "Utilities", "Entertainment"]
}

# categories management
def manage_categories():
    while True:
        print("\n-----------------------------------------------------------------------------------------------------------")
        print("Manage Transaction Categories")
        print("-----------------------------------------------------------------------------------------------------------")
        # display category management menu to the user
        print("1. View All Categories")
        print("2. View Income Categories")
        print("3. View Expense Categories")
        print("4. Add a New Category")
        print("5. Delete an Existing Category")
        print("6. Return to Home Summary")

        # get user input
        choice = input("\nSelect an option: ")

        if choice == "1":
            view_all_categories()
        elif choice == "2":
            view_categories ("Income")
        elif choice == "3":
            view_categories ("Expense")
        elif choice == "4":
            add_category()
        elif choice == "5":
            delete_category()
        elif choice == "6":
            break
        else:
            print("Invalid option. Please try again.")


# display all income and expense categories
def view_all_categories():
    print("\n-----------------------------------------------------------------------------------------------------------")
    print("All Categories")
    print("-----------------------------------------------------------------------------------------------------------")

    # display all income categories
    print("Income Categories:")
    for category in categories["Income"]:
        print(f"- {category}")

    #display all expense categories
    print("\nExpense Categories:")
    for category in categories["Expense"]:
        print(f"- {category}")


# display category by type(income/expense)
def view_categories(category_type):
    print("\n-----------------------------------------------------------------------------------------------------------")
    print(f"{category_type} Categories")
    print("-----------------------------------------------------------------------------------------------------------")

    for category in categories[category_type]:
        print(f"- {category}")


# add a new category
def add_category():
    print("\n-----------------------------------------------------------------------------------------------------------")
    print("Add a New Category")
    print("-----------------------------------------------------------------------------------------------------------")
    # display category type and get user choice
    print("Select category type:")
    print("1. Income")
    print("2. Expense")
    category_choice = input("\nEnter 1 for Income or 2 for Expense: ")

    if category_choice == "1":
        category_type = "Income"
    elif category_choice == "2":
        category_type = "Expense"
    else:
        print("Invalid choice! Please enter 1 or 2.")
        return
    
    # get user input on for a new category without extra whitespaces
    new_category = input("Enter the new category name: ").strip()

    # duplicate category
    if new_category in categories[category_type]:
        print("Category already exists!")
        return

    # add category at the end of the list and display
    categories[category_type].append(new_category)
    print(f"\nCategory '{new_category}' added successfully under {category_type}!")
    

# delete an existing category
def delete_category():
    print("\n-----------------------------------------------------------------------------------------------------------")
    print("Delete an Existing Category")
    print("-----------------------------------------------------------------------------------------------------------")
    # display category type and get user choice
    print("Select category type:")
    print("1. Income")
    print("2. Expense")
    category_choice = input("\nEnter 1 for Income or 2 for Expense: ")

    if category_choice == "1":
        category_type = "Income"
    elif category_choice == "2":
        category_type = "Expense"
    else:
        print("Invalid choice! Please enter 1 or 2.")
        return
    
    # if no category to delete in that category type then display the message
    if not categories[category_type]:
        print(f"\nNo {category_type} categories available to delete.")
        return
    
    print("\nSelect a category to delete:")
    # display categories with nunber options 
    i = 1
    for category in categories[category_type]:
        print(f"{i}. {category}")
        i += 1

    # get user choice to delete
    choice = int(input("\nEnter the number of the category to delete: ")) - 1

    # the choice is not valid then display error message
    if not 0 <= choice < len(categories[category_type]):
        print("Invalid choice.")
        return

    #confirm before delete
    confirm = input("Are you sure you want to delete this category? (Y/N): ").strip().lower()

    if confirm == "y":
        # delete from the list
        deleted_category = categories[category_type].pop(choice)
        print(f"\nCategory '{deleted_category}' deleted successfully.")
    else:
        print("\nDeletion has been canceled.")