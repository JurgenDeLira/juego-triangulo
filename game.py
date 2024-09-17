import pygame
import random
from triangle import Triangle

class Game:
    def __init__(self):
        pygame.init()
        self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Juego de Triángulos")
        self.clock = pygame.time.Clock()
        self.triangles = []
        self.running = True
    
    def check_overlap(self, new_triangle):
        for triangle in self.triangles:
            if pygame.draw.polygon(self.screen, (0, 0, 255), triangle.vertices).colliderect(
               pygame.draw.polygon(self.screen, (0, 0, 255), new_triangle.vertices).get_rect()):
                return True
        return False

    def run(self):
        while self.running:
            self.screen.fill((255, 255, 255))
            
            for triangle in self.triangles:
                triangle.draw(self.screen)
            
            hypotenuse = random.randint(50, 150)
            print(f"Longitud de la hipotenusa: {hypotenuse}")
            cateto = int(input("Ingresa la longitud de uno de los catetos: "))
            
            if cateto >= hypotenuse:
                print("¡El cateto no puede ser mayor o igual a la hipotenusa!")
                continue
            
            new_triangle = Triangle(hypotenuse)
            
            if not self.check_overlap(new_triangle):
                self.triangles.append(new_triangle)
            else:
                print("¡No hay espacio para dibujar más triángulos!")
                self.running = False
            
            pygame.display.flip()
            self.clock.tick(30)
        
        pygame.quit()
