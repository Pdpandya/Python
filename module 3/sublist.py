# Main list
main_list = [1, 2, 3, 4, 5, 6, 7]

# Sublists to check
sublist1 = [3, 4, 5]
sublist2 = [6, 8]

# Iterate through the main list
for i in range(len(main_list) - len(sublist1) + 1):
    # Check if sublist1 matches consecutive elements of the main list
    if main_list[i:i+len(sublist1)] == sublist1:
        print("Sublist 1 is present in the main list.")
        break
else:
    print("Sublist 1 is not present in the main list.")

# Iterate through the main list
for i in range(len(main_list) - len(sublist2) + 1):
    # Check if sublist2 matches consecutive elements of the main list
    if main_list[i:i+len(sublist2)] == sublist2:
        print("Sublist 2 is present in the main list.")
        break
else:
    print("Sublist 2 is not present in the main list.")
