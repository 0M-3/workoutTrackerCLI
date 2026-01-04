#FIX: Test the view workout screen
from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Footer
from textual.binding import Binding
from textual.containers import Vertical, Horizontal


class VisualizeScreen(Screen[None]):
    BINDINGS = [
    ]
    def compose(self) -> ComposeResult:
        yield AppHeader()
        with Horizontal():
            yield SideBar()
            yield VisualizeWorkout()
