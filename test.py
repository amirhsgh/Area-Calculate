from shape import *
from area_calculator import *

def main():
    circle = Circle(5)
    rectangle = Rectangle(10, 20)
    triangle = Triangle(10, 20)
    area = AreaCalculator()
    
    area_rec = rectangle.calculate_area_with(area)
    area_circle = circle.calculate_area_with(area)
    area_triangle = triangle.calculate_area_with(area)
    print(area_circle)
    print(area_rec)
    print(area_triangle)

main()