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
    