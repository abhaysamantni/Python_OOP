import shape
import math

class circleoop(shape.Shape):
    def __init__(self):
        shape.Shape.__init__(self)
        self.radius=1.0
        self.scalingFactor=1.0

    def calculateArea(self):
        return math.pi*self.radius*self.radius*self.scalingFactor
