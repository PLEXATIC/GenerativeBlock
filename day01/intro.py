import pygame as pg
import sys
import numpy as np
sys.path.append("../lib")
from Visualization import Visualization

class BasicDrawings(Visualization):

    def __init__(self):
        super().__init__()
        self.time = 0

    def update(self):
        self.screen.fill((0, 0, 0))
        self.time += 0.01
        base_width = 20
        
        # Find middle bottom
        middle_bottom = (self.resolution[0] // 2, self.resolution[1])

        # Draw a thick line straight up. It will be the trunk of the tree
        branching_origin = (middle_bottom[0], middle_bottom[1] - self.resolution[1]//2)
        
        # Draw 3 levels of branches, that each split up into 5 branches.
        start_points = [
            branching_origin,
        ]

        n_branches = 2

        dy = -0 + (np.sin(self.time)*25)

        for level in range(10):
            dy *= 1.1
            base_width *= 0.5
            new_start_points = []
            for start_point in start_points:
                for i in range(n_branches):
                    percentage = i/(n_branches-1)

                    dx = 100*percentage - 50
                    
                    start_x, start_y = start_point
                    end_x = start_x + dx
                    end_y = start_y + dy
                    end_point = (end_x, end_y)

                    pg.draw.line(self.screen, (255, 255, 255), start_point, end_point, int(base_width)+1)
                    new_start_points.append(end_point)
            start_points = new_start_points

def main():
    visualization = BasicDrawings()
    visualization.run()

if __name__ == "__main__":
    main()