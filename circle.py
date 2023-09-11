# The circle defines a class that perform
# calculations related to circles.
import math

class Circle:

    def __init__(self):
        self.radius = 1.0
        
    def calculate_area(self):
        return math.pi * self.radius**2

    def resize_circle(self, new_radius):
        self.radius=new_radius
        
    def calculate_circumference(self):
        return 2*math.pi*self.radius
    
    def set_radius(self,r):
        self.radius=r
        
    def get_radius(self):
        return self.radius
    
    def set_scalingFactor(self, k):
        self.__scalingFactor=k
        
    def get_scalingFactor(self):
        return self.__scalingFactor


