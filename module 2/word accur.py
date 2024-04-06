sentence = input("Enter a sentence: ")

words = sentence.split()

frequency = {}

for word in words:
    # Removing punctuation (if any) to ensure accurate counting
    word = word.strip('.,!?()[]{}:;"\'')
    
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("Word frequencies in the given sentence:")
for word, count in frequency.items():
    print(word,":",count)

