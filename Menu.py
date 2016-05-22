import pygame, sys, random,glob

class Menu():
    #Declara atributos da classe
    def __init__ (self):

        self.pag = 0
        self.img = pygame.image.load('menu.jpg')
        self.start = pygame.Rect(100,200,190,60)
        self.upgrade = pygame.Rect(100, 400, 190, 60)
        self.fonte = pygame.font.Font("Eastwood.ttf", 40)

        # desenhar jogador
    def desenha(self,display):
        ##self.col = pygame.Rect(self.x, self.y, 60, 60)

        #display.blit(pygame.transform.rotate(self.img, self.velPulo/2), (self.x, self.y))
        display.blit(self.img, (-200,0))
        pygame.draw.rect(display, (0, 255, 0), self.start)
        pygame.draw.rect(display, (0, 255, 0), self.upgrade)