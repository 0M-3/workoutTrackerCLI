from textual.widget import Widget
from textual.widgets import Label
from textual.app import ComposeResult
from textual.containers import Center

class Welcome(Widget):
    MESSAGE = """
     _       __           __               __ 
    | |     / /___  _____/ /______  __  __/ /_
    | | /| / / __ \/ ___/ //_/ __ \/ / / / __/
    | |/ |/ / /_/ / /  / ,< / /_/ / /_/ / /_  
    |__/|__/\____/_/  /_/|_|\____/\__,_/\__/  
          ______                __            
         /_  __/________ ______/ /_____  _____
          / / / ___/ __ `/ ___/ //_/ _ \/ ___/
         / / / /  / /_/ / /__/ ,< /  __/ /    
        /_/ /_/   \__,_/\___/_/|_|\___/_/                                                                                                              
               ________    ____
              / ____/ /   /  _/
             / /   / /    / /  
            / /___/ /____/ /   
            \____/_____/___/   
    """
    COMMENT = "To get started please select on of the options from the left side bar to get started with recording your workout journey!"

    BORDER_TITLE = "Welcome to Workout Tracker CLI!"
    def compose(self) -> ComposeResult:
        with Center():
            yield Label(self.MESSAGE)
            # yield Label(self.COMMENT)
        
