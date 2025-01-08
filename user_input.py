#Get the Menu Choice function ask the user to choose a menu option.
def get_main_menu_choice():
    while True: #Creates a loop that keeps running until the user provides valid input.
        try: #Used to test block of code for errors.
            choice = int(input("Enter a menu option [1-8]: ")) #input() Prompts the user to type something, int() Converts the string input into a number.
            if 1 <= choice <= 8: # Checks if the integer is between 1 and 8
                return choice # Sends the valid number back to the function.
            else: # Runs if the number is outside the range
                print("Invalid choice. Enter a number between 1 and 8.")
        except ValueError: # except - catches errors from the try block, if the user types "abc". ValueError - used when Python tries to convert a word into a number but fails.
            print("That's not a valid number. Try again.") #Asks the user to try again


#Get Item Details ask the user for an item's name and quantity.
def get_item_details():
    item_name = input("Enter the item's name: ")
    while True: # Keeps asking until the user provides a valid number for quantity
        try:
            quantity = int(input(f"Enter the quantity for {item_name}: ")) # Converts quantity to an integer
            return item_name, quantity # Sends back as a tuple (item_name, quantity)
        except ValueError: # Catches errors if the input cannot be converted to an integer
            print("Please enter a valid number for the quantity.")

#Get a Search Term ask the user for a search term.
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

