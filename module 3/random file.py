import random

filename = 'filename.txt'

with open(filename, 'r') as file:
    lines = file.readlines()
    random_line = random.choice(lines)

print("Random line from the file:")
print(random_line.strip())  
