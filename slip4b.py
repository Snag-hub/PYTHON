# Define a class Employee having members id, name, department, salary. Create a subclass called manager with member bonus. Define methods accept and display in both the classes. Create n objects of the manager class and display thedetails of the manager having the maximum total salary (salary+bonus).


class EmployeeInfo:
    def getData(self, empid, ename, salary, dept):
        self.empno = empid
        self.ename = ename
        self.salary = salary
        self.dept = dept

    def displayEmployee(self):
        print("Employee Number:", self.empno)
        print("Employee Name:", self.ename)
        print("Salary:", self.salary)
        print("Department:", self.dept)


class Manager(EmployeeInfo):
    def getBonus(self, bonus):
        self.bonus = bonus

    def displayBonus(self):
        print("Bonus:", self.bonus)


r = int(input("Enter Emp ID:"))
n = input("Enter Emp Name:")
c = input("Enter Dept Name:")
d = int(input("Enter Salary:"))
m = int(input("Enter Bonus:"))
stud1 = Manager()
stud1.getData(r, n, c, d)
stud1.getBonus(m)
stud1.displayEmployee()
stud1.displayBonus()
