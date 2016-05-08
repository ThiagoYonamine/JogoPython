import pygame, sys, random,glob
from pygame.locals import *
############################Player#######################################
class Player():
    #Declara atributos da classe
    def __init__ (self):
        self.y = 0
        self.x = 0
        self.velocidade = 12
        self.img = pygame.image.load ('thiago1.png')
        self.img2 = pygame.image.load ('thiago2.png')
        self.area = pygame.Rect(self.x,self.y,60,60)
        self.anima = 0
        self.direcao = 0
        self.ponto = 0
        self.pontoFont = pygame.font.Font("Eastwood.ttf", 40)
        self.vida = 0
        self.imgvida0 = pygame.image.load ('vida0.png')
        self.imgvida25 = pygame.image.load ('vida25.png')
        self.imgvida50 = pygame.image.load ('vida50.png')
        self.imgvida75 = pygame.image.load ('vida75.png')
        self.imgvida100 = pygame.image.load ('vida100.png')
        self.energia = 50
        self.imgenergia100 = pygame.image.load ('energia100.png')
        self.imgenergia75 = pygame.image.load ('energia75.png')
        self.imgenergia50 = pygame.image.load ('energia50.png')
        self.imgenergia25 = pygame.image.load ('energia25.png')
        self.imgenergia15 = pygame.image.load ('energia15.png')
        self.imgenergia10 = pygame.image.load ('energia10.png')

    #desenhar jogador
    def desenhar(self):
        self.anima +=1
        if self.anima > 10:
            self.anima=0
        if self.anima > 5:
            setDisplay.blit(self.img, (self.x,self.y))
        elif self.anima <=5:
            setDisplay.blit(self.img2, (self.x,self.y))
#####################################Movimento SETAS###########################
def movimento(p1):
             #comidas
        for food in foods[:]:
            if p1.area.colliderect(food):
                foods.remove(food)
                p1.ponto +=1
                sushiSound.play()
                p1.energia +=5
             #shuriken
        if p1.area.colliderect(shuriken.area):
            p1.vida +=1
            p1.y = 20
            p1.x = 450
            shuriken.speed_x *= -1
            shuriken.speed_y *= -1
            p1.direcao = 0
        #bordas
        if p1.y <= 100 and p1.direcao >= 1:
            p1.y += 25
        if p1.y >= 650:
            p1.y -= 25
        if p1.x <= 0:
            p1.x +=25
        if p1.x >= 760:
            p1.x -=25


        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
                p1.direcao = 1
                p1.y -= p1.velocidade
                if keys[pygame.K_p] and p1.energia > 0:
                  setDisplay.blit(p1.img, (p1.x,p1.y+20))
                  p1.y -= p1.velocidade+5
                  p1.energia -=1
        elif keys[pygame.K_DOWN]:
                p1.direcao = 2
                p1.y += p1.velocidade
                if keys[pygame.K_p] and p1.energia > 0:
                  setDisplay.blit(p1.img, (p1.x,p1.y-20))
                  p1.y += p1.velocidade+5
                  p1.energia -=1
        elif keys[pygame.K_LEFT]:
                p1.direcao = 4
                p1.x -= p1.velocidade
                if keys[pygame.K_p] and p1.energia > 0:
                  setDisplay.blit(p1.img, (p1.x+20,p1.y))
                  p1.x -= p1.velocidade+5
                  p1.energia -=1
        elif keys[pygame.K_RIGHT]:
                p1.direcao = 3
                p1.x += p1.velocidade
                if keys[pygame.K_p] and p1.energia > 0:
                  setDisplay.blit(p1.img, (p1.x-20,p1.y))
                  p1.x += p1.velocidade+5
                  p1.energia -=1

        #PvP
        if p1.area.colliderect(p2.area):
                if p1.direcao == 1:
                    p2.y -= 15
                    p1.y += 15
                if p1.direcao == 2:
                    p2.y += 15
                    p1.y -= 15
                if p1.direcao == 3:
                    p2.x += 15
                    p1.x -= 15
                if p1.direcao == 4:
                    p2.x -= 15
                    p1.x += 15
