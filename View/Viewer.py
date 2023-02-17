import pygame
from ViewModel import BFS
from Model.Maze import Maze

class View():

    def __init__(self, maze: Maze):
        self.maze = maze

    def render(self):
        for i in range(self.maze.y):
            for j in range(self.maze.x):
                print(self.maze.get((j,i)).status, end="")
            print("\n", end="")
            print("_" * 50)

