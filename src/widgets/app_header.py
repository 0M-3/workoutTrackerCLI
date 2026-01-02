from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import Label
from textual.containers import Horizontal, Vertical

from rich.text import Text

class AppHeader(Widget):
    COMPONENT_CLASSES = {"app-title", "app-subtitle"}

    def __init__(
            self,
            name: str | None = None,
            id: str | None = None,
            classes: str | None = None,
            disabled: bool = False,
    ) -> None:
        super().__init__(name=name, id=id, classes=classes, disabled=disabled)
    # def on_mount(self) -> None:
    def compose(self) -> ComposeResult:
        with Horizontal():
            with Vertical(id = "cl-header-container"):
                yield Label(Text("Workout Tracker CLI")+Text("vAlpha", style = "dim"), id = "wt-title")


