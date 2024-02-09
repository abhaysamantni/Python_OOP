class Shape():
    def __init__(self):
        self.fillColor = "White"
        self.borderColor = "Black"
        self.__borderWidth = 1.0

    def set_fillColor(self, x):
        self.fillColor = x
    
    def set_borderColor(self, y):
        self.borderColor = y
    
    def get_borderColor(self):
        return self.borderColor
    
    def get_fillColor(self):
        return self.fillColor
    

class Rectangle(Shape):
    def __init__(self):
        Shape.__init__(self)
        self.length = 1.0
        self.width = 2.0

    def set_length(self, x):
        self.length = x

    def set_width(self, y):
        self.width = y

    def get_length(self):
        return self.length
    
    def get_width(self):
        return self.width
    
    def calculate_area(self):
        return self.length * self.width
    
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)
    
class Triangle(Shape):
    def __init__(self):
        Shape.__init__(self)
        self.side1 = 1.0
        self.side2 = 2.0
        self.side3 = 3.0

    def set_side1(self, x):
        self.side1 = x

    def set_side2(self, y):
        self.side2 = y

    def set_side3(self, z):
        self.side3 = z

    def get_side1(self):
        return self.side1
    
    def get_side2(self):
        return self.side2
    
    def get_side3(self):
        return self.side3
    
    def calculate_area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5
    
    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3