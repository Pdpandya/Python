dict = {'apple': 30, 'banana': 20, 'orange': 40, 'grapes': 10}

dict_asc = (sorted(dict.items(), key=lambda item: item[1]))

dict_desc = (sorted(dict.items(), key=lambda item: item[1], reverse=True))

print("Ascending order:", dict_asc)
print("Descending order:", dict_desc)
