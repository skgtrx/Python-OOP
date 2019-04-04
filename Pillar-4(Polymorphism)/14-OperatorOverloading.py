''' Operator Overloading '''

# In this section we'll see how to change the functionality of a particular operator.
# As we know that in python everything is an object.
# for operators we have special methods like __add__(), __sub__(), etc.
# For example like when we add 2 integers it performs sum but when we add 2 strings it performs concatination.
# Well this is know as operator overloading but here we'll define our own defination of overloading.

### Situation ###
# We have to sum the parameter of 2 squares as object by the help of binary + operation.

class Square:
    def __init__(self,side):
        self.side = side
    # Here we go, overload __add__()
    def __add__(self,obj): # We are passing 2 arguments as objects
        return(4*self.side + 4*obj.side)
    # Also we can pass both objects as arguments
    def __sub__(obj1,obj2):
        return(4*obj1.side - 4*obj2.side)

sq1 = Square(5)
sq2 = Square(10)
print("Sum of side of both the squares : ",sq1+sq2)
print("Difference of side of both the squares : ",sq1-sq2)
