# test_list = [{"bread": 5}, {"white Bread": 10}, {"milk": 15}]

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

# search function that takes search item and a list of dictionaries
def search(user_search_item, test_list):
    # Convert user_search_item to lowercase
    user_search_item = user_search_item.lower()

    # Assign converted list of dictionaries to lower_case_list
    lower_case_list = conv_lowercase(test_list)

    # Create an empty list
    result = []

    # Iterate through lowercase list
    for x in lower_case_list:
        for key, value in x.items():
            if user_search_item in key:
                result.append(key)
    return result

#search_results = search("bread", test_list)
#print(search_results)