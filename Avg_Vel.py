input_string = input("Enter sprint points: ").strip()  # Ensure input is stripped of whitespace
if not input_string:  # Check if the input string is empty
    previous_sprints_points = []  # Assign an empty list if no input is provided
else:
    previous_sprints_points = [int(point.strip()) for point in input_string.split(',') if point.strip()]  # Ensure only non-empty strings are converted to integers


def calculate_average_velocity(points):
    return sum(points) / len(points) if points else 0

average_velocity = calculate_average_velocity(previous_sprints_points)
print(f"Average Velocity: {average_velocity}")