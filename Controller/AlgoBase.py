class AlgoBase:

    def __init__(self, maze, cp=(0,0)) -> None:
        self.maze = maze
        self.cp = cp

    def step(self):
        print("Not implemented") # single step in algo

    def change_cp(self, cp):
        pass