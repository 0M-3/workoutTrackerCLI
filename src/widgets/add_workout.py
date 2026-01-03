from textual.widget import Widget
from textual.widgets import Select, Input
from textual.app import ComposeResult
from textual.containers import Vertical
from textual import on
from textual.reactive import reactive

from datetime import datetime 

from database import get_workouts, add_workout

class OtherInput(Input):
    DEFAULT_CSS = """
    .hidden{
        display: none;
    }
    """
    text: reactive[str | None] = reactive(None)

    def __init__ == "__main__":
        super().__init__(classes = "hidden")

    def watch_option(self) -> None:
        if self.text is not None:
            self.update(self.text)
        self.set_class(self.text is None, "hidden")
            

class AddWorkout(Widget):
    self.workouts = get_workouts()

    def compose(self) -> ComposeResult:
        with Vertical():
            yield Select.from_values(self.workouts, id = "select-workout", prompt = "Select workout")
            yield OtherInput(placeholder = "Other workout", id = "other-workout")
            yield Input(placeholder = "Number of reps", id = "reps", type = "number")
            # yield Input(placeholder = "Number of sets", id = "sets", type = "number")
            yield Button("Submit Set", variant = "success", id = "submit-workout")
            
    @on(Select.Changed)
    def select_changed(self, event:Select.Changed) -> None:
        if event.value == "other":
            self.query_one(OtherInput).text = "other"
        else:
            self.query_one(OtherInput).text = None

    @on(Button.Pressed, "#submit-workout")
    def Pressed_Submit(self, event:Button.Pressed) -> None:
    #FIX:This function needs to be tested further and integrated with the database functions.
        now_utc = datetime.now()
        select_query = self.query_one("#select-workout", Select)
        if select_query.value == "other":
            select_query = self.query_one("other-workout", Input)
        rep_query = self.query_one("#reps", Input)
        # set_query = self.query_one("#sets", Input)
        add_workout(date = now_utc, exercise = select_query.value, rep = rep_query.value)

