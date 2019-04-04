''' How to fully initialize an object using special method - init method '''

# Let's see an example to understand it's use.

class Employee:
    def enterEmployeeDetails(self):
        self.name='Mark'
    def displayEmployeeDetails(self):
        print(self.name)

emp = Employee()
#emp.displayEmployeeDetails()
# This above statement is giving error: the name attribute is not defined.
# Well, here if we want it to display details then enterEmployeeDetails() has to be run first.

## For solving above issue we have an special method called __init__().
# All the special methods in python starts and ends with '__' 
# Now, let's use __init__().

class Employee:
    def __init__(self):
        self.name='Mark'
    def displayEmployeeDetails(self):
        print(self.name)

emp = Employee()
emp.displayEmployeeDetails()

# Now, displayEmployeeDetails() is working. 
# Question is how did it happend?
# In class there is something known as constructor which are methods call just after the creation of instance/object.
# So, when we created the object emp __init__() called by default.
# Same way when we initialize all the attributes in the class the its object is known as fully initialized object.
# But still we have a problem and that is, if we create another object of same class them again the employee name would be the same.

## We can also pass arguments to the __init__().
# Let's see how to do it.
class Employee:
    def __init__(self,name):
        self.name=name
    def displayEmployeeDetails(self):
        print(self.name)

emp1 = Employee('Ben')
emp2 = Employee('Mark')
emp1.displayEmployeeDetails() # Ben
emp2.displayEmployeeDetails() # Mark