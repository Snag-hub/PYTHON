#Write a Python script using class, which has two methods get_String and print_String. get_String accept a string from the user and print_String print the string in upper case.

class slip5a:
  def __init__(self):
    self.str1=""

  def get_String(self):
    self.str1=input("Enter a string:")
    
  def print_String(self):
    print(self.str1.upper())


str1= slip5a()
str1.get_String()
str1.print_String()