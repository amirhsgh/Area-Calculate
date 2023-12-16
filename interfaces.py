from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area_with(self, calculator):
        pass


class AreaCalculatorInterface(ABC):
    @abstractmethod
    def calculate_circle_area(self, circle):
        pass

    @abstractmethod
    def calculate_rectangle_area(self, rectangle):
        pass

    @abstractmethod
    def calculate_triangle_area(self, triangle):
        pass
