# Create a list a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] and write a python program that prints out all the elements of the list that are less than 5 

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
    if i < 5:
        print(i)

# Instead of printing the elements one by one, make a new list that has all the elements less than 5 from
# this list in it and print out this new list.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
for i in a:
    if i < 5:
        b.append(i)
print(b)

# Write this in one line of Python.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
[b.append(i) for i in a if i < 5]
print(b)
