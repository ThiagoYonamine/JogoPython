import pygame, sys, random,glob

class Avast():
    #Declara atributos da classe
    def __init__ (self):
        self.tipo = 'avast'
        self.y = random.randint(130, 430)
        self.x = random.randint(1000, 2500)
        self.velocidade = 0
        self.altura = 2
        self.img = pygame.image.load('Avast.png')
        self.col = pygame.Rect(self.x, self.y, 50, 40)  ##arrumar o tamanho certo
        self.angulo =0

    def desenha(self,display,vel):
        self.velocidade = vel/2
        if(self.x <= 600):
            self.velocidade +=10
            self.angulo = 45

        self.x -= self.velocidade
        #self.y += random.randint(-3, 3) #moeda treme
        self.col = pygame.Rect(self.x, self.y+10, 50, 40)##arrumar o tamanho certo
        #pygame.draw.rect(display, (0, 255, 0), self.col)  ## colisao
        display.blit(pygame.transform.rotate(self.img, self.angulo), (self.x, self.y))
