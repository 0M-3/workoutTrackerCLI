from textual.widget import Widget
from textual.widgets import Select, Input, Button, DataTable
from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual import on
from textual.reactive import reactive

from database import view_workouts, delete_workout_by_date

class DeleteWorkout(Widget):
    data = view_workouts()
    def compose(self) -> ComposeResult:
        with Vertical(classes = "widget-container"):
            yield DataTable(id = "delete-table")
            with Horizontal():
                yield Button("Delete",variant = "primary", id = "delete-button")

    def on_mount(self) -> None:
        table = self.query_one("#delete-table", DataTable)
        table.clear(columns = True)
        table.focus()
        table.add_columns("Date", "Exercise", "Sets Performed", "Maximum Reps", "Minimum Reps", "Max Weight", "Min Weight")
        for row in self.data:
            table.add_row(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
        table.cursor_type = "row"
        table.zebra_stripes = True
        
    @on(Button.Pressed, "#delete-button")
    def Pressed_delete(self):
        delete_table=self.query_one("#delete-table", DataTable)
        row_data = delete_table.get_row_at(delete_table.cursor_row)
        delete_workout_by_date(row_data[0])
        self.data = view_workouts()
        delete_table.clear(columns = True)
        delete_table.add_columns("Date", "Exercise", "Sets Performed", "Maximum Reps", "Minimum Reps", "Max Weight", "Min Weight")
        for row in self.data:
            delete_table.add_row(row[0],row[1],row[2],row[3],row[4],row[5],row[6])

