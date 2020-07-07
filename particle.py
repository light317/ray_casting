import pygame
from numpy import array, deg2rad, linalg
from ray import *

class Particle:
    def __init__(self):
        self.pos = array([250, 250])
        
    def display(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.pos, 1, 1)
        
        for ray in self.rays:
            ray.display(screen)
            
    def look(self, screen, walls):
        self.rays = []
        for i in range(0, 360, 5):
            self.rays.append(Ray(self.pos[0], self.pos[1], deg2rad(i)))
            
        for ray in self.rays:
            closest = 1000000
            closest_point = None
            
            for wall in walls:
                pt = ray.cast(wall)
                
                if pt is not None:
                    dis = linalg.norm(pt - self.pos)
                    if(dis < closest):
                        closest = dis
                        closest_point = pt
                        
            if closest_point is not None:
                pygame.draw.line(screen, (255, 255, 255), self.pos, array(closest_point, int))