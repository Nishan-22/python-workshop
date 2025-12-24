class Rectangle:
    length = 0
    breadth = 0
    def area(self):
        a = self.length * self.breadth
        print("Area of rectangle:", a)
obj1 = Rectangle()
obj1.length = 20
obj1.breadth = 30
obj1.area()

# constructor
class Circle:
    def __init__(self,radius):
        self.radius = radius
    def circumference(self):
        circum = 2 * 3.14 * self.radius
        print("Circumference of circle:", circum)
    def area(self):
        a = 3.14 * self.radius * self.radius
        print("Area of circle:", a)
obj2 = Circle(7)
obj2.circumference()
obj2.area()