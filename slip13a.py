# Write a Python program to input a positive integer. Display correct message for correct and incorrect input. (Use Exception Handling)

while True:
    try:
        n = input("Please enter an integer: ")
        n = int(n)
        break
    except ValueError:
        print("No valid integer! Please try again ...")
print("Great, you successfully entered an integer!")
