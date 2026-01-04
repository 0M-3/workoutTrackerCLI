from textual.widget import Widget
from textual.widgets import Select, Input, Button
from textual.app import ComposeResult
from textual.containers import Horizontal
from textual import on
from textual.reactive import reactive

class VisualizeWorkout(Widget):
    def compose(self) -> ComposeResult:
        with Horizontal():
            yield Select()
            yield Button("Generate",variant = "primary", id = "visualize-button")

    @on(Button.Pressed, "#view-button")
    def Pressed_view(self):
        pass
        #TODO: Complete the view function
