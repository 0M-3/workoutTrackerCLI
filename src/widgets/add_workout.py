from textual.widget import Widget
from textual.widgets import Select, Input, Button
from textual.app import ComposeResult
from textual.containers import Vertical
from textual import on
from textual.reactive import reactive

from datetime import datetime 

from database import init_db, get_workouts, add_workout

class OtherInput(Input):
    show_input: reactive[str | None] = reactive(None)

    def __init__(self, id, placeholder="", classes = "widget-input"):
        super().__init__(id=id, placeholder=placeholder, classes= classes)
        self.display = False

    def watch_show_input(self, show: bool) -> None:
        """This runs whenever show_input changes."""
        self.display = bool(show)
        if show:
            self.focus()
        else:
            self.value = ""  # Clear input if hidden
            

class AddWorkout(Widget):
    init_db()
    workouts = get_workouts()
    workouts.append("other")

    def compose(self) -> ComposeResult:
        with Vertical(classes = "widget-container"):
            yield Select.from_values(self.workouts, id = "select-workout", prompt = "Select workout", classes = "widget-select")
            yield OtherInput(placeholder = "Other workout", id = "other-workout", classes = "widget-input")
            yield Input(placeholder = "Number of reps", id = "reps", type = "number", classes = "widget-input")
            yield Input(placeholder = "Weight", id = "weight", type = "number", classes = "widget-input")
            yield Button("Submit Set", variant = "success", id = "submit-workout")

    def select_opened(self):
        self.workouts = get_workouts()
        self.workouts.append("other")
            
    @on(Select.Changed, "#select-workout")
    def select_changed(self, event:Select.Changed) -> None:
        other_input = self.query_one(OtherInput)
        other_input.show_input = (event.value == "other")

    @on(Button.Pressed, "#submit-workout")
    def Pressed_Submit(self, event:Button.Pressed) -> None:
        now= datetime.now()
        select_query = self.query_one("#select-workout", Select)
        if select_query.value == "other":
            select_query = self.query_one("#other-workout", Input)
        rep_query = self.query_one("#reps", Input)
        weight_query = self.query_one("#weight", Input)
        # set_query = self.query_one("#sets", Input)
        add_workout(date = now, exercise = select_query.value, reps = int(rep_query.value), weight = int(weight_query.value))

