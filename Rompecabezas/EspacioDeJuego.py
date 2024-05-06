import pygame
from cuadrado import *
from pygame.locals import *
import sys
class EspacioDeJuego:
    def __init__(self ,x,y,color,cont):
        self.x=x
        self.y=y 
        self.color = color
        self.contenedor = cont 
        self.cuadrados=[]
    def inicio(self):
        if len(self.cuadrados) <=8:
            for i in range(3):
                self.cuadrados.append(Cudrado(self.x+(135*i),self.y,self.color,self.contenedor))
            for i in range(3):
                self.cuadrados.append(Cudrado(self.x+(135*i),self.y+135,self.color,self.contenedor))
            for i in range(2):
                self.cuadrados.append(Cudrado(self.x+(135*i),self.y+270,self.color,self.contenedor))
            self.cuadrados.append(Cudrado(self.x+(135*2),self.y+270,(0,0,255),self.contenedor))
    def dib_all(self):
        for i in self.cuadrados:
            i.dib()
    def move(self):
        for event in pygame.event.get():   
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                for i in self.cuadrados:
                    if event.key == pygame.K_RIGHT:
                            i.x+=50
                    elif event.key == pygame.K_LEFT:
                            i.x-=50 
                            # h.x+=50
                    elif event.key == pygame.K_DOWN:
                            i.y+=50
                    elif event.key == pygame.K_UP:
                            i.y-=50 
    def movicion(self):
        h= self.cuadrados[8]
        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        c=0
                        for i in self.cuadrados:
                            if h.x - i.x == -135 and h.y == i.y and c==0:
                                c+=1
                                h.x +=135
                                i.x -=135
                    elif event.key == pygame.K_LEFT:
                        c=0
                        for i in self.cuadrados:
                            if h.x - i.x == 135 and h.y == i.y and c==0:
                                c+=1
                                h.x -=135
                                i.x +=135
                    elif event.key == pygame.K_DOWN:
                        c=0
                        for i in self.cuadrados:
                            if h.y - i.y == -135 and h.x == i.x and c==0:
                                c+=1
                                h.y +=135
                                i.y -=135
                    elif event.key == pygame.K_UP:
                        c=0
                        for i in self.cuadrados:
                            if h.y - i.y == 135 and h.x == i.x and c==0:
                                h.y -=135
                                i.y +=135

            
        
                    
                    
                

# c=EspacioDeJuego(2,59,8)
# print(c.ta)
        