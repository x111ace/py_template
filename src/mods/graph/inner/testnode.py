# src/mods/graph/test/test_node.py

from ....mods import *
from ...utils import *

from . import InnerState, MainNODE

@dataclass
class TestNODE(BaseNode[InnerState]): # EXAMPLE NODE
    async def run(self, ctx: GraphRunContext[InnerState]
                  ) -> MainNODE: # SHOW THE POSSIBLE NODES TO RETURN
                  # USE `Union[End, NodeName]` FOR MULTIPLE NODES
        printR("\nHello, from `TestNODE`! Returning to `MainNODE`...", speed=0.01)
        return MainNODE()
