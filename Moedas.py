import pygame, sys, random,glob
class Moedas():
    #Declara atributos da classe
    def __init__ (self):
        self.tipo = 'moeda'
        self.y = random.randint(200, 400)
        self.x = random.randint(800, 1500)
        self.velocidade = 0
        self.img = [ pygame.image.load('Coin1.png'), pygame.image.load('Coin0.png'),pygame.image.load('Coin1.png'),pygame.image.load('Coin2.png'),pygame.image.load('Coin3.png'),pygame.image.load('Coin4.png'),pygame.image.load('Coin5.png'),pygame.image.load('Coin6.png'),pygame.image.load('Coin7.png'),pygame.image.load('Coin8.png'),pygame.image.load('Coin9.png'),pygame.image.load('Coin10.png'),pygame.image.load('Coin11.png'),pygame.image.load('Coin12.png'),pygame.image.load('Coin13.png'),]
        self.anima = 0
        self.animAux =0
        self.col = pygame.Rect(self.x, self.y, 40, 60)  ##arrumar o tamanho certo

    def desenha(self,display,vel):
        self.x -= vel
        #self.y += random.randint(-3, 3) #moeda treme

        self.col = pygame.Rect(self.x, self.y, 40, 40)##arrumar o tamanho certo
        #pygame.draw.rect(display, (0, 255, 0), self.col)  ## colisão
        display.blit(self.img[int(self.anima)], (self.x, self.y))

        self.anima +=0.2
        if(self.anima >= 13):
            self.anima = 0