import pygame, sys, random,glob
from Virus import Virus
from Menu import Menu
from Upgrade import Upgrade
from Moedas import Moedas
from Wall import Wall
from Antivirus import Antivirus
class Cenario():
    #Declara atributos da classe
    def __init__ (self):
        self.controle = 0
        self.nivel = 1
        self.y = 0
        self.x = 0
        self.velocidade = 6

        self.numWall = 1
        self.numAntivirus = 0
        self.img = pygame.image.load('background.jpg')
        self.floor = pygame.image.load('Floor.png')
        self.imgRed = pygame.image.load('Untitled-1.png')
        self.listWalls = []
        self.listMoedas = []
        self.listAntivirus = []

    def desenha(self,display):
        ##background
        self.x -= self.velocidade

        display.blit(self.img, (self.x, self.y))

        if(self.x <= 800-2753): # recomeça o background
            self.x=0

        ###walls
        for i in range(len(self.listWalls)):
            self.listWalls[i].desenha(display,self.velocidade)

        ###moedas
        for i in range(len(self.listMoedas)):
            self.listMoedas[i].desenha(display,self.velocidade)

        ###antivirus
        for i in range(len(self.listAntivirus)):
            self.listAntivirus[i].desenha(display,self.velocidade)

    def desenhaFloor(self, display):
        display.blit(self.floor, (self.x, 527))

        display.blit(self.imgRed, (0, 0))


    def update(self):
        w = 0
        while (w < len(self.listWalls)):
            ##wall sai do mapa
            if (self.listWalls[w].x < -40):
                self.listWalls.remove(self.listWalls[w])
            w += 1

        w = 0
        while (w < len(self.listMoedas)):
             ##moeda sai do mapa
            if (self.listMoedas[w].x < -30):
                self.listMoedas.remove(self.listMoedas[w])
            w += 1

        w = 0
        while (w < len(self.listAntivirus)):
            ##antivirus sai do mapa
            if (self.listAntivirus[w].x < -60):
                self.listAntivirus.remove(self.listAntivirus[w])
            w += 1



        if (len(self.listWalls) < self.numWall):
            self.listWalls.append(Wall())

        if (len(self.listMoedas) < 5):
            self.listMoedas.append(Moedas())

        if (len(self.listAntivirus) < self.numAntivirus):
            self.listAntivirus.append(Antivirus())

    def criaWalls(self):
        for i in range(2):
            self.listWalls.append(Wall())

    def criaMoedas(self):
        for i in range(5):
           self.listMoedas.append(Moedas())

    def criaAntivirus(self):
        for i in range(2):
            self.listAntivirus.append(Antivirus())

    def controler(self):
        self.controle += 0.1


        if(self.controle >= self.nivel*25 ):

            self.nivel += 1
            ##print(self.nivel)
            self.velocidade += 0.5
            self.controle = 0

            if(self.nivel%2 ==0):
                self.numAntivirus += 1
                self.numWall += 1




    def reset(self):
        self.controle = 0
        self.nivel = 1
        self.y = 0
        self.x = 0
        self.velocidade = 6
        self.numWall = 1
        self.numAntivirus = 0

        w = 0
        while (w < len(self.listWalls)):
            ##wall sai do mapa

            self.listWalls.remove(self.listWalls[w])
            w += 1

        w = 0
        while (w < len(self.listMoedas)):
            ##moeda sai do mapa

            self.listMoedas.remove(self.listMoedas[w])
            w += 1

        w = 0
        while (w < len(self.listAntivirus)):
            ##antivirus sai do mapa

            self.listAntivirus.remove(self.listAntivirus[w])
            w += 1