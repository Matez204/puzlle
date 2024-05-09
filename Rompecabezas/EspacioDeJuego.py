import pygame
from cuadrado import *
from pygame.locals import *
import sys
import random
class EspacioDeJuego:
    def __init__(self ,x,y,color,cont):
        self.x=x
        self.y=y 
        self.color = color
        self.contenedor = cont 
        self.cuadrados=[]
        self.nlist=[1,2,3,4,5,6,7,8,9]
    def inicio(self):
        random.shuffle(self.nlist)
        if len(self.cuadrados) <=8:
            for i in range(3):
                self.cuadrados.append(Cudrado(self.x+(135*i),self.y,self.color,self.contenedor,self.nlist[0]))
                self.nlist.pop(0)
            for i in range(3):
                self.cuadrados.append(Cudrado(self.x+(135*i),self.y+135,self.color,self.contenedor,self.nlist[0]))
                self.nlist.pop(0)
            for i in range(3):
                self.cuadrados.append(Cudrado(self.x+(135*i),self.y+270,self.color,self.contenedor,self.nlist[0]))
                self.nlist.pop(0)
        for i in self.cuadrados:
            if i.num == 9:
                i.color = (0,255,255)
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
        for i in self.cuadrados:
            if i.num == 9:
                h = i
        for event in pygame.event.get():    
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        c=0
                        for i in self.cuadrados:
                            if h.x - i.x == -135 and h.y == i.y and c==0:
                                c+=1
                                h.x +=135
                                i.x -=135
                    elif event.key == pygame.K_RIGHT:
                        c=0
                        for i in self.cuadrados:
                            if h.x - i.x == 135 and h.y == i.y and c==0:
                                c+=1
                                h.x -=135
                                i.x +=135
                    elif event.key == pygame.K_UP:
                        c=0
                        for i in self.cuadrados:
                            if h.y - i.y == -135 and h.x == i.x and c==0:
                                c+=1
                                h.y +=135
                                i.y -=135
                    elif event.key == pygame.K_DOWN:
                        c=0
                        for i in self.cuadrados:
                            if h.y - i.y == 135 and h.x == i.x and c==0:
                                c+=1
                                h.y -=135
                                i.y +=135
    def win(self,a,b):
        cont=[0,0,0,0,0,0,0,0,0]
        for i in self.cuadrados:
            for ind,j in enumerate(possiciones):
                if i.num == ind+1:
                    xy=[i.x,i.y]
                    if xy == j:
                        print("posicion ",ind+1," bien")
                        cont[ind]=1
        c=0
        for i in cont:
            c+=i
        print(c)
        if c==9:

            fuente_grande = pygame.font.Font(None, 72)
            texto_superficie = fuente_grande.render("Ganaste", True, (0,255,255))
            texto_rect = texto_superficie.get_rect()
            texto_rect.center = (a // 2, b // 2)
            self.contenedor.blit(texto_superficie, texto_rect)

                    
        
            
            # if i.num == 2:
            #     xy=(i.x,i.y)
            #     if xy == possiciones[1]:
            #         print("Dos si ")
            #         cont[1]=1
            # if i.num == 3:
            #     xy=(i.x,i.y)
            #     if xy == possiciones[0]:
            #         print("Uno si ")
            #         cont[0]=1
        
                
                
            

            
        
                    
                    
                

# c=EspacioDeJuego(2,59,8)
# print(c.ta)
        