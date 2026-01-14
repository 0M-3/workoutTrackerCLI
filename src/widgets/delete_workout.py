from textual.widget import Widget
from textual.widgets import Select, Input, Button, DataTable
from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual import on
from textual.reactive import reactive

from database import view_workouts, delete_workout

class DeleteWorkout(Widget):
    data = view_workouts()
    selected_workout_id: reactive[int | None] = reactive(None)

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
            table.add_row(row[1],row[2],row[3],row[4],row[5],row[6],row[7], key=str(row[0]))
        table.cursor_type = "row"
        table.zebra_stripes = True
    
    def on_data_table_row_selected(self, event: DataTable.RowSelected):
        self.selected_workout_id = event.row_key.value
        
    @on(Button.Pressed, "#delete-button")
    def Pressed_delete(self):
        if self.selected_workout_id is not None:
            delete_workout(self.selected_workout_id)
            
            # Refresh table
            delete_table=self.query_one("#delete-table", DataTable)
            self.data = view_workouts()
            delete_table.clear()
            for row in self.data:
                delete_table.add_row(row[1],row[2],row[3],row[4],row[5],row[6],row[7], key=str(row[0]))
            
            self.selected_workout_id = None
