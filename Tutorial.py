import pygame, sys, random,glob
from Menu import Menu
class Tutorial():
    #Declara atributos da classe
    def __init__ (self):


        self.img = [pygame.image.load('Tutorial1.jpg'),pygame.image.load('Tutorial2.jpg'),pygame.image.load('Tutorial3.jpg'),pygame.image.load('Tutorial4.jpg'),pygame.image.load('Tutorial5.jpg'),pygame.image.load('Tutorial6.jpg')]
        self.next = pygame.Rect(650,100,90,60)
        self.prev = pygame.Rect(80, 100, 90, 60)
        self.imgMenu = pygame.image.load('Back.png')
        self.controle = 0

        # desenhar jogador
    def desenha(self,display, menu):
        ##self.col = pygame.Rect(self.x, self.y, 60, 60)
        #display.blit(pygame.transform.rotate(self.img, self.velPulo / 2), (self.x, self.y))
        display.blit(self.img[self.controle], (0, 0))
        #pygame.draw.rect(display,(0,0,0),self.prev,0)
        MousePos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed() == (1, 0, 0) and self.next.collidepoint(MousePos):
            self.controle += 1
            pygame.mouse.set_pos(680, 180)
        if pygame.mouse.get_pressed() == (1, 0, 0) and self.prev.collidepoint(MousePos):
            self.controle -= 1
            pygame.mouse.set_pos(80, 180)
        if(self.controle >=6):
            menu.pag=0
            self.controle = 0

        if(self.controle < 0):
            menu.pag = 0
            self.controle = 0



