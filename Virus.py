import pygame, sys, random,glob

class Virus():
    #Declara atributos da classe
    def __init__ (self):
        self.score = 0
        self.vida = 1
        self.vidaBase = 1
        self.dinheiro = 0
        self.y = 500
        self.x = 200
        self.velPulo = 0
        self.puloDuplo = 1
        self.img = [pygame.image.load('virus0.png'),pygame.image.load('virus1.png'),pygame.image.load('virus2.png'),pygame.image.load('virus3.png'),pygame.image.load('virus4.png'),pygame.image.load('virus5.png')]
        self.efeito = [pygame.image.load('Sprite1.png'),pygame.image.load('Sprite2.png'),pygame.image.load('Sprite4.png'),pygame.image.load('Sprite5.png'),pygame.image.load('Sprite6.png'),pygame.image.load('Sprite7.png'),pygame.image.load('Sprite8.png'),pygame.image.load('Sprite9.png')]
        self.controlEfeito = False
        self.animaEfeito = 0
        self.anima = 0;
        self.estado = "correndo" ## "pulando" ## "planando"
        self.col = pygame.Rect(self.x,self.y,60,60)
        self.fonte = pygame.font.Font("Eastwood.ttf", 30)
        self.unlockPlanar = False
        self.unlockPuloDuplo = False
        self.unlockSuperPeso = False

        # desenhar jogador
    def desenha(self,display):
        self.col = pygame.Rect(self.x, self.y, 76, 76)
        self.score += 0.1
        #display.blit(pygame.transform.rotate(self.img, self.velPulo/2), (self.x, self.y))

        display.blit(self.img[int(self.anima)], (self.x, self.y))
        if(self.estado=="correndo"):
            self.anima += 1
        if (self.estado == "planando"):
            self.anima -= 0.25
        if(self.estado =="pulando"):
            self.anima -= 1
        if (self.estado == "dash"):
            self.anima += 3
        if(self.anima >=6):
            self.anima = 0
        if (self.anima < 0):
            self.anima = 5

        scoref= self.fonte.render("Score: "+ str(int(self.score)), 1, (255, 255, 255))
        vidas = self.fonte.render("Vida: "+ str( self.vida), 1, (255, 255, 255))
        dinheiros = self.fonte.render("BitCoins: "+ str(self.dinheiro), 1, (255, 255, 255))
        display.blit(vidas, (50, 25))
        display.blit(dinheiros, (200, 25))
        display.blit(scoref, (550, 25))

    def desenhaEfeito(self,display):
        if(self.controlEfeito):
            display.blit(self.efeito[int(self.animaEfeito)], (200,420))
            self.animaEfeito +=1
            if(self.animaEfeito >=8):
                self.animaEfeito =0
                self.controlEfeito = False

    def pula(self):

        keys = pygame.key.get_pressed()
        self.y += self.velPulo
        if (self.y < 492):  # caida
            if keys[pygame.K_LEFT ] and self.unlockPlanar:
                self.estado = "planando"
                self.velPulo = 1.8
                #self.velPulo += 0.1
                ##OUU correção do "bug" self.velPulo = 0 e tirar and
            elif keys[pygame.K_DOWN ] and self.unlockSuperPeso:
                self.estado = "dash"
                self.velPulo += 5
            elif keys[pygame.K_RIGHT]and self.puloDuplo >0 and self.unlockPuloDuplo:
                self.estado = "pulando"
                self.velPulo = -30
                self.puloDuplo -=1
            else:
                self.velPulo += 2

        if (self.y >= 492):  # chao

            self.estado = "correndo"
            self.velPulo = 0
            self.y = 492
            self.puloDuplo = 1

        if keys[pygame.K_UP ]:
            if (self.y >= 492):
                self.controlEfeito = True
                self.estado = "pulando"
                self.velPulo = -30


