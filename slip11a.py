#Write a Python program to compute element-wise sum of given tuples. 
# Original lists: (1, 2, 3, 4) (3, 5, 2, 1) (2, 2, 3, 1)
# Element-wise sum of the said tuples: (6, 9, 8, 6)


x = (1,2,3,4)
y = (3,5,2,1)
z = (2,2,3,1)
print("Original lists:")
print(x)
print(y)
print(z)
print("\nElement-wise sum of the said tuples:")
result = tuple(map(sum, zip(x, y, z)))
print(result)