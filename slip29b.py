#Write a Python script to sort (ascending and descending) a dictionary by key and value. 

dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

ascending = sorted(dict.items())
descending = sorted(dict.items(), reverse=True)

print("Ascending: ", ascending)
print("Descending: ", descending)