''' Importance of self keyword '''

# let's understand it by the help of an example:
class Employee:
    def employeeDetails():
        pass

emp = Employee()
# emp.employeeDetails() #TypeError: employeeDetails() takes 0 positional arguments but 1 was given.
# We haven't given any argument then why it's throwing this kind of error.

# emp.employeeDetails() is equivalent to Employee.employeeDetails(emp). Both are valid statements but emp.employeeDetails() it more popular.
# So, it's passing emp but it's not defined to take an argument.
# That's why we use self.

class Employee:
    def employeeDetails(self):
        self.name = "Ram" # class attribute
        print(self.name)

emp = Employee()
emp.employeeDetails() # No error
Employee.employeeDetails(emp)

# Also, it's not necessary that self has to be self but it can be any.
class Employee:
    def employeeDetails(con):
        con.name = "Ram" # class attribute
        print(con.name)

emp = Employee()
emp.employeeDetails() # No error

## There are few more situations where self comes handy.
class Employee:
    def employeeDetails(self):
        self.name = "Ram" # class attribute
        age = 25 # situation
        print(self.name)
        print(age)

emp = Employee()
emp.employeeDetails()
# You might be thinking age is working fine without self then why to use self?
# Well, what if i create another method in Employee class and want to use that age attribute.
# Then, would i be able to use it? NO. 
# Let's see
class Employee:
    def employeeDetails(self):
        self.name = "Ram" # class attribute
        age = 25 # situation
        print(self.name)
        print(age)
    def employeeAge(self):
        print(age)

emp = Employee()
emp.employeeDetails()
emp.employeeAge() # Here come error age is not defined
# Now, let's check it again with self 
class Employee:
    def employeeDetails(self):
        self.name = "Ram" # class attribute
        self.age = 25 # situation
        print(self.name)
        print(self.age)
    def employeeAge(self):
        print(self.age)

emp = Employee()
emp.employeeDetails() # We have to run it first because this method is creating age attribute.
emp.employeeAge()

