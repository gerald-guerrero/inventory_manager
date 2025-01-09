#Get the Menu Choice function ask the user to choose a menu option.
def get_main_menu_choice():
    while True: #Creates a loop that keeps running until the user provides valid input.
        try: #Used to test block of code for errors.
            choice = input("Enter a menu option [1-8]: ") #input() Prompts the user to type something, int() Converts the string input into a number.
            if choice.isdigit() and 1 <= int(choice) <= 8: #Checks if the choice contains only numbers and is between 1 and 8
                return int(choice) #Converts the menu choice (string) into an integer and sends the number back to the program.
            else: #Runs if the choice fails validation check (isdigit() or range check).
                print("Invalid choice. Enter a number between 1 and 8.")
        except ValueError: # except - catches errors from the try block, if the user types "abc". ValueError - used when Python tries to convert a word into a number but fails.
            print("That's not a valid number. Try again.") #Asks the user to try again


#Get Item Details ask the user for an item's name and quantity.
def get_item_details():
    while True: # Keeps asking until the user provides a valid number for quantity
        item_name = input("Enter the item's name: ")
        if not item_name or any(char in "#@!" for char in item_name): #Checks if the item name is empty or contains invalid characters
            print("Invalid name. It cannot be empty or contain symbols like #, @, or !") # Tells the user what’s wrong and restarts the loop for valid input.
            continue

        try:
            quantity = input(f"Enter the quantity for {item_name}: ") #Prompts user to enter a quantity for the item
            if not quantity.isdigit() or int(quantity) <=0: # Checks input contains only digits and quantity is greater than zero
                print("Quantity must be a positive number.")
                continue
            return item_name, int(quantity) # Sends back as a tuple (item_name, quantity)
        except ValueError: # Catches errors if the input can't be converted to an integer
            print("Please enter a valid number for the quantity.")

#GAsk the user for a search term to look up items in the inventory
def get_search_term():
    return input("Enter the name to search for: ")


#Testing Block
if __name__ == "__main__":
    print("")

    #Test the menu choice
    menu_choice = get_main_menu_choice() #Calls the function to test it.
    print(f"You selected menu option: {menu_choice}") # Confirms the user's menu choice

    #Test item details
    name, quantity = get_item_details()
    print(f"Item: {name}, Quantity: {quantity}") # Confirms the item name and quantity

    #Test search term
    search = get_search_term()
    print(f"Search Term: {search}") #Confirms the search term

