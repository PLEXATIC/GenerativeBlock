import pygame as pg

class Visualization:
    """Helper class to easily get visualizations by modifying the update method. For this, override the update method"""
    def __init__(self, resolution=(640, 480), fps=60):
        self.resolution = resolution
        self.fps = fps
        pg.init()
        self.clock = pg.time.Clock()
        self.running = True
        self.screen = pg.display.set_mode(self.resolution)

    def update(self):
        pass


    def run(self):
        while self.running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
            self.update()
            pg.display.flip()
            self.clock.tick(self.fps)

