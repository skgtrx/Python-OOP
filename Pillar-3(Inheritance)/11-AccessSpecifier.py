''' In this section we'll get to know about Access Specifier Public, Private and Protected Members of the class '''

# Public Means access to anyone.
# Proctected means access to itself and serived class
# Private means only access to itself.

# In python by default these access specifier are not included into the syntex.
# Rather a naming convention has been given to them to make their use easy.
# For Public -> it's normal the way we do.
# For Protected -> Start your member name with _
# For Private -> Start your member name wit __

class Car:
    numberOfWheels = 4 # Public
    _color = "Black" # Protected
    __yearOfManufacture = 2017 # Private
class Bmw(Car):
    def __init__(self):
        print("Protected attribute color: ",self._color)
car = Car()
print("Public attribute number of Wheels : ",car.numberOfWheels)
# The same we accessed the public member we can also access the protected as well.
# But due too the naming convention it's not recommended to do so.
bmw = Bmw()
# Now, let's print private 
print("Private attribute by class year of manufacture : ",Car._Car__yearOfManufacture) # This is known as name mangling in private member.
print("Private attribute by instance year of manufacture : ",car._Car__yearOfManufacture)
# Private attribute can be access by either class or the instance of that class only.
# But it's recommended to not do it until and unless not necessary.
