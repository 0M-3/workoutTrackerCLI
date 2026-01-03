from textual.widget import Widget
from textual.app import ComposeResult
from textual.containers import Vertical, Center
from textual.widgets import Button
from textual import on

class SideBar(Widget):
    def compose(self) -> ComposeResult:
        with Vertical(id = "vertical"):
            with Center():
                yield Button("Add Workout", id = "add-workout", variant = "primary", classes = "sidebutton")
                yield Button("View Recent Workouts", id = "view-workout", variant = "primary", classes = "sidebutton")
                yield Button("Delete Workout", id = "delete-workout", variant = "primary", classes = "sidebutton")
                yield Button("Visualize Workout", id = "visualize", variant = "primary", classes = "sidebutton")
    @on(Button.Pressed, "#add-workout")
    def Pressed_Add(self) -> None:
    #TODO: Add function for navigation to add_workout screen
    @on(Button.Pressed, "#view-workout")
    def Pressed_Add(self) -> None:
    #TODO: Add function for navigation to view_workout screen
    @on(Button.Pressed, "#delete-workout")
    def Pressed_Add(self) -> None:
    #TODO: Add function for navigation to delete_workout screen
    @on(Button.Pressed, "#visualized")
    def Pressed_Add(self) -> None:
    #TODO: Add function for navigation to visualize screen
