import pygame, sys, random,glob

class Upgrade():
    #Declara atributos da classe
    def __init__ (self):


        self.img = pygame.image.load('UpgradeMenu.png')
        self.menu = pygame.Rect(150,500,90,90)
        self.vidaBtn = pygame.Rect(40, 40, 90, 90)
        self.fonte = pygame.font.Font("Eastwood.ttf", 40)

        # desenhar jogador
    def desenha(self,display):
        ##self.col = pygame.Rect(self.x, self.y, 60, 60)

        #display.blit(pygame.transform.rotate(self.img, self.velPulo/2), (self.x, self.y))
        display.blit(self.img, (0,0))
        pygame.draw.rect(display, (0, 255, 0), self.menu)
        pygame.draw.rect(display, (0, 255, 0), self.vidaBtn)
