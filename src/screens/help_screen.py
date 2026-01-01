from textual.screen import ModalScreen
from textual.widgets import Footer, Markdown
from textual.app import ComposeResult
from textual.binding import Binding
from textual.containers import Vertical, VerticalScroll

class HelpScreen(ModalScreen[None]):
    BINDINGS = [
        Binding("q", "app.quit", "Quit", show = False),
        Binding("escapse,f1,?", "app.pop_screen()", "Close help", key_display="esc")
    ]

    HELP_MARKDOWN = """
    ### How do I quit WorkoutTrackerCLI?

    Press `Ctrl+C` on your keyboard.
    `q` also works if an input isn't being focused.
    If focus is on the prompt input box on the home screen, `esc` will close WorkoutTrackerCLI too.

    ### General navigation

    Elia has very strong mouse support. Most things can be clicked.

    Use `tab` and `shift+tab` to move between different widgets on screen.

    In some places you can make use of the arrow keys or Vim nav keys to move around.

    In general, pressing `esc` will move you "closer to home".
    Pay attention to the bar at the bottom to see where `esc` will take you.

    If you can see a scrollbar, `pageup`, `pagedown`, `home`, and `end` can also
    be used to navigate.

    On the chat screen, pressing `up` and `down` will navigate through messages,
    but if you just wish to scroll a little, you can use `shift+up` and `shift+down`.

    """

    def compose(self) -> ComposeResult:
        with Vertical(id = "help-container") as vertical:
            vertical.border_title = "WorkoutTrackerCLI Help"
            with VerticalScroll():
                yield Markdown(self.HELP_MARKDOWN, id = "help-markdown")
            yield Markdown(
                """Use `pageup`, `pagedown`, `up`, and `down` to scroll.""",
                id = "help-scroll-keys-info"
            )
            yield Footer()
