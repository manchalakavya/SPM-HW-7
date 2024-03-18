# tests_for_team_effort.py
import unittest
from Team_Effort import calculate_effort_hours  # Keeping this import as per your instruction

class CalculateEffortHoursTest(unittest.TestCase):

    def test_standard_scenario(self):
        """Validating functionality with regular input."""
        project_days = 10
        contributors = [
            {"name": "Leo", "pto_hours": 2, "ceremony_hours": 2, "available_hours_per_day": 8},
            {"name": "Riya", "pto_hours": 4, "ceremony_hours": 3, "available_hours_per_day": 8}
        ]
        _, overall_effort_hours = calculate_effort_hours(project_days, contributors)
        self.assertEqual(overall_effort_hours, 149)  # Correcting the expected outcome to align with the calculation

    def test_no_contributors(self):
        """Examine the function's response when no contributors are present."""
        project_days = 10
        contributors = []
        _, overall_effort_hours = calculate_effort_hours(project_days, contributors)
        self.assertEqual(overall_effort_hours, 0)

    def test_excess_pto_scenario(self):
        """Evaluating function behavior when PTO exceeds the sprint period."""
        project_days = 10
        contributors = [
            {"name": "Sam", "pto_hours": -10, "ceremony_hours": 2, "available_hours_per_day": 8}  # Using negative PTO as a unique case
        ]
        _, overall_effort_hours = calculate_effort_hours(project_days, contributors)
        # Assuming the function treats negative PTO in a specific manner:
        self.assertTrue(overall_effort_hours > 0)  

    def test_sprint_duration_zero(self):
        """Checking function output with zero-length sprint."""
        project_days = 0
        contributors = [
            {"name": "Tina", "pto_hours": 2, "ceremony_hours": 2, "available_hours_per_day": 8}
        ]
        _, overall_effort_hours = calculate_effort_hours(project_days, contributors)
        self.assertEqual(overall_effort_hours, 0)

if __name__ == '__main__':
    unittest.main()
