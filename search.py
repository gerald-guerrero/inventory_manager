# con_lowercase function takes list of dictionaries as an argument
def conv_lowercase(dicts_list):
    # Create an empty list
    result = []

    # Iterate through each dictionary in list
    for d in dicts_list:
        # Create new dictionary
        new_dict = {}
        # Iterate through key-value pair is dicts_list
        for key, value in d.items():
            # Checks if value is a string since you can't make a number lowercase
            # If value is a string, convert to lowercase
            if isinstance(value, str):
                value = value.lower()
            # Add lowercase value to new dictionary    
            new_dict[key.lower()] = value
        # Add dictionary to resullt list    
        result.append(new_dict)
    # Return new lowercase list of dictionaries     
    return result

# search function that takes search item, search value, and a list of dictionaries
# search_value must exist in list of dictionaries or the program will generate an error
def search(user_search_item, search_value, test_list):
    # Convert user_search_item to lowercase
    user_search_item = user_search_item.lower()

    # Convert search_value to lowercase
    search_value = search_value.lower()

    # Assign converted list of dictionaries to lower_case_list
    lower_case_list = conv_lowercase(test_list)

    # Use list comprehension to return a list of dictionary items that match the user's search item
    # Return an empty list if the item is not in the list of dictionaries
    return [x for x in lower_case_list if x[search_value] == user_search_item]