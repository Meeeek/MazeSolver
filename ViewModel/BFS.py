from ViewModel.AlgoBase import AlgoBase
from Model.Maze import Maze
from queue import Queue

class BFS(AlgoBase):

    def __init__(self, maze: Maze, cp=(0,0)):
        super().__init__(maze, cp)
        # initialize queue
        self.q = Queue()
        self.q.put((maze.get(cp), 0))
        self.total_steps = 0
        self.maze = maze

    def change_cp(self, cp):
        ele, path_size = self.q.get()
        ele.status = 0
        self.q = Queue()
        o = self.maze.get(cp)
        self.q.put((o, 0))
        o.status = 1

    def step(self) -> bool:
        ele, path_size = self.q.get()
        self.total_steps += 1
        if not ele: 
            return True

        # get and append neighbors
        for o in [ele.left, ele.right, ele.up, ele.down]:
            if o and o.status == 0:
                self.q.put((o, path_size + 1))
                o.status = 1
            elif o and o.status == 4:
                print(f'Total steps: {self.total_steps}')
                print(f'Minimum path: {path_size}')
                return True # found target
        
        ele.status = 2

        return False
