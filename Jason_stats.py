
def get_inventory_count(inventory):   #counts number of items in the inventory
    return len(inventory)

def get_total_quantity(inventory):   #adds numeric values in inventory and gives sum
    return sum(inventory.values())

def get_top_item(inventory):   #get the top item (highest number) in the inventory
    try:                       #Try/except block should only work if numbers are not a tie
        return max(inventory, key=inventory.get)
    except ValueError:
        return None
    
if __name__ == "__main__":
      mock_inv = {"Apple": 6, "Orange": 5}
      print(get_inventory_count(mock_inv))  # Expect 2
      print(get_total_quantity(mock_inv))   # Expect 15
      print(get_top_item(mock_inv))         # Expect "Apple"



