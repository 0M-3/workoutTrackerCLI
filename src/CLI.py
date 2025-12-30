import questionary
from database import get_workouts


def start_cli():
    while True:
        action = (
            questionary.select(
                "Workout Tracker Menu:",
                choices = ["Add today's workout", "View my recent workouts", "Delete a workout", "Visualize the workout data", "Exit"]
                ).ask()
        )
        match action:
            case "Add today's workout": 
                Add_workout()
            case "View my recent workouts": 
                View_workout()
            case "Delete a workout": 
                Delete_workout()
            case "Visualize the workout data": 
                Visualize_workout()
            case "Exit":
                print("Exit")
                break

def Add_workout():
    workouts_list = get_workouts()
    select_workout = (
        questionary.select(
            "Select a workout:",
            choices = workouts_list
        ).ask()
    )
    print(select_workout)


def View_workout():
    print("View my recent workouts")
def Delete_workout():
    print("Delete a workout")

def Visualize_workout():
    print("Visualize the data")

if __name__ == '__main__':
    start_cli()
