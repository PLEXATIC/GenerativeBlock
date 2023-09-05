import pygame as pg
import sys
import numpy as np

sys.path.append("../lib")
from Visualization import Visualization

CIRCLE_SEGMENT_COUNT = 100

class WiggelyCircle():
    def __init__(self, x, y, radius=10, color=(255, 255, 255), rotation_speed=0, wiggle_amplitude=3, wiggle_frequency=30):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.wiggle_speed = rotation_speed
        self.wiggle_amplitude = wiggle_amplitude
        self.time = 0
        self.wiggle_frequency = wiggle_frequency
        self.activation = 0

    def update(self):
        self.time += 0.01

    def draw(self, screen):
        global CIRCLE_SEGMENT_COUNT
        line_segments = []
        
        for i in range(CIRCLE_SEGMENT_COUNT):
            percentage = i/(CIRCLE_SEGMENT_COUNT-1)
            distortion = np.sin(self.time*self.wiggle_speed*2*np.pi + percentage*2*np.pi*self.wiggle_frequency)*self.wiggle_amplitude
            relative_radius = self.radius + self.activation * distortion
            angle = percentage*2*np.pi
            x = self.x + np.cos(angle)*relative_radius
            y = self.y + np.sin(angle)*relative_radius
            line_segments.append((x, y))
        pg.draw.lines(screen, self.color, False, line_segments, 1)


class ShootingCirclesVisualization(Visualization):
    def __init__(self):
        super().__init__()
        self.time = 0
        self.circles = []
        count_x, count_y = 16, 9
        for ix in range(count_x):
            for iy in range(count_y):
                x = ix*self.resolution[0]/count_x + self.resolution[0]/(count_x*2)
                y = iy*self.resolution[1]/count_y + self.resolution[1]/(count_y*2)
                self.circles.append(WiggelyCircle(x, y, radius=50, color=(255, 255, 255), rotation_speed=0.1, wiggle_amplitude=3 + np.random.random()*20, wiggle_frequency=0 + (np.random.random()*20 -10)**2))

    def update(self):
        
        # Fill with 0.01 alpha, so that the circles leave a trail
        fill_surf = pg.Surface(self.resolution)
        fill_surf.set_alpha(50)
        fill_surf.fill((0,0,0))
        self.screen.blit(fill_surf, (0,0))
        
        for circle in self.circles:
            if np.random.random() > 0.995:
                circle.activation = 1
            circle.activation *= 0.95
            circle.wiggle_frequency += 0.05* (np.sin(self.time*2))
            circle.wiggle_amplitude += 0.05* (np.cos(self.time*2))
            circle.update()
            circle.draw(self.screen)
        self.time += 0.01

def main():
    visualization = ShootingCirclesVisualization()
    visualization.run()

if __name__ == "__main__":
    main()