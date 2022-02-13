# Python Program to Create a Class in which One Method Accepts a String from the User and Another method Prints it. Define a class named Country which has a method called print Nationality. Define subclass named state from Country which has a mehtod called printState. Write a method to print state, country and nationality.


class slip30b():
    def __init__(self):
        self.string=""
 
    def get(self):
        self.string=input("Enter Country: ")
 
    def put(self):
        print("Country is:")
        print(self.string)

class country:
    def printNationality(self):
        print("Nationality is:")
        print(self.string)


class state(country):
  def printState(self):
    print("State is:")
    print(self.string)


obj=slip30b()
obj.get()
obj.put()

obj1=state(country)
obj.printNationality()
obj1.printState()


