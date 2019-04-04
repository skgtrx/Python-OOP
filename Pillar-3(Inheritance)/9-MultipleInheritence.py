''' Type 2 - Multiple Inheritence '''

# Here, multiple inheritence simply means that a derived class can have more than one base class.
# Derived class can inherit all the attributes and methods of its parent class/es.
# Simple example Derived(child) and Base(Mother,Father).

class OperatingSystem:
    multitasking = True
    name = "MacOSX"
class Apple:
    website = "www.apple.com"
    name = "MacOSApple"
class MacBook(OperatingSystem,Apple): # Here, we've passed multiple classes as base.
    def __init__(self):
        if self.multitasking is True: # Here we're inheriting multitasking attribute from OperatingSystem class.
            print("This is a multi tasking system. Visit {} for more details.".format(self.website)) # Similarly, website form Apple class
            print("name : ",self.name)
# Point is, what if both the base class have same attribute name then which one will be called?
# Simple answer to this question is order of passing of base class matters.
mac1 = MacBook()