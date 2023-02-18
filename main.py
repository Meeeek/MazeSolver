from Model.Maze import Maze
from ViewModel.BFS import BFS
from ViewModel.DFS import DFS
from View.Viewer import View
import time

# init phases
#  model -> viewModel -> viewer
m = Maze()

alg = BFS(m)

v = View(m)

alg.step()

phase = 0
# 0: drawing
# 1: running
# 2: finished

while(phase < 2):
    v.render()
    
    if phase == 0:
        if v.check_event():
            phase = 1
    elif phase == 1:
        time.sleep(0.05)
        if alg.step():
            phase = 2

while phase == 2:
    pass