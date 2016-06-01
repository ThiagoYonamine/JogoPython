import pygame, sys, random,glob

class Antivirus():
    #Declara atributos da classe
    def __init__ (self):
        self.tipo = 'antivirus'
        self.y = random.randint(130, 430)
        self.x = random.randint(1000, 2500)
        self.velocidade = 0
        self.altura = 2
        self.img = pygame.image.load('antivirus.png')

        self.col = pygame.Rect(self.x, self.y, 40, 60)  ##arrumar o tamanho certo

    def desenha(self,display,vel):
        if(self.y > 430):
            self.altura *=-1
        elif(self.y < 130):
            self.altura *=-1
        self.x -= vel
        #self.y += random.randint(-3, 3) #moeda treme
        self.y += self.altura
        self.col = pygame.Rect(self.x, self.y, 60, 70)##arrumar o tamanho certo
        #pygame.draw.rect(display, (0, 255, 0), self.col)  ## colisão
        display.blit(self.img, (self.x, self.y))
