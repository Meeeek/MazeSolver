from ViewModel.AlgoBase import AlgoBase
from Model.Maze import Maze
from queue import Queue

class BFS(AlgoBase):

    def __init__(self, maze: Maze, cp=(0,0)):
        super().__init__(maze, cp)
        # initialize queue
        self.q = Queue()
        self.q.put(maze.get(cp))

    def step(self) -> bool:
        print(f'At {self.cp}')
        ele = self.q.get()
        if ele: 
            print(f'Element {ele.cp}')
        else:
            return True

        # get and append neighbors
        for o in [ele.left, ele.right, ele.up, ele.down]:
            if o and o.status == 0:
                self.q.put(o)
                o.status = 1
            elif o and o.status == 4:
                return True # found target
        
        if ele: ele.status = 2

        return False
