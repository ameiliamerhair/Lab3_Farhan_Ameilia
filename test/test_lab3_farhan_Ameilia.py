import unittest
from src.lab3_farhan_Ameilia import circle_area, trapezium_area, ellipse_area, rhombus_area

class TestShapes(unittest.TestCase):

    def setUp(self):
        """Setup method runs before each test."""
        print("\nSetup: Preparing tests...")

    def tearDown(self):
        """Teardown method runs after each test."""
        print("Teardown: Cleaning up after tests...")

    # ✅ Circle Tests
    def test_circle_area_valid(self):
        self.assertAlmostEqual(circle_area(3), 28.274333882308138)

    def test_circle_area_zero(self):
        self.assertEqual(circle_area(0), 0)

    def test_circle_area_invalid(self):
        with self.assertRaises(ValueError):
            circle_area(-1)

    # ✅ Trapezium Tests
    def test_trapezium_area_valid(self):
        self.assertEqual(trapezium_area(10, 8, 5), 45.0)

    def test_trapezium_area_invalid(self):
        with self.assertRaises(ValueError):
            trapezium_area(-10, 8, 5)

    # ✅ Ellipse Tests
    def test_ellipse_area_valid(self):
        self.assertAlmostEqual(ellipse_area(7, 4), 87.96459430051421)

    def test_ellipse_area_invalid(self):
        with self.assertRaises(ValueError):
            ellipse_area(-7, 4)

    # ✅ Rhombus Tests
    def test_rhombus_area_valid(self):
        self.assertEqual(rhombus_area(6, 8), 24.0)

    def test_rhombus_area_invalid(self):
        with self.assertRaises(ValueError):
            rhombus_area(6, -8)

if __name__ == "__main__":
    unittest.main()
