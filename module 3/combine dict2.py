data = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
cvalues = {}

for d in data:
    item = d['item']
    amount = d['amount']

    if item in cvalues:
        cvalues[item] += amount
    else:
        cvalues[item] = amount

print("Combined values in the list of dictionaries:")
print(cvalues)
