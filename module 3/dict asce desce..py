# Dictionary to sort
dict = {'apple': 30, 'banana': 20, 'orange': 40, 'grapes': 10}

# Sort the dictionary by value in ascending order
dict_asc = (sorted(dict.items(), key=lambda item: item[1]))

# Sort the dictionary by value in descending order
dict_desc = (sorted(dict.items(), key=lambda item: item[1], reverse=True))

# Output the sorted dictionary in ascending order
print("Ascending order:", dict_asc)

# Output the sorted dictionary in descending order
print("Descending order:", dict_desc)
