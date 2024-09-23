import pygame
import math
import random

class Triangle:
    def __init__(self, hypotenuse, screen):
        self.hypotenuse = hypotenuse
        self.screen = screen
        self.vertices = self.create_random_triangle()
    
    def create_random_triangle(self):
        x1 = random.randint(50, 750)
        y1 = random.randint(50, 550)
        angle = random.uniform(0, 2 * math.pi)
        cateto = random.randint(10, self.hypotenuse - 1)
        
        x2 = x1 + cateto * math.cos(angle)
        y2 = y1 - cateto * math.sin(angle)
        x3 = x1 + self.hypotenuse * math.cos(angle + math.pi / 2)
        y3 = y1 - self.hypotenuse * math.sin(angle + math.pi / 2)
        
        return [(x1, y1), (x2, y2), (x3, y3)]
    
    def draw(self):
        pygame.draw.polygon(self.screen, (0, 0, 255), self.vertices)

    def get_rect(self):
        return pygame.draw.polygon(self.screen, (0, 0, 255), self.vertices).get_rect()
