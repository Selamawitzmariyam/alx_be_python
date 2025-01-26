import math

class Shape:
    def area(self):
        """Base method to calculate area. Should be overridden in derived classes."""
        raise NotImplementedError("Subclasses must implement the area() method.")

class Rectangle(Shape):
    def __init__(self, length, width):
        """
        Initialize a Rectangle instance.
        :param length: Length of the rectangle.
        :param width: Width of the rectangle.
        """
        self.length = length
        self.width = width

    def area(self):
        """Override the area() method to calculate the area of the rectangle."""
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        """
        Initialize a Circle instance.
        :param radius: Radius of the circle.
        """
        self.radius = radius

    def area(self):
        """Override the area() method to calculate the area of the circle."""
        return math.pi * self.radius ** 2

# Example usage:
def main():
    # Create instances of Rectangle and Circle
    rectangle = Rectangle(10, 5)
    circle = Circle(7)

    # Display the areas using polymorphism
    print(f"Area of the rectangle: {rectangle.area():.2f}")
    print(f"Area of the circle: {circle.area():.2f}")

if __name__ == "__main__":
    main()