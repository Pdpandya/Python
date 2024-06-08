tuple_list = [('a', 1), ('b', 2), ('c', 3)]
dictionary = dict(tuple_list)

print("Dictionary:", dictionary)



""" We have a list of tuples named tuple_list, where each tuple contains a key-value pair.
Using dictionary comprehension or the dict() constructor, we create a dictionary where the keys are taken from the first elements of the tuples and the values are taken from the second elements of the tuples """