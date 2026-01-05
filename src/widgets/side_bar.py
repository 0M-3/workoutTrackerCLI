from textual.widget import Widget
from textual.app import ComposeResult
from textual.containers import Vertical, Center
from textual.widgets import Button
from textual import on

# from screens.add_screen import AddScreen
# from screen.delete_screen import DeleteScreen
# from screen.view_screen import ViewScreen
# from screen.visualize_screen import VisualizeScreen

class SideBar(Widget):
    def __init__(self, add, delete, view, visual, id = None, classes= None):
        super().__init__(id = id, classes = classes)
        self.add = add
        self.delete = delete
        self.view = view
        self.visual = visual
    def compose(self) -> ComposeResult:
        with Vertical(id = "vertical"):
            with Center():
                yield Button("Add Workout", id = "add-workout", variant = "primary", classes = "sidebutton")
                yield Button("View Recent Workouts", id = "view-workout", variant = "primary", classes = "sidebutton")
                yield Button("Delete Workout", id = "delete-workout", variant = "primary", classes = "sidebutton")
                yield Button("Visualize Workout", id = "visualize", variant = "primary", classes = "sidebutton")
