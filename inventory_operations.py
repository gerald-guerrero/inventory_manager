
#---------------------Mod C Inventory Manager--------------------------
#Create List 
inventory = []
#Add item
def add_item(inventory, item_name, quantity):

    #Get rid of spaces 
    fruit_no_spaces = str(item_name).strip().upper()

   

    #Validations-------------------------------
    if isinstance(quantity, str):
        try: 

            quantity = int(quantity)
        except ValueError:
            print("Quantity must be a number!")
            print("Status: Failure")
            return False
        
        
        
    elif isinstance(item_name, int):
        print("Item name cannot be a number!")
        print("Status: Failure")
        return False
    elif quantity < 0:
        print("Quantity cannot be negative!")
        print("Status:Failure")
        return False
    elif quantity == 0:
        print("Quantity Cannot be 0")
        print("Status:Failure")
        return False
    #------------------------------------------
    
    #If fruit exists in inventory then add to quantity 
    for item in inventory:
        if fruit_no_spaces in item:
            print(f"Item found adding to quantity!")
            print(f"Updated quantity from {item[fruit_no_spaces]} to {quantity + item[fruit_no_spaces]}")

            #add item quantitiy to existing quantity - quantity is added to the quantity attatched to the found key 
            item[fruit_no_spaces] += quantity
            print("Status: Success!")
            return True
    
    # If not found Asigns value to key of fruit - asigns quantity to new fruit 
    new_fruit = {fruit_no_spaces: (quantity)}  
    inventory.append(new_fruit)
    print(f"Created new item! {fruit_no_spaces} added to inventory with a quantity of {quantity}") 
    print("Status: Success!")
    return True




   
    
#Remove Item

def remove_item(inventory, item_name):
    #converts name 
    fruit_no_spaces = str(item_name).strip().upper()
    #if item in list
    for item in inventory:
        if fruit_no_spaces in item:
            inventory.remove(item)
            print("item found! Deleting item")
            return True
    else:
        print("Fruit not found!")
        return False
        


#Update quantity

def update_quantity(inventory, item_name, new_quantity):

    fruit_no_spaces = str(item_name).strip().upper()
    
    #Validations ----------------------------------
    if isinstance(new_quantity, str):
        try:
            new_quantity = int(new_quantity)
        except ValueError:
            print("New quantity must be a number!")
            print("Status: Failure")
            return False
    elif isinstance(item_name, int):
        print("Item name cannot be a number!")
        print("Status: Failure")
        return False
    elif new_quantity < 0:
        print("New quantity cannot be negative!")
        print("Status:Failure")
        return False
    elif new_quantity == 0:
        print("New quantity cannot be 0!")
        print("Status: Failure")
        return False
    #---------------------------------------------

    for item in inventory:
        if fruit_no_spaces in item:
            print(f"Item {fruit_no_spaces} found. Updating quantity from {item[fruit_no_spaces]} to {new_quantity} ")
            item[fruit_no_spaces] = new_quantity
            return True
    else:    
        print("Item not found, adding item")
        add_item(inventory, item_name, new_quantity )
        return True



