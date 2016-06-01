import pygame, sys, random,glob

class Wall():
    #Declara atributos da classe
    def __init__ (self):
        self.tipo = 'wall'
        self.y = 490
        self.x = random.randint(800, 2500)
        self.velocidade = 0
        self.img = pygame.image.load('wall.png')
        self.col = pygame.Rect(self.x, self.y, 40, 60)


    def desenha(self,display,vel):
        self.x -= vel
        self.col = pygame.Rect(self.x, self.y, 40, 60)##arrumar o tamanho certo
        display.blit(self.img, (self.x, self.y))

