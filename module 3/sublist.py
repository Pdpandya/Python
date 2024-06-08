lst = [1, 2, 3, 4, 5, 6, 7]

sublist1 = [3, 4, 5]
sublist2 = [6, 8]

# Convert lists to strings
main_str = ' '.join(map(str, lst))
sublist1_str = ' '.join(map(str, sublist1))
sublist2_str = ' '.join(map(str, sublist2))

if sublist1_str in main_str:
    print("Sublist 1 is present in the main list.")
else:
    print("Sublist 1 is not present in the main list.")

if sublist2_str in main_str:
    "Sublist 2 is present in the main list."
else:
   "Sublist 2 is not present in the main list." 
       


