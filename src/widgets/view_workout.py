from textual.widget import Widget
from textual.widgets import Select, Input, Button, DataTable
from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual import on
from textual.reactive import reactive

from database import get_dates, view_workouts

class ViewWorkout(Widget):
    dates= get_dates()
    def compose(self) -> ComposeResult:
        with Vertical(classes = "widget-container"):
            with Horizontal():
                yield Select.from_values(self.dates, id = "view-select")
                yield Button("Query",variant = "primary", id = "view-button")
            yield DataTable(id = "view-table")

    @on(Button.Pressed, "#view-button")
    def Pressed_view(self):
        table = self.query_one("#view-table", DataTable)
        view_date = self.query_one("#view-select", Select)
        if view_date.value == Select.BLANK:
            data = view_workouts()
        else:
            data = view_workouts(view_date.value)
        table.clear(columns = True)
        table.focus()
        table.add_columns("Date", "Exercise", "Sets Performed", "Maximum Reps", "Minimum Reps", "Max Weight", "Min Weight")
        for row in data:
            table.add_row(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
        table.cursor_type = "row"
        table.zebra_stripes = True

