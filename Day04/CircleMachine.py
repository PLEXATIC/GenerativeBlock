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
        pg.draw.circle(screen, (255, 255, 255), self.get_center_position().astype(int), self.radius, 1)
        pg.draw.circle(screen, (255, 255, 255), self.get_swinger_position().astype(int), 3, 0)
        for child in self.children:
            pg.draw.line(screen, (255, 255, 255), self.get_swinger_position().astype(int), child.get_swinger_position().astype(int), 1)
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
    def __init__(self, parent, radius, speed, angle, children=[]):
        self.parent = parent
        self.radius = radius
        self.speed = speed
        self.angle = angle
        self.children = children

    def get_center_position(self):
        return self.parent.get_swinger_position() + self.parent.radius * np.array([math.cos(self.parent.angle), math.sin(self.parent.angle)])
    
    def get_swinger_position(self):
        return self.get_center_position() + self.radius * np.array([math.cos(self.angle), math.sin(self.angle)])

class CircleMachineVisualization(Visualization):
    def __init__(self):
        super().__init__()
        baseCircle = FixedCircle(pos=np.array([self.resolution[0] / 2, self.resolution[1] / 2]),
            radius=100,
            speed=np.pi*0.1,
            angle=0
            )
        
        some_child = MovingCircle(parent=baseCircle, angle=np.pi, radius=110, speed=np.pi*0.2)
        childOfChild = MovingCircle(parent=some_child, angle=np.pi, radius=80, speed=np.pi*0.3)
        some_child.children.append(childOfChild)
        baseCircle.children.append(some_child)

        self.circles = [baseCircle]

    def update(self):
        self.circles[0].update(1/self.fps)
        self.screen.fill((0, 0, 0))
        for circle in self.circles:
            circle.draw(self.screen)
        
    

if __name__ == "__main__":
    vis = CircleMachineVisualization()
    vis.run()