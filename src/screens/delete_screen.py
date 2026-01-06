from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Footer
from textual.binding import Binding
from textual.containers import Vertical, Horizontal

from widgets.side_bar import SideBar
# from widgets.app_header import AppHeader
from widgets.delete_workout import DeleteWorkout

class DeleteScreen(Screen[None]):
    BINDINGS = [
    ]
    def __init__(self, add, view, delete, visual):
        super().__init__()
        self.add = add
        self.view = view
        self.delete = delete
        self.visual = visual
    def compose(self) -> ComposeResult:
        # yield AppHeader()
        with Horizontal():
            yield SideBar(add = self.add, view = self.view, delete = self.delete, visual = self.visual)
            yield DeleteWorkout()
