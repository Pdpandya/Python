# Sample list of dictionaries
data = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

# Dictionary to store combined values
combined_values = {}

# Iterate over each dictionary in the list
for d in data:
    item = d['item']
    amount = d['amount']
    # If the item already exists in the combined dictionary, add the amount to its existing value
    if item in combined_values:
        combined_values[item] += amount
    # If the item is not in the combined dictionary, create a new entry
    else:
        combined_values[item] = amount

# Print the combined dictionary
print("Combined values in the list of dictionaries:")
print(combined_values)
