inv = {'apples': 5, 'oranges': 10, 'pears': 15}


#Return how many **distinct items** are in the inventory (e.g., `len(inventory)` if it’s a dict).
get_inventory_count = len(inv)


#Sum all item quantities.
get_total_quantity = sum


#Return the **item with the highest quantity**.  
#Handle ties or empty inventory as you see fit (maybe return `None` or an empty string in those cases).
get_top_item = max
if __name__ == None:
    print('Please enter item: ')
     

    print(get_inventory_count(inv))
    print(get_total_quantity(inv))
    print(get_top_item(inv))
