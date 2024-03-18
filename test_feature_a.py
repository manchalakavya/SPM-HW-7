# test_feature_a.py
import unittest
from Avg_Vel import calculate_average_velocity

class TestCalculateAverageVelocity(unittest.TestCase):

    def test_with_multiple_points(self):
        """Test calculate_average_velocity with multiple points."""
        points = [10, 20, 30]
        expected = 20
        self.assertEqual(calculate_average_velocity(points), expected)

    def test_with_empty_list(self):
        """Test calculate_average_velocity with an empty list returns 0."""
        self.assertEqual(calculate_average_velocity([]), 0)

    def test_with_single_point(self):
        """Test calculate_average_velocity with a single point returns that point."""
        points = [50]
        expected = 50
        self.assertEqual(calculate_average_velocity(points), expected)

    def test_with_negative_points(self):
        """Test calculate_average_velocity with negative points."""
        points = [-10, -20, -30]
        expected = -20
        self.assertEqual(calculate_average_velocity(points), expected)

    def test_with_zero_points(self):
        """Test calculate_average_velocity with zeros."""
        points = [0, 0, 0]
        expected = 0
        self.assertEqual(calculate_average_velocity(points), expected)

if __name__ == '__main__':
    unittest.main()
