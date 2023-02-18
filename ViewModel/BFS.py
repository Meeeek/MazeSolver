from ViewModel.AlgoBase import AlgoBase
from Model.Maze import Maze
from queue import Queue

class BFS(AlgoBase):

    def __init__(self, maze: Maze, cp=(0,0)):
        super().__init__(maze, cp)
        # initialize queue
        self.q = Queue()
        self.q.put((maze.get(cp), [cp]))
        self.total_steps = 0
        self.maze = maze

    def change_cp(self, cp):
        ele, path = self.q.get()
        ele.status = 0
        self.q = Queue()
        o = self.maze.get(cp)
        self.q.put((o, [cp]))
        o.status = 1

    def step(self) -> bool:
        ele, path = self.q.get()
        self.total_steps += 1
        if not ele: 
            return True

        # get and append neighbors
        for o in [ele.left, ele.right, ele.up, ele.down]:
            if o and o.status == 0:
                self.q.put((o, path + [o.cp]))
                o.status = 1
            elif o and o.status == 4:
                print(f'Total steps: {self.total_steps}')
                print(f'Minimum path: {len(path)}')
                print(f'Path: {path}')
                for p in path:
                    self.maze.get(p).status = 5
                return True # found target
        
        ele.status = 2

        return False
