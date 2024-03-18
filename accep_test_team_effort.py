import subprocess
import unittest

class FeatureBAcceptanceTest(unittest.TestCase):
    def run_script_with_inputs(self, inputs):
        """Helper function to execute the script and provide inputs."""
        command = ["python", "Team_Effort.py"]
        process = subprocess.run(command, input=inputs, text=True, capture_output=True)
        return process.stdout

    def test_happy_path(self):
        """Acceptance test for valid inputs."""
        user_inputs = "10\n2\nLeo\n2\n2\n8\nRiya\n4\n3\n8\n"
        expected_output_parts = ["Leo: Available Effort-Hours = ", "Riya: Available Effort-Hours = ", "Total Available Effort-Hours for Team: "]
        output = self.run_script_with_inputs(user_inputs)
        for part in expected_output_parts:
            self.assertIn(part, output)

    def test_unhappy_path_zero_sprint_days(self):
        """Acceptance test for zero sprint days."""
        user_inputs = "0\n1\nTina\n2\n2\n8\n"
        expected_output = "Total Available Effort-Hours for Team: 0"
        output = self.run_script_with_inputs(user_inputs)
        self.assertIn(expected_output, output)

if __name__ == '__main__':
    unittest.main()
