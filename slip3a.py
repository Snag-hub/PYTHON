# Write a Python program to check if a given key already exists in a dictionary. If key exists replace with another key/value pair.

def checkKey(dict, key):

    if key in dict.keys():
        print("Present, ", end=" ")
        print("value =", dict[key])
    else:
        print("Not present")

dict = {'a': 100, 'b': 200, 'c': 300}

key = 'b'
checkKey(dict, key)

key = 'w'
checkKey(dict, key)
