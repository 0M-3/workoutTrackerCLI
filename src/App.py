from textual.app import App, ComposeResult 
from textual.screen import Screen
from textual.widgets import Header, Footer, Button, ContentSwitcher
from textual.widget import Widget
from textual.containers import Vertical, Horizontal, Center
from textual.binding import Binding

from screens.help_screen import HelpScreen
from screens.home_screen import HomeScreen
from widgets.side_bar import SideBar

class LayoutApp(App):
    CSS_PATH = "app.tcss"
    BINDINGs = [
        Binding("q", "app.quit", "Quit", show=False),
        Binding("f1,?", "help", "Help"),
    ]

    async def action_help(self) -> None:
        if isinstance(self.screen, HelpScreen):
            self.pop_screen()
        else:
            await self.push_screen(HelpScreen())

    def on_ready(self) -> None:
        self.push_screen(HomeScreen())


if __name__ == "__main__":
    app = LayoutApp()
    app.run()
