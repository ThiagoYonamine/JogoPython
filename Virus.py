import pygame, sys, random,glob
import sqlite3
from  useBD import UseBd
BD= UseBd()
BD.create()
BD.imprime()
class Virus():
    #Declara atributos da classe
    def __init__ (self):

        self.score = 0
        self.Hscore = BD.selectScore()
        self.vida = 1
        self.vidaBase = BD.selectVida()
        self.dinheiro = BD.selectDinheiro()
        self.y = 500
        self.x = 200
        self.velPulo = 0
        self.puloDuplo = 1
        self.img = [pygame.image.load('virus0.png'),pygame.image.load('virus1.png'),pygame.image.load('virus2.png'),pygame.image.load('virus3.png'),pygame.image.load('virus4.png'),pygame.image.load('virus5.png')]
        #efeito pulo
        self.efeito = [pygame.image.load('Sprite1.png'),pygame.image.load('Sprite2.png'),pygame.image.load('Sprite4.png'),pygame.image.load('Sprite5.png'),pygame.image.load('Sprite6.png'),pygame.image.load('Sprite7.png'),pygame.image.load('Sprite8.png'),pygame.image.load('Sprite9.png')]
        ##efeito cai
        self.efeito2 = [pygame.image.load('Cai0.png'),pygame.image.load('Cai1.png'),pygame.image.load('Cai2.png'),pygame.image.load('Cai3.png'),pygame.image.load('Cai4.png') ]
        ##efeito dash ARRUMAR NOME DOS ARQUIVOSS
        self.efeito3 = [pygame.image.load('Plana0.png'),pygame.image.load('Plana1.png'),pygame.image.load('Plana2.png'),pygame.image.load('Plana3.png'),pygame.image.load('Plana4.png'),pygame.image.load('Plana5.png')]
        self.controlEfeito = False
        self.controlEfeito2 = False
        self.controlEfeito3 = False
        self.animaEfeito = 0
        self.animaEfeito2 = 0
        self.animaEfeito3 = 0
        self.anima = 0;
        self.estado = "correndo" ## "pulando" ## "planando"
        self.col = pygame.Rect(self.x,self.y,60,60)
        self.fonte = pygame.font.Font("Eastwood.ttf", 30)
        self.unlockPlanar = BD.selectUnlockPlanar()
        self.unlockPuloDuplo = BD.selectUnlockPuloDuplo()
        self.unlockSuperPeso = BD.selectUnlockSuperPeso()


    # desenhar jogador
    def salvaBD(self):
        print("save")
        BD.update(self)
        #BD.imprime()
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

        self.desenhaEfeito(display)
        self.desenhaEfeito2(display)
        self.desenhaEfeito3(display)
        scoref= self.fonte.render("Score: "+ str(int(self.score)), 1, (255, 255, 255))
        vidas = self.fonte.render("Vida: "+ str( self.vida), 1, (255, 255, 255))
        dinheiros = self.fonte.render("BitCoins: "+ str(self.dinheiro), 1, (255, 255, 255))
        display.blit(vidas, (50, 25))
        display.blit(dinheiros, (200, 25))
        display.blit(scoref, (550, 25))

    def desenhaEfeito(self,display):
        if(self.controlEfeito):

            display.blit(self.efeito[int(self.animaEfeito)], (self.x,self.y-10))
            self.animaEfeito +=1
            if(self.animaEfeito >=8):
                self.animaEfeito =0
                self.controlEfeito = False

    def desenhaEfeito2(self, display):
        if (self.controlEfeito2):
            display.blit(self.efeito2[int(self.animaEfeito2)], (190,self.y+75))
            self.animaEfeito2 += 0.5
            if (self.animaEfeito2 >= 4):
                self.animaEfeito2 = 0
                self.controlEfeito2 = False


    def desenhaEfeito3(self, display):
        if (self.controlEfeito3):
            display.blit(pygame.transform.rotate(self.efeito3[int(self.animaEfeito3)], -70+self.animaEfeito3), (self.x-15, self.y-50))

            self.animaEfeito3 += 0.5
            if (self.animaEfeito3 >= 5):
                self.animaEfeito3= 0
                self.controlEfeito3 = False

    def pula(self):

        keys = pygame.key.get_pressed()
        self.y += self.velPulo
        if (self.y < 492):  # caida
            if keys[pygame.K_LEFT ] and self.unlockPlanar:
                self.estado = "planando"
                self.velPulo = 1.8
            elif keys[pygame.K_DOWN ] and self.unlockSuperPeso:
                self.controlEfeito3 = True
                self.estado = "dash"
                self.velPulo += 5
            elif keys[pygame.K_RIGHT]and self.puloDuplo >0 and self.unlockPuloDuplo:
                self.estado = "pulando"
                self.controlEfeito = True
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


