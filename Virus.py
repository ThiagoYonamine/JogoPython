import pygame, sys, random,glob

class Virus():
    #Declara atributos da classe
    def __init__ (self):
        self.vida = 1
        self.y = 400
        self.x = 200
        self.velPulo = 0
        self.img = pygame.image.load('virus.png')
        self.col = pygame.Rect(self.x,self.y,60,60)
        self.fonte = pygame.font.Font("Eastwood.ttf", 40)

        # desenhar jogador
    def desenha(self,display):
        self.col = pygame.Rect(self.x, self.y, 60, 60)

        #display.blit(pygame.transform.rotate(self.img, self.velPulo/2), (self.x, self.y))
        display.blit(self.img, (self.x, self.y))
        vidas = self.fonte.render(str(self.vida), 1, (80, 80, 50))
        display.blit(vidas, (50, 25))

    def pula(self):

        keys = pygame.key.get_pressed()
        self.y += self.velPulo
        if (self.y < 400):  # caida
            if keys[pygame.K_LEFT] and self.y > 200:
                self.velPulo += 0.1
                ##OUU correção do "bug" self.velPulo = 0 e tirar and
            elif keys[pygame.K_DOWN]:
                self.velPulo += 6
            else:
                self.velPulo += 2

        if (self.y >= 400):  # chao
            self.velPulo = 0
            self.y = 400

        if keys[pygame.K_UP]:
            if (self.y >= 400):
                self.velPulo = -25
