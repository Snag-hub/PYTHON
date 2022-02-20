#Define a class Date (Day, Month, Year) with functions to accept and display it. Accept date from user. Throw user defined exception “invalid Date Exception” if the date is invalid.


class Date():
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        print("Day: ", self.day)
        print("Month: ", self.month)
        print("Year: ", self.year)
    
    def accept(self):
        self.day = int(input("Enter day: "))
        self.month = int(input("Enter month: "))
        self.year = int(input("Enter year: "))
        if self.day > 31 or self.day < 1 or self.month > 12 or self.month < 1 or self.year < 1:
            raise Exception("Invalid Date Exception")
        else:
            self.display()
  
string1 = Date(1,1,1)
string1.accept()

    

    
