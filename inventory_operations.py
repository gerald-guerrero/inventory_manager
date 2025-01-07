
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
            
            return True
    
    # Asigns value to key of fruit - asigns quantity to new fruit 
    new_fruit = {fruit_no_spaces: int(quantity)}  
    inventory.append(new_fruit)
    print(f"Created new item! {fruit_no_spaces} added to inventory") 
     
    return True

#make status to be false if error. 

 
    
add_item(inventory, "apple", 4)
add_item(inventory, "Apple", 4)
add_item(inventory, "    Apple", 5)
# add_item(inventory, "Banana", 8)
# add_item(inventory, "Mango", 10)
# add_item(inventory,"cantlope", 8)
# add_item(inventory, "Pineapple", 10)

print(inventory)
   
    

#return(bool)
#if bool = True:
    #print("Success")
    #else:
        #print("Failure")
#Add item to list !

#Remove Item

#if item is in list:
    #item_count +-1
    #else:
        #return(False) 
        #print(No item found!)


#Update quantity

#take in item_name, new_quant 

#item_count = new_quant

#if item_name is not in list:
    #Add item
    #print(f"Item added with a quantity or {item_count}")