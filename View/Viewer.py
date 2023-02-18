import pygame
from Model.Maze import Maze
from pygame import Rect, draw
from pygame import MOUSEBUTTONDOWN, KEYDOWN, MOUSEMOTION, MOUSEBUTTONUP
from pygame import mouse
from ViewModel.AlgoBase import AlgoBase

class View():

    blockw = 16
    isMousePressed = False

    def __init__(self, maze: Maze, alg: AlgoBase):
        self.alg = alg
        self.maze = maze
        self.size = maze.x * self.blockw, maze.y * self.blockw # (width, height)
        self.screen = pygame.display.set_mode(self.size)
        self.rects = [[] for _ in range(self.maze.x)]
        # init rects
        for i in range(self.maze.y):
            for j in range(self.maze.x):
                # this iterates block
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
        mp = mouse.get_pos()

        for event in pygame.event.get():
            if(self.isMousePressed and event.type == MOUSEMOTION):
                self._collide_draw(3, mp)
            elif (event.type == MOUSEBUTTONDOWN):
                self.isMousePressed = True
                self._collide_draw(3, mp)
            elif (event.type == MOUSEBUTTONUP):
                self.isMousePressed = False                
            elif (event.type == KEYDOWN):
                if event.key == 13:
                    return True
                elif event.key == 101:
                    self._collide_draw(4, mp)
                elif event.key == 115:
                    self.alg.change_cp((mp[0] // self.blockw, mp[1] // self.blockw))
                
        return False
        
    def _collide_draw(self, stat, mp):
        for i in range(self.maze.y):
            for j in range(self.maze.x):
                bl = self.maze.get(cp=(j, i))
                if self.rects[j][i].collidepoint(mp):
                    bl.status = stat

