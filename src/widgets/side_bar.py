from textual.widget import Widget
from textual.app import ComposeResult
from textual.containers import Vertical, Center
from textual.widgets import Button

class SideBar(Widget):
    def compose(self) -> ComposeResult:
        with Vertical(id = "vertical"):
            with Center():
                yield Button("Add Workout", id = "add-workout", variant = "primary", classes = "sidebutton")
                yield Button("View Recent Workouts", id = "view-workout", variant = "primary", classes = "sidebutton")
                yield Button("Delete Workout", id = "delete-workout", variant = "primary", classes = "sidebutton")
                yield Button("Visualize Workout", id = "visualize", variant = "primary", classes = "sidebutton")

