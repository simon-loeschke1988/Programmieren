import math
from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self,name):
        self.name = name
    @abstractmethod
    def area(self):
        pass
    
    def describe(self):
        return f"{self.name}"
    
class Rectangle(Shape):
    def __init__(self, height, width ,name="Rectangle"):
        super().__init__(name)
        self.height= height
        self.width= width
    def area(self):
        pass
    
    
class Circle(Shape):
    def __init__(self, radius ,name="Circle"):
        super().__init__(name)
        self.r= radius
    
    def area(self):
        return math.floor(math.pi * (self.r**2))

class Triangle(Shape):
    def __init__(self, height, base,name="Triangle"):
        super().__init__(name)
        self.h= height
        self.b= base
    
    def area(self):
        return 0.5 * self.h * self.b
    

    
    




if __name__ == "__main__":
    pass