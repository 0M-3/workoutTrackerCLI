#FIX: Test the screen for the add workout screen
from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Footer
from textual.binding import Binding
from textual.containers import Vertical, Horizontal

from widgets.side_bar import SideBar
from widgets.app_header import AppHeader
from widgets.add_workout import AddWorkout

class AddScreen(Screen[None]):
    BINDINGS = [
    ]
    def __init__(self, add, recent, delete, visual):
        super.__init__()
        self.add = add
        self.recent = recent 
        self.delete = delete
        self.visual = visual
    def compose(self) -> ComposeResult:
        yield AppHeader()
        with Horizontal():
            yield SideBar(add = self.add, recent = self.recent, delete = self.delete, visual = self.visual)
            yield AddWorkout()
        
