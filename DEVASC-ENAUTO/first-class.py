class Dog():
    
    # Class object attribute
    # Same for any instance of a class
    species = 'mammal'

    def __init__(self, breed, name, spots):
        #Attributes
        #We take in the argument
        #Assign it using self.attribute_name
        self.breed = breed
        self.name = name

        #Expect boolean True/Flase
        self.spots = spots

    # Operations/Actions ---> Methods
    def bark(self, number):
        print("Woof! My name is {} and the number is {}".format(self.name,number))

class Circle():

    #CLASS OBJECT ATTRIBUTE
    pi = 3.14

    def __init__(self,radius=1):
        self.radius = radius
        self.area = radius*radius*self.pi
    
    #METHOD
    def get_circumference(self):
        return self.radius * self.pi * 2


#my_dog = Dog('Catahoula', 'Appa', False)

#my_dog.bark(10)

my_circle = Circle()

print(my_circle.get_circumference())