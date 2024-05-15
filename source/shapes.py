
import math


class shape:
  def area(self):
    pass

  def perimeter(self):
    pass

class circle(shape):
  def __init__(self, radius):
    self.radius = radius

  def area(self):
    return math.pi * self.radius ** 2
  
  def perimeter(self):
    return math.pi * self.radius * 2