import pygame, sys, random,glob
from Virus import Virus

class Wall():
    #Declara atributos da classe
    def __init__ (self,vel):
        self.tipo = 'wall'
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
        self.tipo = 'moeda'
        self.y = random.randint(230, 350)
        self.x = random.randint(500, 1500)
        self.velocidade = vel
        self.img = pygame.image.load('moeda.png')

        self.col = pygame.Rect(self.x, self.y, 40, 60)  ##arrumar o tamanho certo

    def desenha(self):

        self.x -= self.velocidade
        #self.y += random.randint(-3, 3) #moeda treme

        self.col = pygame.Rect(self.x, self.y, 40, 60)##arrumar o tamanho certo
        display.blit(self.img, (self.x, self.y))

class Antivirus():
    #Declara atributos da classe
    def __init__ (self,vel):
        self.tipo = 'antivirus'
        self.y = random.randint(230, 350)
        self.x = random.randint(500, 2000)
        self.velocidade = vel
        self.altura = 2
        self.img = pygame.image.load('wall.png')

        self.col = pygame.Rect(self.x, self.y, 40, 60)  ##arrumar o tamanho certo

    def desenha(self):
        if(self.y > 350):
            self.altura *=-1
        elif(self.y < 200):
            self.altura *=-1
        self.x -= self.velocidade
        #self.y += random.randint(-3, 3) #moeda treme
        self.y += self.altura
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
        self.listAntivirus = []

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

        ###antivirus
        for i in range(len(cenario.listAntivirus)):
            self.listAntivirus[i].desenha()

    ##nao sei se esse é o melhor lugar para isso
    def update(self):
        w = 0
        while (w < len(self.listWalls)):
            ##wall sai do mapa
            if (self.listWalls[w].x < -20):
                self.listWalls.remove(self.listWalls[w])
            w += 1

        w = 0
        while (w < len(self.listMoedas)):
             ##moeda sai do mapa
            if (self.listMoedas[w].x < -20):
                self.listMoedas.remove(self.listMoedas[w])
            w += 1

        w = 0
        while (w < len(self.listAntivirus)):
            ##antivirus sai do mapa
            if (self.listAntivirus[w].x < -20):
                self.listAntivirus.remove(self.listAntivirus[w])
            w += 1




        ##coloca + wall, deixa sempre com 2, substituir por num_wall
        if (len(self.listWalls) < 2):
            self.listWalls.append(Wall(self.velocidade))
        ##coloca + wall, deixa sempre com 2, substituir por num_wall
        if (len(self.listMoedas) < 5):
            self.listMoedas.append(Moedas(self.velocidade))
        ##coloca + wall, deixa sempre com 2, substituir por num_wall
        if (len(self.listAntivirus) < 2):
            self.listAntivirus.append(Antivirus(self.velocidade))

    def criaWalls(self):
        for i in range(2):
            self.listWalls.append(Wall(cenario.velocidade))

    def criaMoedas(self):
        for i in range(5):
            self.listMoedas.append(Moedas(cenario.velocidade))

    def criaAntivirus(self):
        for i in range(2):
            self.listAntivirus.append(Antivirus(cenario.velocidade))

##alguns metodos sei la de quem
def checkColisao(obj, virus):
    w = 0
    while (w < len(obj)):
        if ((virus.col.colliderect(obj[w].col))):

            if(obj[w].tipo == 'wall'):
                virus.vida -= 1

            if(obj[w].tipo == 'antivirus'):
                if (obj[w].y >= virus.y + 20 or virus.velPulo > 0):
                    virus.velPulo = -20
                    virus.dinheiro += 5
                else:
                    virus.vida -= 1
            if(obj[w].tipo == 'moeda'):
                virus.dinheiro += 1
            obj.remove(obj[w])
        w += 1

pygame.init()
pygame.font.init()
mainClock = pygame.time.Clock()
display = pygame.display.set_mode((500,600)) ## mudar de acordo com a img certa. ps 1ª ser +- 1/3 da img
pygame.display.set_caption('Jogo')

virus = Virus()
cenario = Cenario()
cenario.criaWalls()
cenario.criaMoedas()
cenario.criaAntivirus()
#################apenas um teste, colocar uma lista de walls no cenario, mudar desenha do cenario para desenhar walls tbm###
#git
###########################################################################################################################

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    cenario.desenha()
    cenario.update()
    checkColisao(cenario.listWalls,virus)
    checkColisao(cenario.listMoedas,virus)
    checkColisao(cenario.listAntivirus,virus)
    virus.desenha(display)
    virus.pula()
    pygame.display.update()
    mainClock.tick(40)
