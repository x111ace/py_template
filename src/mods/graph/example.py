# src/mods/graph/app.py

from ...mods import *
from ..utils import *

from . import AppState, MainMenu

@dataclass
class ExampleNode(BaseNode[AppState]): # EXAMPLE NODE
    async def run(self, ctx: GraphRunContext[AppState]
                  ) -> MainMenu: # SHOW THE POSSIBLE NODES TO RETURN
                  # USE `Union[End, NodeName]` FOR MULTIPLE NODES
        printR("\nHello, from `ExampleNode`! Returning to `MainMenu`...", speed=0.01)
        return MainMenu()
