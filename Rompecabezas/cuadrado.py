import pygame 

class Cudrado:
    def __init__(self,x,y,color,cont):
        self.x = x
        self.y = y 
        self.color = color
        self.ta = (120,120)
        self.contenedor = cont 
    def dib(self):
        pygame.draw.rect(self.contenedor,self.color,((self.x,self.y),self.ta),border_radius=15)
