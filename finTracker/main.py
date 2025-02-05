from transactions import add_transaction, view_transactions, show_home_summary
from categories import manage_categories
import pyfiglet

def main():
    print("\n")
    ascii_banner = pyfiglet.figlet_format("Financial Tracker", font="slant")  # You can try different fonts here
    print(ascii_banner)

    while True:
        # get user choice
        show_home_summary()
        choice = show_menu() 
        
        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_transactions()
        elif choice == "3":
            manage_categories()
        elif choice == "4":
            # exit the program
            print("Exiting... Goodbye!\n")
            break  
        else:
            print("Invalid choice, please try again.")

# display menu to user
def show_menu():
    print("Menu:")
    print("1. Add a Transaction")
    print("2. View Transactions Overview")
    print("3. Manage Transaction Categories")
    print("4. Exit")
    # get user input
    choice = input("\nSelect an option: ")
    return choice

if __name__ == "__main__":
    main()
