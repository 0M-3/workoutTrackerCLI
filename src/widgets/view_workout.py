from textual.widget import Widget
from textual.widgets import Select, Input, Button
from textual.app import ComposeResult
from textual.containers import Horizontal
from textual import on
from textual.reactive import reactive

from database import get_dates

class ViewWorkout(Widget):
    dates= get_dates()
    def compose(self) -> ComposeResult:
        with Horizontal(classes = "widget-container"):
            yield Select.from_values(self.dates)
            yield Button("Query",variant = "primary", id = "view-button")

    @on(Button.Pressed, "#view-button")
    def Pressed_view(self):
        pass
        #TODO: Complete the view function
