def calculate_effort_hours(sprint_days, team_members):
    """
    Calculates and returns the available effort hours for each team member and the total for the team.

    Parameters:
    - sprint_days (int): Number of days in the sprint.
    - team_members (list): A list of dictionaries, each representing a team member's details.

    Returns:
    - tuple: (member_hours, total_effort_hours_for_team) where member_hours is a dictionary mapping each team member's name to their available effort hours, and total_effort_hours_for_team is the sum of all members' hours.
    """
    total_effort_hours_for_team = 0
    member_hours = {}
    for member in team_members:
        total_hours_available = sprint_days * member["available_hours_per_day"]
        actual_available_hours = total_hours_available - member["pto_hours"] - member["ceremony_hours"]
        actual_available_hours = max(actual_available_hours, 0)
        member_hours[member['name']] = actual_available_hours
        total_effort_hours_for_team += actual_available_hours
        
    return member_hours, total_effort_hours_for_team

def get_team_input():
    """
    Collects input for sprint days and team members from the user and calculates effort hours.

    This function should only be called when executing the script directly.
    """
    sprint_days = int(input("Enter sprint days: "))
    team_members = []
    num_members = int(input("Enter the number of team members: "))
    for _ in range(num_members):
        name = input("Enter team member's name: ")
        pto_hours = int(input(f"Enter PTO hours for {name}: "))
        ceremony_hours = int(input(f"Enter ceremony hours for {name}: "))
        available_hours_per_day = int(input(f"Enter available hours per day for {name}: "))
        team_members.append({
            "name": name,
            "pto_hours": pto_hours,
            "ceremony_hours": ceremony_hours,
            "available_hours_per_day": available_hours_per_day
        })

    member_hours, total_effort_hours = calculate_effort_hours(sprint_days, team_members)
    for name, hours in member_hours.items():
        print(f"{name}: Available Effort-Hours = {hours}")
    print(f"Total Available Effort-Hours for Team: {total_effort_hours}")

if __name__ == "__main__":
    get_team_input()
