from textual.app import App, ComposeResult 
from textual.screen import Screen
from textual.widgets import Header, Footer, Button, ContentSwitcher
from textual.widget import Widget
from textual.containers import Vertical, Horizontal, Center
from textual.binding import Binding
from textual import on

from screens.help_screen import HelpScreen
from screens.home_screen import HomeScreen
from screens.add_screen import AddScreen
from screens.delete_screen import DeleteScreen
from screens.view_screen import ViewScreen
from screens.visualize_screen import VisualizeScreen

from widgets.side_bar import SideBar
from widgets.app_header import AppHeader
from widgets.delete_workout import DeleteWorkout
from widgets.view_workout import ViewWorkout
from widgets.visualize_workout import VisualizeWorkout

from database import init_db

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
        init_db()
        self.push_screen(HomeScreen(add = AddScreen, delete = DeleteScreen, view = ViewScreen, visual = VisualizeScreen))

    @on(Button.Pressed, "#add-workout")
    def Pressed_Add(self) -> None:
        self.push_screen(AddScreen(add = AddScreen, delete = DeleteScreen, view = ViewScreen, visual = VisualizeScreen))

    @on(Button.Pressed, "#view-workout")
    def Pressed_View(self) -> None:
        self.push_screen(ViewScreen(add = AddScreen, delete = DeleteScreen, view = ViewScreen, visual = VisualizeScreen))

    @on(Button.Pressed, "#delete-workout")
    def Pressed_Delete(self) -> None:
        self.push_screen(DeleteScreen(add = AddScreen, delete = DeleteScreen, view = ViewScreen, visual = VisualizeScreen))

    @on(Button.Pressed, "#visualized")
    def Pressed_Visualize(self) -> None:
        self.push_screen(VisualizeScreen(add = AddScreen, delete = DeleteScreen, view = ViewScreen, visual = VisualizeScreen))


if __name__ == "__main__":
    app = LayoutApp()
    app.run()
