''' 
In this series we'll be learning about:
1) Types of Inheritence
2) Abstract base class
'''

''' Type 1 - Single Inheritence '''
# Here we'll be going to create a parent class and a child class.
# Both the classes have their own attributes.
# But we'll let chile class inherit parent class attributes and methods.

# Base Class
class Apple: # Parent class
    manufacturer = "Apple Inc."
    contactWebsite = "www.apple.com/contact"

    def contactDetails(self):
        print("To contact us, log on to {}".format(self.contactWebsite))

# Derived Class
class MacBook(Apple): # Child of Apple class, syntex - class child(Parent)
    def __init__(self):
        self.yearOfManufacture = 2017

    def manufactureDetails(self):
        print("This MacBook was manufactured in the year {} by {}".format(self.yearOfManufacture,self.manufacturer))    
        # Now, let's understand how this actually happened?
        # We call the manufacturer attribute and didn't throw the error. 
        # A system work here, first python looks at the instance attribute, if not available then class attribute if still 
        # not available and base class is present then looks for the base class attribute.
    
# Now, it's time to launch our macBooks
mac1 = MacBook()
# Notice that we won't create an instance of Apple class as their only one Apple exists.
mac1.manufactureDetails()
mac1.contactDetails()