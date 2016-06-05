import pygame, sys, random,glob

class Upgrade():
    #Declara atributos da classe
    def __init__ (self):

        self.precoVida = 10
        self.precoSuperPeso = 250
        self.precoPlanar = 2000
        self.precoPuloDuplo = 100
        self.img = pygame.image.load('UpgradeMenu.jpg')
        self.imgVida = pygame.image.load('Life.png')
        self.imgSuperPeso = pygame.image.load('Drop.png')
        self.imgPuloDuplo = pygame.image.load('DoubleJump.png')
        self.imgPlanar = pygame.image.load('Plane.png')
        self.imgVidaFocus = pygame.image.load('LifeFocus.png')
        self.imgSuperPesoFocus = pygame.image.load('DropFocus.png')
        self.imgPuloDuploFocus = pygame.image.load('DoubleJumpFocus.png')
        self.imgPlanarFocus = pygame.image.load('PlaneFocus.png')
        self.menuBtn = pygame.Rect(370,550,90,40)
        self.imgMenu = pygame.image.load('Back.png')
        self.vidaBtn = pygame.Rect(20, 75, 180, 450)
        self.superPesoBtn = pygame.Rect(215, 75, 178, 450)
        self.puloDuploBtn = pygame.Rect(410, 75, 175, 450)
        self.planarBtn = pygame.Rect(602, 75, 180, 450)
        self.fonte = pygame.font.Font("Eastwood.ttf", 40)
        self.fonte2 = pygame.font.Font("Eastwood.ttf", 30)

        # desenhar jogador
    def desenha(self,display,virus):
        ##self.col = pygame.Rect(self.x, self.y, 60, 60)
        levelVida = self.fonte2.render(str(virus.vidaBase), 1, (0, 0, 0))
        dinheiros = self.fonte.render("BitCoins: " + str(virus.dinheiro), 1, (255, 255, 255))
        precoVida = self.fonte.render(str(self.precoVida), 1, (255, 255, 0))
        precoSuperPeso = self.fonte.render(str(self.precoSuperPeso), 1, (255, 255, 0))
        precoPlanar = self.fonte.render(str(self.precoPlanar), 1, (255, 255, 0))
        precoPuloDuplo = self.fonte.render(str(self.precoPuloDuplo), 1, (255, 255, 0))

        #display.blit(pygame.transform.rotate(self.img, self.velPulo/2), (self.x, self.y))
        display.blit(self.img, (0,0))
        display.blit(dinheiros, (300, 10))
        display.blit(levelVida, (138, 285))
        display.blit(precoVida, (40, 450))
        display.blit(precoSuperPeso, (270, 450))
        display.blit(precoPuloDuplo, (460, 450))
        display.blit(precoPlanar, (650, 450))

        #pygame.draw.rect(display, (0, 255, 0), self.menuBtn)
        #pygame.draw.rect(display, (0, 255, 0), self.vidaBtn)
        #pygame.draw.rect(display, (0, 255, 0), self.superPesoBtn)
        #pygame.draw.rect(display, (0, 255, 0), self.puloDuploBtn)
        #pygame.draw.rect(display, (0, 255, 0), self.planarBtn)
        display.blit(self.imgMenu, (370, 550))
        MousePos = pygame.mouse.get_pos()
        if pygame.mouse.get_focused() and self.vidaBtn.collidepoint(MousePos):
            display.blit(self.imgVidaFocus, (56, 109))
        else:
            display.blit(self.imgVida, (59, 112))

        if pygame.mouse.get_focused() and self.superPesoBtn.collidepoint(MousePos) or virus.unlockSuperPeso:
            display.blit(self.imgSuperPesoFocus, (254, 96))
        else:
            display.blit(self.imgSuperPeso, (257, 99))

        if pygame.mouse.get_focused() and self.puloDuploBtn.collidepoint(MousePos) or virus.unlockPuloDuplo:
            display.blit(self.imgPuloDuploFocus, (422, 115))
        else:
            display.blit(self.imgPuloDuplo, (425, 118))

        if pygame.mouse.get_focused() and self.planarBtn.collidepoint(MousePos) or virus.unlockPlanar:
            display.blit(self.imgPlanarFocus, (620, 126))
        else:
            display.blit(self.imgPlanar, (623, 129))
