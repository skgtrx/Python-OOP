''' Abstract Base Class '''
# Abstract base class doesn't have defination on its own but 
# forces the implimentation of abstract methods in its derived classs.
# Abstract class doesn't have an instance.

### Situation ###
# We have 2 classes square and rectangle.
# Both of them area method.
# We hae to make sure that both the classes must contain area class.

# Here, for this situation an abstract class can help us.
# For creating an abstract we have to import ABCMeta and abstractmethod from abc module.

from abc import ABCMeta, abstractmethod

# Abstract class 
class Shape(metaclass = ABCMeta): # We have to pass ABCMeta to metaclass
    @abstractmethod # Decorator for making abstract method.
    def area(self):
        return 0

class Square(Shape):
    side = 4
    def area(self):
        print("Area of square: ",self.side*self.side)

class Rectangle(Shape):
    length = 10
    width = 5 
    def area(self):
        print("Area of rectangle: ",self.length*self.width)

sq = Square()
rec = Rectangle()
sq.area()
rec.area()
# We can check either abstract class is working or not by commenting area method in either of Square or Rectangle.

# Let's try creating object of abstract class
#s = Shape()  
#TypeError: Can't instantiate abstract class Shape with abstract methods area
         