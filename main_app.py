import user_input
import inventory_operations
import search

menu_choice = 0
inventory = []
# Loop will continue to ask for user input until 8 is selected which breaks the loop
while (menu_choice != 8): 
    # Reads menu.txt to print out menu options
    with open("menu.txt", "r") as menu: 
        print(menu.read())

    menu_choice = user_input.get_main_menu_choice()
    #The following conditionals check the user input for an associated menu option
    if (menu_choice == 1):
        print("(Add Item) selected\n")
        item_name, item_qty = user_input.get_item_details()
        inventory_operations.add_item(inventory, item_name, item_qty)
    elif (menu_choice == 2):
        print("(Remove Item) selected\n")
        item_name = user_input.get_search_term()
        inventory_operations.remove_item(inventory, item_name)
    elif (menu_choice == 3):
        print("(Update Quantity) selected\n")
        item_name, item_qty = user_input.get_item_details()
        inventory_operations.update_quantity(inventory, item_name, item_qty)
    elif (menu_choice == 4):
        print("(Search Items) selected\n")
        search_term = user_input.get_search_term()
    elif (menu_choice == 5):
        print("(Show Stats) selected\n")
    elif (menu_choice == 6):
        print("(Save Inventory) selected\n")
    elif (menu_choice == 7):
        print("(Load Inventory) selected\n")
    print(inventory)
print("\nExiting Inventory Manager\n")