def pontos(p1):
            pontos = p1.pontoFont.render(str(p1.ponto), 1, (80, 80, 50))
            setDisplay.blit(pontos, (530, 25))
            ##############vida############
            if p1.vida == 0:
                setDisplay.blit(p1.imgvida100, (600,10))
            elif p1.vida == 1:
                setDisplay.blit(p1.imgvida75,(600,10))
            elif p1.vida == 2:
                setDisplay.blit(p1.imgvida50, (600,10))
            elif p1.vida == 3:
                setDisplay.blit(p1.imgvida25, (600,10))
            elif p1.vida == 4:
                setDisplay.blit(p1.imgvida0, (600,10))
            ############energia############
            if p1.energia > 150:
                setDisplay.blit(p1.imgenergia100, (600,50))
            elif p1.energia > 125:
                setDisplay.blit(p1.imgenergia75, (600,50))
            elif p1.energia > 75:
                setDisplay.blit(p1.imgenergia50, (600,50))
            elif p1.energia > 50:
                setDisplay.blit(p1.imgenergia25, (600,50))
            elif p1.energia > 0:
                setDisplay.blit(p1.imgenergia15, (600,50))
            elif p1.energia == 0:
                setDisplay.blit(p1.imgenergia10, (600,50))


###################################Movimento WASD##########################
def movimento2(p2):
        #comidas
        for food in foods[:]:
            if p2.area.colliderect(food):
                foods.remove(food)
                p2.ponto +=1
                sushiSound.play()
                #Shuriken
                p2.energia +=5

        #Colisao Shuriken
        if p2.area.colliderect(shuriken.area):
            p2.vida += 1
            p2.x = 300
            p2.y = 20
            shuriken.speed_x *= -1
            shuriken.speed_y *= -1
            p2.direcao = 0

        if p2.y <= 100 and p2.direcao >= 1:
            p2.y += 25
        if p2.y >= 650:
            p2.y -= 25
        if p2.x <= 0:
            p2.x +=25
        if p2.x >= 760:
            p2.x -=25

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
              p2.direcao = 1
              p2.y -= p2.velocidade
              if keys[pygame.K_r] and p2.energia > 0:
                  setDisplay.blit(p2.img, (p2.x,p2.y-20))
                  p2.y -= p2.velocidade+5
                  p2.energia -=1
        elif keys[pygame.K_s]:
              p2.direcao = 2
              p2.y += p2.velocidade
              if keys[pygame.K_r] and p2.energia > 0:
                  setDisplay.blit(p2.img, (p2.x,p2.y+20))
                  p2.y += p2.velocidade+5
                  p2.energia -=1
        elif keys[pygame.K_a]:
              p2.direcao = 4
              p2.x -= p2.velocidade
              if keys[pygame.K_r] and p2.energia > 0:
                  setDisplay.blit(p2.img, (p2.x+20,p2.y))
                  p2.x -= p2.velocidade+5
                  p2.energia -=1
        elif keys[pygame.K_d]:
              p2.direcao = 3
              p2.x += p2.velocidade
              if keys[pygame.K_r] and p2.energia > 0:
                  setDisplay.blit(p2.img, (p2.x-20,p2.y))
                  p2.x += p2.velocidade+5
                  p2.energia -=1
          #PvP
        if p2.area.colliderect(p1.area):
                if p2.direcao == 1:
                    p1.y -= 15
                    p2.y += 15
                if p2.direcao == 2:
                    p1.y += 15
                    p2.y -= 15
                if p2.direcao == 3:
                    p1.x += 15
                    p2.x -= 15
                if p2.direcao == 4:
                    p1.x -= 15
                    p2.x += 15
def pontos2(p2):
            pontos = p2.pontoFont.render(str(p2.ponto), 1, (80, 80, 50))
            setDisplay.blit(pontos, (240, 25))

            if p2.vida == 0:
                setDisplay.blit(p2.imgvida100, (60,10))
            elif p2.vida == 1:
                setDisplay.blit(p2.imgvida75,(60,10))
            elif p2.vida == 2:
                setDisplay.blit(p2.imgvida50, (60,10))
            elif p2.vida == 3:
                setDisplay.blit(p2.imgvida25, (60,10))
            elif p2.vida == 4:
                setDisplay.blit(p1.imgvida0, (60,10))
            ############energia############
            if p2.energia > 150:
                setDisplay.blit(p2.imgenergia100, (60,50))
            elif p2.energia > 125:
                setDisplay.blit(p2.imgenergia75, (60,50))
            elif p2.energia > 75:
                setDisplay.blit(p2.imgenergia50, (60,50))
            elif p2.energia > 50:
                setDisplay.blit(p2.imgenergia25, (60,50))
            elif p2.energia > 0:
                setDisplay.blit(p2.imgenergia15, (60,50))
            elif p2.energia == 0:
                setDisplay.blit(p2.imgenergia10, (60,50))
