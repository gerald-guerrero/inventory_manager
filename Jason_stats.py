def get_inventory_count(inventory_list):   # counts number of items in the inventory list
    return len(inventory_list)

def get_total_quantity(inventory_list):   # adds numeric values in inventory list and gives sum
    total_quantity = 0
    for inventory in inventory_list:
        total_quantity += sum(inventory.values())
    return total_quantity

def get_top_item(inventory_list):   # get the top item (highest number) in the inventory list
    combined_inventory = {}
    for inventory in inventory_list:
        for item, quantity in inventory.items():
            if item in combined_inventory:
                combined_inventory[item] += quantity
            else:
                combined_inventory[item] = quantity
    try:                       
        return max(combined_inventory, key=combined_inventory.get)
    except ValueError:                       #Except block should only work if numbers are not present
        return None
    
if __name__ == "__main__":
    mock_inv = [{"Apple": 6}, {"Orange": 6}, {"Kiwi": 9}]
    print(get_inventory_count(mock_inv))  # Expect 3
    print(get_total_quantity(mock_inv))   # Expect 21
    print(get_top_item(mock_inv))         # Expect "Kiwi"
