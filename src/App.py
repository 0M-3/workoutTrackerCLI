from textual.app import App, ComposeResult 
from textual.screen import Screen
from textual.widgets import Header, Footer, Button 
from textual.containers import VerticalGroup


class ColumnsContainer(VerticalGroup):
    DEFAULT_CSS = """
    ColumnsContainer {
        width: 1fr;
        height: 1fr;
        border: solid white;
    }
    """
    def compose(self) -> ComposeResult:
        yield Button("Button 1", id = "b1", variant="primary")
        yield Button("Button 2", id = "b2", variant="primary")
        yield Button("Button 3", id = "b3", variant="primary")
        yield Button("Button 4", id = "b4", variant="primary")


class MainScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield ColumnsContainer()
        
class LayoutApp(App):
    def on_ready(self) -> None:
        self.push_screen(MainScreen())

if __name__ == "__main__":
    app = LayoutApp()
    app.run()
