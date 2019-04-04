# Noun => Class
# Adjective => Attributes
# Actions => Methods
# Objects/Instances are for give life to the class.

### Through this program we are goin to check weather an employee has achieved his weekly task or not.

class Employee: # Here we are defining an Employee
    # Let's define the ideal properties/attributes of our employee.
    name = "Ben"
    designation = "Sales Executive"
    sales_made_this_week = 6

    # let's create method for checking our objective
        # self is the default argument of constructor used to access attributes of class
    def hasAchivedTarget(self): 
        # Min 5 sales are required to achieve target. 
        if(self.sales_made_this_week>=5):
            print("Target Achieved")
        else:
            print(self.name," couldn't achieve the target")

# Now, let give life to our employee Ben.
# Make instance/object
emp1 = Employee()
# let's see what's the name of emp1
print(emp1.name)
# let's see what's tthe designation of emp1
print(emp1.designation)
# let's see weather our emp1 achieved the target or not.
emp1.hasAchivedTarget()

'''
Q. What if we create another object of Employee() does it make any difference between emp1 and emp2?
A. No, which means the way we have created attributed is not the correct way. As class is something which general for a group, in our case 
   general for employees.
'''

'''
TakeAway:
Now, we know how to create a class, attributes, methods and objects. Also know how to use them in general.
'''

''' 
Bonus:
In python everything is object, for example-
>>> num = [1,2,3]
>>> type(num)
>>> <class 'list'>
This simply means that we have created num as an object of class list. That's why we can access its methods like append etc.
>>> num.append(4)
'''