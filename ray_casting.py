import pygame
import numpy
from Limits import *
from particle import *

width = 800
height = 800
size = (width, height)

class Display:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        
        #Random walls
        self.walls = []
        for i in range(5):
            
            x1 = numpy.random.randint(0, width)
            y1 = numpy.random.randint(0, height)
            
            x2 = numpy.random.randint(0, width)
            y2 = numpy.random.randint(0, height)
            
            x3 = numpy.random.randint(0, width)
            y3 = numpy.random.randint(0, height)
            
            self.walls.append(Limits(x1, y1, x2, y2))
        
        self.walls.append(Limits(0, 0, width, 0))
        self.walls.append(Limits(0, 0, 0, height))
        self.walls.append(Limits(0, height, width, height))
        self.walls.append(Limits(width, 0, width, height))
        self.particle = Particle()
        
        self.stop = False
        self.clock = pygame.time.Clock()
        
    def Draw(self):
        for wall in self.walls:
            wall.display(self.screen)
        self.particle.display(self.screen)
        
    def run(self):
        while not self.stop:
            self.screen.fill((0,0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stop = True
                    
                    #get the mouse position
                    if event.type == pygame.MOUSEMOTION:
                        pos = event.pos
                        self.particle.pos[0] = pos[0]
                        self.particle.pos[1] = pos[1]
                    
            self.particle.look(self.screen, self.walls)
            self.Draw()
            self.clock.tick(100)
            pygame.display.update()
            
            
if __name__ == '__main__':
    a = Display()
    a.run()
                        
                        