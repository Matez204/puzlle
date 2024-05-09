import pygame 
class Cudrado:
    def __init__(self,x,y,color,cont,num):
        self.x = x
        self.y = y 
        self.color = color
        self.ta = (120,120)
        self.contenedor = cont 
        self.num= num
        self.fue=pygame.font.Font(None,50) 
        self.tex=self.fue.render(str(self.num),True,(0,0,0))
        self.tec_rec=self.tex.get_rect()
    def dib(self):
        self.tec_rec.x,self.tec_rec.y=self.x+90,self.y+80
        
        pygame.draw.rect(self.contenedor,self.color,((self.x,self.y),self.ta),border_radius=15)
        if self.num == 9:
            pass
        else:
            self.contenedor.blit(self.tex,self.tec_rec)
            
possiciones=[[150,150],[285,150],[420,150],
             [150,285],[285,285],[420,285],
             [150,420],[285,420],[420,420]]