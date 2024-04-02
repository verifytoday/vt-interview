"""
Design a simple class structure for a zoo management system
where you need to model Animal, Bird, and Mammal classes.

The Animal class should be the base class with common attributes like
name and age, and a method make_sound() that prints a generic sound.

The Bird and Mammal classes should inherit from Animal but
override the make_sound() method to print specific sounds for a bird and a mammal, respectively.

Additionally, implement a method describe() in the Animal class that
prints a description of the animal including its name, age, and the sound it makes.

Provide an example of how to create instances of Bird and Mammal
and demonstrate polymorphism with the make_sound() method.


Extra:
How would you extend this system to include more specific animal types,
like Eagle under Bird or Tiger under Mammal, each with its unique behaviors?

What modifications would you make to the class structure to accommodate new requirements,
such as tracking the diet of each animal (e.g., carnivore, herbivore)?

Discuss how you would use interfaces or abstract classes in Python
to enforce certain methods in the subclasses.
"""