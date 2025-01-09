
#---------------------Mod C Inventory Manager--------------------------
#Create List 
inventory = []
#Add item
def add_item(inventory, item_name, quantity):

    #Get rid of spaces 
    fruit_no_spaces = str(item_name).strip().upper()

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
    new_fruit = {fruit_no_spaces: int(quantity)}  
    inventory.append(new_fruit)
    print(f"Created new item! {fruit_no_spaces} added to inventory") 
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
    
    for item in inventory:
        if fruit_no_spaces in item:
            item[fruit_no_spaces] = new_quantity
            print("Item found. Updating quantity")
            return True
    else:    
        print("Item not found, adding item")
        add_item(inventory, item_name, new_quantity )
        return True




