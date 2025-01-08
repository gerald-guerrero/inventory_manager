with open("menu.txt", "r") as menu: # Reads menu.txt to print out menu options
    print(menu.read())
    
menu_choice = 0
# Loop will continue to ask for user input until 8 is selected which breaks the loop
while (menu_choice != 8): 
    # Temporary user input logic. Function will be changed later using input_manager.py function
    menu_choice = int(input("Select a menu option:\n")) 
    #The following conditionals check the user input for an associated menu option
    if (menu_choice == 1):
        print("(Add Option) selected")
    elif (menu_choice == 2):
        print("(Remove Item) selected")
    elif (menu_choice == 3):
        print("(Update Quantity) selected")
    elif (menu_choice == 4):
        print("(Search Items) selected")
    elif (menu_choice == 5):
        print("(Show Stats) selected")
    elif (menu_choice == 6):
        print("(Save Inventory) selected")
    elif (menu_choice == 7):
        print("(Load Inventory) selected")

print("Exiting Inventory Manager")