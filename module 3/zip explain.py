"""The zip() function in Python is used to combine multiple iterable objects (like lists, tuples, or strings) element-wise into tuples. It takes one or more iterables as arguments and returns an iterator of tuples where the i-th tuple contains the i-th element from each of the input iterables"""

## example
## 1 multiple sequences
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
for num, letter in zip(list1, list2):
    print(num, letter)
    
## 2  iterables into tuples:

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = zip(list1, list2)
print(list(zipped))


## 3 Transposing data

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = zip(*matrix)
print(list(transposed))

