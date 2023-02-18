import pygame
from ViewModel import BFS
from Model.Maze import Maze
from pygame import Rect, draw
from pygame import MOUSEBUTTONDOWN, KEYDOWN

class View():

    blockw = 16

    def __init__(self, maze: Maze):
        self.maze = maze
        pygame.init()
        self.size = maze.x * self.blockw, maze.y * self.blockw # (width, height)
        self.screen = pygame.display.set_mode(self.size)
        self.rects = [[] for _ in range(self.maze.x)]
        # init rects
        for i in range(self.maze.y):
            for j in range(self.maze.x):
                # this iterates block
                bl = self.maze.get(cp=(j, i))
                self.rects[j].append(Rect((j*self.blockw, i*self.blockw), (self.blockw, self.blockw)))

    def render(self):
        self.screen.fill((0,0,0))
        for i in range(self.maze.y):
            for j in range(self.maze.x):
                r = self.rects[j][i]
                bl = self.maze.get(cp=(j,i))
                draw.rect(self.screen, bl.get_color(), r)
        pygame.display.flip()

    def check_event(self) -> bool:
        for event in pygame.event.get():
            print(event)
            print(event.type)
            if (event.type == MOUSEBUTTONDOWN):
                for i in range(self.maze.y):
                    for j in range(self.maze.x):
                        bl = self.maze.get(cp=(j, i))
                        if self.rects[j][i].collidepoint(event.pos):
                            bl.status = 3
            elif (event.type == KEYDOWN):
                return True
        return False
        


