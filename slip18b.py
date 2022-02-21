# Write a python script to define the class person having members name, address. Create a subclass called Employee with members staffed salary. Create 'n' objects of the Employee class and display all the details of the employee.

# employee class code in Python
# class definition
class Employee:
    __id = 0
    __name = ""
    __gender = ""
    __city = ""
    __salary = 0

    # function to set data
    def setData(self, id, name, gender, city, salary):
        self.__id = id
        self.__name = name
        self.__gender = gender
        self.__city = city
        self.__salary = salary

        # function to get/print data
    def showData(self):
        print("Id\t\t:", self.__id)
        print("Name\t:", self.__name)
        print("Gender\t:", self.__gender)
        print("City\t:", self.__city)
        print("Salary\t:", self.__salary)

# main function definition


def main():
    # Employee Object
    emp = Employee()
    emp.setData(1, 'Syed Nadeem Hussain', 'Male', 'Pune', 50000)
    emp.showData()


if __name__ == "__main__":
    main()
