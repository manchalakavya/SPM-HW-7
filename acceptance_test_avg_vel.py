import subprocess
import unittest

class FeatureAAcceptanceTest(unittest.TestCase):
    def test_average_velocity_happy_path(self):
        """Simulate user entering multiple sprint points and check average velocity calculation."""
        # Prepare the command to run your Python script
        command = ["python", "Avg_Vel.py"]
        # Simulate input for your script
        user_input = "10,20,30\n"
        # Expected output
        expected_output = "Average Velocity: 20.0\n"

        # Run your script with simulated input
        process = subprocess.run(command, input=user_input, text=True, capture_output=True)
        # Validate the output
        self.assertIn(expected_output, process.stdout)

    def test_average_velocity_empty_input(self):
        """Simulate user entering no sprint points and check the output."""
        command = ["python", "Avg_Vel.py"]
        user_input = "\n"  # Simulating pressing Enter without input
        expected_output = "Average Velocity: 0\n"

        process = subprocess.run(command, input=user_input, text=True, capture_output=True)
        self.assertIn(expected_output, process.stdout)

if __name__ == '__main__':
    unittest.main()