####################################shuriken###################################
class Iminigo():
    def __init__(self):
        self.x = 200
        self.y = 350
        self.speed_x = random.choice([-12,-13,-14,-15,10,11,12,13])
        self.speed_y = random.choice([-6,-7,-8,-9,-17,6,7,8,9,17])
        self.img = pygame.image.load ('shu1.png')
        self.img2 = pygame.image.load ('shu2.png')
        self.anima = 0
        self.area = pygame.Rect(self.x,self.y,170,170)

    def mover(self):
        self.x += self.speed_x
        self.y += self.speed_y
        if self.y <= 100:
            self.speed_y *= -1
        if self.y >= 550:
            self.speed_y *= -1
        if self.x <= 0:
           self.speed_x *=-1
        if self.x >= 650:
           self.speed_x *=-1

    def desenhar(self):
            self.anima+=1
            if self.anima == 10:
                self.anima =0
            if self.anima < 5:
                setDisplay.blit(self.img, (self.x,self.y))
            elif self.anima >=5:
                setDisplay.blit(self.img2, (self.x,self.y))
##################################vencedor###############################
def vencedor(p1,p2):
    op=0
    musica=0
    botao = pygame.Rect(230,590,330,70)##sair
    botao2 = pygame.Rect(230,500,330,70)##jogar novamente
    if(p1.vida == 5) or p2.ponto >=50:
        op=1
    if(p2.vida == 5) or p1.ponto >= 50:
        op=1
    while(op==1):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        if(p1.vida == 5) or p2.ponto >=50:
            if(musica==0):
                vitoria.play()
                musica=1
                pygame.mixer.music.stop()
            vencedor1=pygame.image.load ('vencedor1.png')
            setDisplay.blit(vencedor1, (0,0))
            #pygame.draw.rect(windowSurface, (0,0,0), botao)
            #pygame.draw.rect(windowSurface, (0,0,0), botao2)
            pygame.display.update()
            if pygame.mouse.get_pressed() == (1,0,0) and botao.collidepoint(pygame.mouse.get_pos()):
                pygame.quit()
                sys.exit()
            if pygame.mouse.get_pressed() == (1,0,0) and botao2.collidepoint(pygame.mouse.get_pos()):
                op=0
                p1.vida=0
                p1.ponto=0
                p1.y = 20
                p1.x = 450
                p1.energia=50
                p2.vida=0
                p2.ponto=0
                p2.energia=50
                p2.y = 20
                p2.x = 300
                p1.direcao = 0
                p2.direcao = 0
                pygame.mixer.music.play()
        if(p2.vida == 5) or p1.ponto >= 50:
            if(musica==0):
                vitoria.play()
                musica=1
                pygame.mixer.music.stop()
            vencedor2=pygame.image.load ('vencedor2.png')

            setDisplay.blit(vencedor2, (0,0))
            #pygame.draw.rect(windowSurface, (0,0,0), botao)
            #pygame.draw.rect(windowSurface, (0,0,0), botao2)
            pygame.display.update()
            if pygame.mouse.get_pressed() == (1,0,0) and botao.collidepoint(pygame.mouse.get_pos()):
                pygame.quit()
                sys.exit()
            if pygame.mouse.get_pressed() == (1,0,0) and botao2.collidepoint(pygame.mouse.get_pos()):
                op=0
                p1.vida=0
                p1.ponto=0
                p1.y = 20
                p1.x = 450
                p1.energia=50
                p2.vida=0
                p2.ponto=0
                p2.energia=50
                p2.y = 20
                p2.x = 300
                p1.direcao = 0
                p2.direcao = 0
                pygame.mixer.music.play()

