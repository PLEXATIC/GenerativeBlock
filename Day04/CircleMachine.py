import pygame as pg
import numpy as np
import math
import random
import sys
sys.path.append("../lib")
from Visualization import Visualization

class BaseCircle:
    def update(self, t):
        self.angle += self.speed * t
        for child in self.children:
            if child != self:
                child.update(t)

    def draw(self, screen):
        pg.draw.circle(screen, (125, 125, 125), self.get_center_position().astype(int), self.radius, 1)
        pg.draw.circle(screen, (255, 255, 255), self.get_swinger_position().astype(int), 3, 1)
        for child in self.children:
            pg.draw.line(screen, (255, 255, 255), self.get_swinger_position().astype(int), child.get_center_position().astype(int), 1)
            child.draw(screen)

class FixedCircle(BaseCircle):
    def __init__(self, pos, radius, speed, angle, children=[]):
        self.pos = pos
        self.radius = radius
        self.speed = speed
        self.angle = angle
        self.children = children
    

    def get_center_position(self):
        return self.pos
    

    def get_swinger_position(self):
        return self.get_center_position() + self.radius * np.array([math.cos(self.angle), math.sin(self.angle)])
    

class MovingCircle(BaseCircle):
    def __init__(self, parent, radius, speed, angle, children=None):
        self.parent = parent
        self.radius = radius
        self.speed = speed
        self.angle = angle
        if children:
            self.children = children
        else:
            self.children = []

    def get_center_position(self):
        return self.parent.get_swinger_position()
    
    def get_swinger_position(self):
        parent_rot = 0
        if self.parent:
            parent_rot = self.parent.angle
        return self.get_center_position() + self.radius * np.array([math.cos(self.angle+parent_rot), math.sin(self.angle+parent_rot)])

class CircleMachineVisualization(Visualization):
    def __init__(self):
        super().__init__()
        baseCircle = FixedCircle(pos=np.array([self.resolution[0] / 2, self.resolution[1] / 2]), radius=60, speed=np.pi*2.8, angle=0)
        
        some_child = MovingCircle(parent=baseCircle, angle=0, radius=60, speed=np.pi*2.8)
        some_child.children.clear()
        baseCircle.children.append(some_child)
        self.circles = [baseCircle]

        another_child = MovingCircle(parent=some_child, angle=0, radius=60, speed=np.pi*1)
        some_child.children.append(another_child)

        yet_another_child = MovingCircle(parent=another_child, angle=0, radius=60, speed=np.pi*2.8)
        another_child.children.append(yet_another_child)


        


        self.track = []
        self.fps = 60
        self.debug = True

    def update(self):
        if pg.key.get_pressed()[pg.K_d]:
            self.debug = not self.debug

        self.circles[0].update(1/self.fps * 0.1)
        self.screen.fill((0, 0, 0))
        
        for circle in self.circles:
            if self.debug:
                circle.draw(self.screen)

        self.track.append(self.circles[0].children[0].children[0].children[0].get_swinger_position())
        if len(self.track) > 3:
            pg.draw.lines(self.screen, (255, 255, 255), False, self.track, 1)
        
    

if __name__ == "__main__":
    vis = CircleMachineVisualization()
    vis.run()