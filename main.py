import pygame, sys, random,glob
from Virus import Virus

class Wall():
    #Declara atributos da classe
    def __init__ (self,vel):
        self.y = 400
        self.x = random.randint(500, 1500)
        self.velocidade = vel
        self.img = pygame.image.load('wall.png')
        self.col = pygame.Rect(self.x, self.y, 40, 60)


    def desenha(self):
        self.x -= self.velocidade
        self.col = pygame.Rect(self.x, self.y, 40, 60)##arrumar o tamanho certo
        display.blit(self.img, (self.x, self.y))

#
class Moedas():
    #Declara atributos da classe
    def __init__ (self,vel):
        self.y = random.randint(230, 350)
        self.x = random.randint(500, 1500)
        self.velocidade = vel
        self.img = pygame.image.load('moeda.png')

        self.col = pygame.Rect(self.x, self.y, 40, 60)  ##arrumar o tamanho certo

    def desenha(self):
        self.x -= self.velocidade
        self.col = pygame.Rect(self.x, self.y, 40, 60)##arrumar o tamanho certo
        display.blit(self.img, (self.x, self.y))

####se pa herança
### cenario pode ter uma lista de walls
class Cenario():
    #Declara atributos da classe
    def __init__ (self):
        self.y = 0
        self.x = 0
        self.velocidade = 6
        self.img = pygame.image.load('background.png')
        self.listWalls = []
        self.listMoedas = []

    def desenha(self):
        ##background
        self.x -= self.velocidade
        display.blit(self.img, (self.x, self.y))
        if(self.x <= 500-800): # recomeça o background
            self.x=0

        ###walls
        for i in range(len(cenario.listWalls)):
            self.listWalls[i].desenha()

        ###moedas
        for i in range(len(cenario.listMoedas)):
            self.listMoedas[i].desenha()

    ##nao sei se esse é o melhor lugar para isso
    def update(self):
        w = 0
        while (w < len(self.listWalls)):
            ##wall sai do mapa
            if (self.listWalls[w].x < -20):
                self.listWalls.remove(self.listWalls[w])

             ##moeda sai do mapa
            if (self.listMoedas[w].x < -20):
                self.listMoedas.remove(self.listMoedas[w])

            w += 1

        ##coloca + wall, deixa sempre com 2, substituir por num_wall
        if (len(self.listWalls) < 2):
            self.listWalls.append(Wall(self.velocidade))
        ##coloca + wall, deixa sempre com 2, substituir por num_wall
        if (len(self.listMoedas) < 5):
            self.listMoedas.append(Moedas(self.velocidade))

    def checkColisao(self,virus):
        w = 0
        while (w < len(self.listWalls)):
            if ((virus.col.colliderect(self.listWalls[w].col))):
                self.listWalls.remove(self.listWalls[w])

            w += 1

    def criaWalls(self):
        for i in range(2):
            self.listWalls.append(Wall(cenario.velocidade))

    def criaMoedas(self):
        for i in range(5):
            self.listMoedas.append(Moedas(cenario.velocidade))


pygame.init()
pygame.font.init()
mainClock = pygame.time.Clock()
display = pygame.display.set_mode((500,600)) ## mudar de acordo com a img certa. ps 1ª ser +- 1/3 da img
pygame.display.set_caption('Jogo')

virus = Virus()
cenario = Cenario()
cenario.criaWalls()
cenario.criaMoedas()
#################apenas um teste, colocar uma lista de walls no cenario, mudar desenha do cenario para desenhar walls tbm###
#git
###########################################################################################################################

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    cenario.desenha()
    cenario.update()
    cenario.checkColisao(virus)

    #####################colocar no desenha do cenario########################3

    ################achar um lugar pra iss0 -_-##############################

    ################################################

    virus.desenha(display)
    virus.pula()
    pygame.display.update()
    mainClock.tick(40)
