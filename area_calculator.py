import math
from interfaces import AreaCalculatorInterface


class AreaCalculator(AreaCalculatorInterface):

    def calculate_circle_area(self, circle):
        return math.pi * circle.radius ** 2
    
    def calculate_rectangle_area(self, rectangle):
        return rectangle.width * rectangle.height

    def calculate_triangle_area(self, triangle):
        return (triangle.base * triangle.height) / 2