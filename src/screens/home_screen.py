from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Footer
from textual.binding import Binding
from textual.containers import Vertical, Horizontal

from widgets.side_bar import SideBar
from widgets.welcome import Welcome

class HomeScreen(Screen[None]):
    BINDINGS = [
    ]
    def __init__(self, add, delete, view, visual):
        super(HomeScreen, self).__init__()
        self.add = add
        self.delete = delete
        self.view = view
        self.visual = visual
    def compose(self) -> ComposeResult:
        # yield AppHeader()
        with Horizontal():
            yield SideBar(add = self.add, view = self.view, delete = self.delete, visual = self.visual)
            yield Welcome()
        
