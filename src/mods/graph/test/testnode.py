# src/mods/graph/test/test_node.py

from ....mods import *
from ...utils import *

from . import TestState, MainTestNODE

@dataclass
class TestNODE(BaseNode[TestState]): # EXAMPLE NODE
    async def run(self, ctx: GraphRunContext[TestState]
                  ) -> MainTestNODE: # SHOW THE POSSIBLE NODES TO RETURN
                  # USE `Union[End, NodeName]` FOR MULTIPLE NODES
        printR("\nHello, from `TestNODE`! Returning to `MainTestNODE`...", speed=0.01)
        return MainTestNODE()
