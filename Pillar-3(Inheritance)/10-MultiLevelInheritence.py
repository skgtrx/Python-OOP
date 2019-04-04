''' Type 3 - Multi Level Inheritence '''

# It's like same as previous section of multiple inheritence but here we have multi levels of class
# class at lower level have access to the methods and attributes of all the class above it.

class MusicalInstruments:
    numberOfMajorKeys = 12

class StringInstruments(MusicalInstruments):
    typeOfWood = "Tonewood"

class Guitar(StringInstruments):
    def __init__(self):
        self.numberOfStrings = 6
        print("This Guitar consists of {} strings. Is is made of {} and it can play {} keys.".format(self.numberOfStrings,
        self.typeOfWood,self.numberOfMajorKeys))

guitar = Guitar()