####################################INTRO#################################
def intro():
    alpha=0
    i2 = pygame.image.load ('inicial.png').convert(24)
    i1 = pygame.image.load ('logoPython.png').convert(24)
    setDisplay.fill((255,255,255))
    while alpha <= 300:
        i1.set_alpha(alpha)
        setDisplay.blit(i1, (120,250))
        alpha +=1
        pygame.display.update()
    alpha=0
    setDisplay.fill((255,255,255))
    while alpha <= 150:
        i2.set_alpha(alpha)
        setDisplay.blit(i2, (0,0))
        alpha +=1
        pygame.display.update()
#######################################MENU##############################
def Menu():
    botao3 = pygame.Rect(305,585,190,60)
    jogo = 1
    while(jogo==1):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        menu=pygame.image.load ('menu.png')
        setDisplay.blit(menu, (0,0))
        #pygame.draw.rect(windowSurface, (0,0,0), botao3)
        pygame.display.update()
        if pygame.mouse.get_pressed() == (1,0,0) and botao3.collidepoint(pygame.mouse.get_pos()):
            jogo = 0

#######################################main##############################

# pygame
pygame.init()
pygame.font.init()
mainClock = pygame.time.Clock()
 # Criando janela do jogo
WINDOWWIDTH = 800
WINDOWHEIGHT = 700
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
setDisplay = pygame.display.set_mode((800,700))
pygame.display.set_caption('NINJA')
pygame.font.init()
BLACK = (0,0,0)
#intro
intro()
Menu()
#COMIDA
foodCounter = 0
NEWFOOD = 40
img = pygame.image.load ('sushi.png')
foods = []
for i in range(20):
    foods.append(pygame.Rect(random.randint(0, 775),
        random.randint(100, 675), 25, 25))
#Dados dos jogadores
    #p1
p1 = Player()
p1.y = 20
p1.x = 450
p1.img = pygame.image.load ('th1.png')
p1.img2 = pygame.image.load ('th2.png')
    #p2
p2= Player()
p2.y = 20
p2.x = 300
p2.img = pygame.image.load ('je1.png')
p2.img2 = pygame.image.load ('je2.png')
#suriken
shuriken = Iminigo()
#paredes
paredes = []
paredes.append(pygame.Rect(0,0,800,10))
paredes.append(pygame.Rect(0,0,10,800))
paredes.append(pygame.Rect(0,690,800,10))
paredes.append(pygame.Rect(790,0,10,800))
#musica
sushiSound = pygame.mixer.Sound('sushi.wav')
vitoria = pygame.mixer.Sound('vitoria.wav')
pygame.mixer.music.load('Mbackground.wav')
pygame.mixer.music.play()

#eventos
cont=0
rand = random.randint(100, 500)
#background
background = pygame.image.load ('background.png').convert(24)
#background.set_alpha(150)
# loop do jogo
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    vencedor(p1,p2)

    foodCounter += 1
    if foodCounter >= NEWFOOD:
        # coloca + sushi
        foodCounter = 0
        foods.append(pygame.Rect(random.randint(0, 775),
            random.randint(100, 675), 25, 25))
    # Atualiza o fundo
    setDisplay.blit(background,(0,0))
    #fun\E7oes dos jogadores
    pontos2(p2)
    pontos(p1)
    p1.desenhar()
    p2.desenhar()
    movimento2(p2)
    movimento(p1)
     # desenha as comidas
    for i in range(len(foods)):
        #pygame.draw.rect(windowSurface, (0,0,0 ), foods[i])
        setDisplay.blit(img, foods[i])
    #da shuriken
    shuriken.mover()
    shuriken.desenhar()
    #Calculo da colisao quadrada
    p1.area = pygame.Rect(p1.x,p1.y,60,60)
    p2.area = pygame.Rect(p2.x,p2.y,60,60)
    shuriken.area = pygame.Rect(shuriken.x+15,shuriken.y+15,140,140)
    #pygame.draw.rect(windowSurface, WHITE, pac.area)
    #pygame.draw.rect(windowSurface, BLACK, prof.area)
    #PAREDE
    #pygame.draw.rect(windowSurface, BLACK, paredes[0])
    #pygame.draw.rect(windowSurface, BLACK, paredes[1])
    #pygame.draw.rect(windowSurface, BLACK, paredes[2])
    #pygame.draw.rect(windowSurface, BLACK, paredes[3])
    cont +=1
    #if cont == 100;
    # atualiza a tela
    pygame.display.update()
    mainClock.tick(40)