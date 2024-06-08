strings_list = ['abc', 'xyz', 'aba', '1221']

count = 0
for s in strings_list:
    if len(s) >= 2 and s[0] == s[-1]:
        count += 1

print("same and last character:", count)
