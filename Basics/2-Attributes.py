''' In this section we will see attributes '''
# In this section we'll be learning about.
# Types of attributes : Class and Instance Attributes


### Class Attributes and Instance Attributes

## Class Attributes : The attributes which are same for all the instances.
## Instance Attributes : The attributes which are as per the instances.

# For example :
# In previous section we have used only class attributes as the value of attributes are same for all the instances.
# So, class attribute is something which is common among all its instances.
class Employee:
    numberOfWorkingHours = 40 # Class Attributes

# Let's create 2 employee objects
emp1 = Employee()
emp2 = Employee()
# Let's print number of working hours for both the employees
print("Number of working hours for Employee 1 : ",emp1.numberOfWorkingHours)
print("Number of working hours for Employee 2 : ",emp2.numberOfWorkingHours)
# It's same for both

# What if we want to change the value of the class attribute?
# We can do that by - class_name.attribute_name = value
Employee.numberOfWorkingHours = 45
# Let's again print number of working hours for both the employees
print("Number of working hours for Employee 1 : ",emp1.numberOfWorkingHours)
print("Number of working hours for Employee 2 : ",emp2.numberOfWorkingHours)

# Now let's see how we can create an instance attribute and what are it's significance.
emp1.name = 'Raja'
print(emp1.name)
# What if we try to the same for emp2
#print(emp2.name) # We'll get an error that name attribute is not defined for this employee.
# Let's define it and check it again.
emp2.name = 'Ben'
print(emp2.name) # See it worked but it printed Ben not Raja.

# Now, what if i want to hange the numberOfWorkingHours for emp1.
# Well i can create an instance attribute.
emp1.numberOfWorkingHours = 40 
# let's see weather numberOfWorkingHours is change for emp2 as well.
print("Number of working hours for Employee 1 : ",emp1.numberOfWorkingHours) # 40
print("Number of working hours for Employee 2 : ",emp2.numberOfWorkingHours) # 45

# Question: What just happened?
# When an object access any attribute python first of all check wheather that object has same instance attribute or not.
# IF yes then it prints it's value else it moves to the value of class attribute. In case class also don't have it then it throws error.



































