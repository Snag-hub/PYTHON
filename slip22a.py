# Write a python class to accept a string and number n from user and display n repetition of strings by overloading * operator.


class String:
    def __init__(self, str, n):
        self.str = str
        self.n = n

    def __mul__(self, other):
        return self.str * self.n


