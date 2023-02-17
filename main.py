from Model.Maze import Maze
from ViewModel.BFS import BFS
from View.Viewer import View

# init phases
#  model -> viewModel -> viewer
m = Maze()

alg = BFS(m)

v = View(m)

alg.step()
while(True):
    v.render()
    if alg.step():
        break