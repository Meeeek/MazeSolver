from Model.Maze import Maze
from ViewModel.BFS import BFS
from ViewModel.DFS import DFS
from View.Viewer import View
import time
import pygame

pygame.init()

# init phases
#  model -> controller -> viewer
m = Maze()

alg = BFS(m)

v = View(m, alg)

phase = 0
# 0: drawing
# 1: running
# 2: finished
while(True):
    v.render()

    if phase == 0:
        if v.check_event():
            phase = 1
            
    elif phase == 1:
        time.sleep(0.025)
        if alg.step():
            phase = 2

    elif phase == 2:
        if v.check_event():
            m = Maze()
            alg = BFS(m)
            v = View(m, alg)
            phase = 0
