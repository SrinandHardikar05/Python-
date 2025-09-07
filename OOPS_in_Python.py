#  Object = A 'bundle' of related attributes (variables) and methods (functions)
#            Example phone, cup, book
#            You need a 'class' to create many objects

# Class = (blueprint) used to design the structure and layout of an object
# Methods = they are actions that our objects can perform  

from oops_in_python2 import Car

car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Corvette", 2025, "blue", True)

car1.drive()
car1.stop()