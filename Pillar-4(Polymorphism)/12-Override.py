''' Polymorphism '''

# Polymorphism means 2 things things which looks same but behaves diffenently shows the polymorphics property of them.
# For Example: + in case of 2 intigers do sum but in case of stings do concatination.
# Which is also know as overriding.

### Situation ###
# We have an employee class and a trainee class.
# Trainee has inherited the employee class.
# But the number of working hours for the trainee is different then that of employee.
# How we can set different number of working hours for Trainee?
# What if want to reset it back to tthe base class class value then How we'll do it?
  
class Employee: # Base class
    def setNumberOfWorkingHours(self):
        self.numberOfWorkingHours = 40
    
    def displayNumberOfWorkingHours(self):
        print(self.numberOfWorkingHours)

class Trainee(Employee): # Derived class
    # For overriding we need to redifine it here again.
    def setNumberOfWorkingHours(self):
        self.numberOfWorkingHours = 45

    # for getting back to the base class value we have to use super().
    def resetNumberOfWorkingHours(self):
        super().setNumberOfWorkingHours()

# Here we created our employee
emp = Employee()
# Set the number of working hours for the employee
emp.setNumberOfWorkingHours()
print("Number of working hours of employee :",end=" ")
emp.displayNumberOfWorkingHours()  

# Here we created the trainee
trainee = Trainee()

# Let's set the value of number of working hours values for trainee.
trainee.setNumberOfWorkingHours()
# Let's print the number of working hours after setting its value.
print("Number of working hours after setting :",end=" ")
trainee.displayNumberOfWorkingHours()

# Let's set the number of working hours value to the base class value.
trainee.resetNumberOfWorkingHours()
# Let's print the number of working hours after resetting.
print("Number of working hours after resetting :",end=" ")
trainee.displayNumberOfWorkingHours()