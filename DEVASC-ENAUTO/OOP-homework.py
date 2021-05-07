import math

class Line:
    def __init__(self,coor1,coor2):
        self.coor1 = tuple(coor1)
        self.coor2 = tuple(coor2)


    def distance(self):
        return math.sqrt((self.coor2[0] - self.coor1[0])**2 + (self.coor2[1] - self.coor1[1])**2)

    def slope(self):
        return (self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0])


#line1 = Line((3,2), (8,10))


#print(line1.distance())

#print(line1.slope())


class Cylinder:

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return math.pi * self.radius**2 * self.height
        
    def surface_area(self):
        return (2 * math.pi * self.radius * self.height) + (2 * math.pi * self.radius**2)
        

c = Cylinder(2,3)

print(c.volume())

print(c.surface_area())