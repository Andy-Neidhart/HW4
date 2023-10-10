def reverse_sort_dictionary(input_dict):
    # Sort the dictionary items in reverse order by keys
    sorted_items = sorted(input_dict.items(), key=lambda x: x[0], reverse=True)
    
    # Extract names and phone numbers from sorted items
    result_list = [(name, phone_number) for name, (phone_number, _) in sorted_items]
    return result_list
