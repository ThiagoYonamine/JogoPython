import pygame, sys, random,glob

class Menu():
    #Declara atributos da classe
    def __init__ (self):

        self.pag = 0
        self.img = pygame.image.load('Menu.jpg')
        self.start = pygame.Rect(225,328,350,55)
        self.imgStart = pygame.image.load('Start.png')
        self.imgStartFocus = pygame.image.load('StartFocus.png')
        self.upgrade = pygame.Rect(225, 390, 350, 55)
        self.imgUpgrade = pygame.image.load('Upgrade.png')
        self.imgUpgradeFocus = pygame.image.load('UpgradeFocus.png')
        self.tutorial = pygame.Rect(225, 450, 350, 55)
        self.imgTutorial  = pygame.image.load('Tutorial.png')
        self.imgTutorialFocus = pygame.image.load('TutorialFocus.png')
        self.fonte = pygame.font.Font("Eastwood.ttf", 40)

        # desenhar jogador
    def desenha(self,display):
        ##self.col = pygame.Rect(self.x, self.y, 60, 60)
        #display.blit(pygame.transform.rotate(self.img, self.velPulo / 2), (self.x, self.y))
        display.blit(self.img, (0, 0))
        #pygame.draw.rect(display, (0, 255, 0), self.start)
        #pygame.draw.rect(display, (0, 255, 0), self.upgrade)
        #pygame.draw.rect(display, (0, 255, 0), self.tutorial)
        #display.blit(self.imgStart, (357, 348))
        #display.blit(self.imgStart, (327, 407))
        #display.blit(self.imgStart, (328, 466))

        MousePos = pygame.mouse.get_pos()
        if pygame.mouse.get_focused() and self.start.collidepoint(MousePos):
            display.blit(self.imgStartFocus, (350, 341))
        else:
            display.blit(self.imgStart, (357, 348))

        if pygame.mouse.get_focused() and self.upgrade.collidepoint(MousePos):
            display.blit(self.imgUpgradeFocus, (320, 400))
        else:
            display.blit(self.imgUpgrade, (327, 407))

        if pygame.mouse.get_focused() and self.tutorial.collidepoint(MousePos):
            display.blit(self.imgTutorialFocus, (321, 459))
        else:
            display.blit(self.imgTutorial, (328, 466))






