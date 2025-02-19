from math import pi

def circle_area(r):
    """Calculate the area of a circle given a radius."""
    if not isinstance(r, (int, float)) or r < 0:
        raise ValueError("Invalid radius. Must be a non-negative number.")
    return pi * (r ** 2)

def trapezium_area(a, b, h):
    """Calculate the area of a trapezium given two bases and height."""
    if not all(isinstance(i, (int, float)) and i > 0 for i in [a, b, h]):
        raise ValueError("All dimensions must be positive numbers.")
    return 0.5 * (a + b) * h

def ellipse_area(a, b):
    """Calculate the area of an ellipse given two axes."""
    if not all(isinstance(i, (int, float)) and i > 0 for i in [a, b]):
        raise ValueError("Both axes must be positive numbers.")
    return pi * a * b

def rhombus_area(d1, d2):
    """Calculate the area of a rhombus given two diagonals."""
    if not all(isinstance(i, (int, float)) and i > 0 for i in [d1, d2]):
        raise ValueError("Both diagonals must be positive numbers.")
    return 0.5 * d1 * d2
