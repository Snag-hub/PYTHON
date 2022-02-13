# Write a Python Program to Check if given number is prime or not. Also find factorial of the given no using user defined function.


num = int(input("Enter a number: "))
flag = False
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break

if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")

#find factorial of the given no using user defined function
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)

print("Factorial of", num, "is", factorial(num))