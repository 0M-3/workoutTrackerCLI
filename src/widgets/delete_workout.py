from textual.widget import Widget
from textual.widgets import Select, Input, Button
from textual.app import ComposeResult
from textual.containers import Horizontal
from textual import on
from textual.reactive import reactive

from database import get_dates, delete_workout_by_date

class DeleteWorkout(Widget):
    dates = get_dates()
    def compose(self) -> ComposeResult:
        with Horizontal():
            yield Select.from_values(self.dates, id = "delete-select")
            yield Button("Delete",variant = "primary", id = "delete-button")

    @on(Button.Pressed, "#delete-button")
    def Pressed_delete(self):
        delete_date=self.query_one("#delete-select", Select)
        delete_workout_by_date(delete_date.value)
        

