# The circle defines a class that performs calculations related to circles.

import math

class Circle:
    """
    A class representing a circle.

    Attributes:
        radius (float): The radius of the circle.
        scalingFactor (float): The scaling factor for resizing the circle.

    Methods:
        calculate_area(): Calculates the area of the circle.
        resize_circle(new_radius): Resizes the circle by changing its radius.
        calculate_circumference(): Calculates the circumference of the circle.
        set_radius(r): Sets the radius of the circle.
        get_radius(): Returns the radius of the circle.
        set_scalingFactor(k): Sets the scaling factor for resizing the circle.
        get_scalingFactor(): Returns the scaling factor for resizing the circle.
    """

    def __init__(self):
        self.radius = 1.0
        
    def calculate_area(self):
        """
        Calculates the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return math.pi * self.radius**2

    def resize_circle(self, new_radius):
        """
        Resizes the circle by changing its radius.

        Parameters:
            new_radius (float): The new radius of the circle.
        """
        self.radius = new_radius
        
    def calculate_circumference(self):
        """
        Calculates the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2*math.pi*self.radius
    
    def set_radius(self, r):
        """
        Sets the radius of the circle.

        Parameters:
            r (float): The radius of the circle.
        """
        self.radius = r
        
    def get_radius(self):
        """
        Returns the radius of the circle.

        Returns:
            float: The radius of the circle.
        """
        return self.radius
    
    def set_scalingFactor(self, k):
        """
        Sets the scaling factor for resizing the circle.

        Parameters:
            k (float): The scaling factor for resizing the circle.
        """
        self.scalingFactor = k
        
    def get_scalingFactor(self):
        """
        Returns the scaling factor for resizing the circle.

        Returns:
            float: The scaling factor for resizing the circle.
        """
        return self.scalingFactor
# The circle defines a class that perform
# calculations related to circles.
import math

class Circle:
    def __init__(self):
        self.__radius = 1.0
        
    def calculate_area(self):
        return math.pi * self.__radius**2

    def resize_circle(self, new_radius):
        self.__radius = new_radius
        
    def calculate_circumference(self):
        return 2*math.pi*self.__radius
    
    def set_radius(self, r):
        self.__radius = r
        
    def get_radius(self):
        return self.__radius
    
    def set_scalingFactor(self, k):
        self.__scalingFactor = k
        
    def get_scalingFactor(self):
        return self.__scalingFactor

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


