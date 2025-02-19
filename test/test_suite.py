import unittest
import sys
import os

# Ensure the app directory is in the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now import the functions from the app module

from test_lab3_farhan_Ameilia import TestShapes


def run_tests(choice):
    suite = unittest.TestSuite()

    if choice == 'c':
        suite.addTest(TestShapes('test_circle_area_valid'))
        suite.addTest(TestShapes('test_circle_area_zero'))
        suite.addTest(TestShapes('test_circle_area_invalid'))
    elif choice == 't':
        suite.addTest(TestShapes('test_trapezium_area_valid'))
        suite.addTest(TestShapes('test_trapezium_area_invalid'))
    elif choice == 'e':
        suite.addTest(TestShapes('test_ellipse_area_valid'))
        suite.addTest(TestShapes('test_ellipse_area_invalid'))
    elif choice == 'r':
        suite.addTest(TestShapes('test_rhombus_area_valid'))
        suite.addTest(TestShapes('test_rhombus_area_invalid'))
    else:
        print("Invalid choice. Exiting.")
        return

    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    print("Enter a shape to test ('c' for Circle, 't' for Trapezium, 'e' for Ellipse, 'r' for Rhombus):")
    choice = input().strip().lower()
    run_tests(choice)
