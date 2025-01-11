import user_input
import inventory_operations
import search
import Jason_stats as stats

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
        item_name, item_qty = user_input.get_item_details()
        inventory_operations.add_item(inventory, item_name, item_qty)
    elif (menu_choice == 2):
        print("\n(Remove Item) selected")
        item_name = user_input.get_search_term()
        inventory_operations.remove_item(inventory, item_name)
    elif (menu_choice == 3):
        print("\n(Update Quantity) selected")
        item_name, item_qty = user_input.get_item_details()
        inventory_operations.update_quantity(inventory, item_name, item_qty)
    elif (menu_choice == 4):
        print("\n(Search Items) selected")
        search_term = user_input.get_search_term()
        search_results = search.search(search_term, inventory)
        print(search_results)
    elif (menu_choice == 5):
        print("\n(Show Stats) selected")
        inventory_count = stats.get_inventory_count(inventory)
        total_quantity = stats.get_total_quantity(inventory)
        top_item = stats.get_top_item(inventory)

        print("Inventory Count: ", inventory_count)
        print("Total Quantity: ", total_quantity)
        print("Top Item: ", top_item)
    elif (menu_choice == 6):
        print("\n(Save Inventory) selected")
    elif (menu_choice == 7):
        print("\n(Load Inventory) selected")
    elif(menu_choice == 8):
        print("\nExiting Inventory Manager")
        break
    input("\nPress \"Enter\" to Continue")
