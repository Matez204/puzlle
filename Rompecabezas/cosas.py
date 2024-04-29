import pygame 
from pygame.locals import *
import sys 
pygame.init()

wight=500
height=500
sr=(wight,height)
screen = pygame.display.set_mode(sr)
pygame.display.set_caption("Rompecabezas")
Blanco=(255,255,255) 
pos=[20,20]
ta=(50,50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                pos[0]+=50
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen,Blanco,(pos,ta),border_radius=15)
    
    pygame.display.flip()