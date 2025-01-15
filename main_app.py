import user_input
import inventory_operations
import search
import Jason_stats as stats
import json

def save_inventory(inventory, filename="inventory.json"):
    """
    Takes in the current inventory and saves it with the designated file name and type
    file is saved to the current working directory
    """
    with open(filename, "w") as f:
        json.dump(inventory, f)
    return

def load_inventory(filename="inventory.json"):
    """
    Reads the saved inventory file if it exists and returns the inventory as a list of dicts
    If the file is not found, it will return an empty list
    """
    try:
        with open(filename, "r") as f:
            inventory = json.load(f)
    except:
        print("File not found. Returning an empty list")
        inventory = []
    return inventory

menu_choice = 0
inventory = []
# Loop will continue to ask for user input until 8 is selected which breaks the loop
while (True): 
    # Reads menu.txt to print out menu options
    with open("menu.txt", "r") as menu: 
        print(menu.read())

    menu_choice = user_input.get_main_menu_choice()
    #The following conditionals check the user input for an associated menu option
    if (menu_choice == 1):
        print("\n(Add Item) selected")
        item_name, item_qty = user_input.get_item_details() # Retrieves item data from user
        inventory_operations.add_item(inventory, item_name, item_qty) # Adds item data to inventory
    elif (menu_choice == 2):
        print("\n(Remove Item) selected")
        item_name = user_input.get_search_term() # Gets item name from user
        inventory_operations.remove_item(inventory, item_name) # Removes item from inventory
    elif (menu_choice == 3):
        print("\n(Update Quantity) selected")
        item_name, item_qty = user_input.get_item_details() # Retrieves item data from user
        inventory_operations.update_quantity(inventory, item_name, item_qty) # Updates the quantity
    elif (menu_choice == 4):
        print("\n(Search Items) selected")
        search_term = user_input.get_search_term() # Gets item name from user
        search_results = search.search(search_term, inventory) # Gets search results from item name
        print(search_results)
    elif (menu_choice == 5):
        print("\n(Show Stats) selected")
        inventory_count = stats.get_inventory_count(inventory) # Gets the amount of unique items
        total_quantity = stats.get_total_quantity(inventory) # Gets total amount of all items
        top_item = stats.get_top_item(inventory) # Gets item with highest quantity

        print("Inventory Count: ", inventory_count)
        print("Total Quantity: ", total_quantity)
        print("Top Item: ", top_item)
    elif (menu_choice == 6):
        print("\n(Save Inventory) selected")
        # Saves current inventory list to inventory.json
        save_inventory(inventory, "inventory.json") 
    elif (menu_choice == 7):
        print("\n(Load Inventory) selected")
        # Retreives inventory data from inventory.json and assigns it to the inventory list
        inventory = load_inventory("inventory.json") 
    elif(menu_choice == 8):
        # Will exit the main menu loop and stop the program
        print("\nExiting Inventory Manager")
        break

    # Creates a break in between menu loops to prioritize showing menu results before continuing
    input("\nPress \"Enter\" to Continue\n") 
