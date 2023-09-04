import pygame as pg
import sys
sys.path.append("../lib")
from Visualization import Visualization

class BasicDrawings(Visualization):
    def update(self):
        self.screen.fill((0, 0, 0))
        pg.draw.line(self.screen, (255, 255, 255), (0, 0), (100, 100))

def main():
    visualization = BasicDrawings()
    visualization.run()

if __name__ == "__main__":
    main()