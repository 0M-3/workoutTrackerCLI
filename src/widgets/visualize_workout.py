from textual.widget import Widget
from textual.widgets import Select, Input, Button
from textual.app import ComposeResult
from textual.containers import Horizontal
from textual import on
from textual.reactive import reactive

from database import get_workouts

class VisualizeWorkout(Widget):
    workouts = get_workouts()
    workouts.append("All")
    def compose(self) -> ComposeResult:
        with Horizontal(classes = "widget-container"):
            yield Select.from_values(self.workouts, id = "select-visualize")
            yield Button("Generate",variant = "primary", id = "visualize-button")

    @on(Button.Pressed, "#visualize-button")
    def Pressed_view(self):
        pass
        #TODO: Complete the view function
