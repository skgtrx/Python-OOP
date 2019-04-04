''' Static and Instance Methods '''
### Instance Methods : 
# All the methods we have used so far in the class are instance methods.
# Instance Methods requires self parameter to be passed as an argument.
# For accessing Insntance methods object must be created/required.

### Static Methods :
# These methods belongs to class itself.
# They don't require any object/Instance to access them. They can simply be access by class itself.
# Also, due to no instance required there is no need to pass self as an argument to them.

## Let's see how to create static method.
class Employee:
    def employeeDetails(self):
        self.name = 'Ben'
    @staticmethod # decorator
    # Decorators are functions that take another function and extends their functionality.
    def welcomeMessage():
        print("Welcome to our organisation")

emp = Employee()
emp.employeeDetails()
print(emp.name)
emp.welcomeMessage() 
Employee.welcomeMessage()
# We are not getting any error for not passsing self.
# static method can be accessed by both object and class itself.
