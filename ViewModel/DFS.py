from ViewModel.AlgoBase import AlgoBase
from Model.Maze import Maze

class DFS(AlgoBase):

    def __init__(self, maze: Maze, cp=(0,0)) -> None:
        super().__init__(maze, cp)
        self.stack = [] # use list as stack, end of list is the top of stack
        self.stack.append(maze.get(cp))

    def step(self) -> bool:
        if len(self.stack) == 0:
            return True
        ele = self.stack.pop() # pop the end of the list, top of stack
        
        # append neighbors
        for o in [ele.left, ele.up, ele.right, ele.down]:
            if o and o.status == 0:
                self.stack.append(o)
                o.status = 1
            elif o and o.status == 4:
                return True

        ele.status = 2
        return False
