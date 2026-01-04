#TODO: Create the delete workout widget
from textual.widget import Widget
from textual.widgets import Select, Input, Button
from textual.app import ComposeResult
from textual.containers import Horizontal
from textual import on
from textual.reactive import reactive

class ViewWorkout(Widget):
    def compose(self) -> ComposeResult:
        with Horizontal():
            yield Select()
            yield Button("Delete",variant = "primary", id = "delete-button")

    @on(Button.Pressed, "#delete-button")
    def Pressed_delete(self):
        pass
        #TODO: Complete the view function
