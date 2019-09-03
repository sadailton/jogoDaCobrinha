from time import sleep
import pygame
import random

branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)

try:
    pygame.init()
except:
    print("Erro ao carregar o pygame")
    exit(1)

janela_largura = 800
janela_altura = 600

tamanho_cobra = 10
relogio = pygame.time.Clock()

fundo = pygame.display.set_mode((janela_largura,janela_altura))
pygame.display.set_caption("Jogo da cobrinha")

def texto(msg, cor, tamanho_fonte, x, y):
    fonte = pygame.font.SysFont(None, tamanho_fonte)
    texto1 = fonte.render(msg, True, cor)
    fundo.blit(texto1, [x, y])


def desenha_cobra(CobraXY, tamanho_cobra):
    for XY in CobraXY:
        pygame.draw.rect(fundo, branco, [XY[0], XY[1], tamanho_cobra, tamanho_cobra])


def desenha_fruta(pos_fruta_x, pos_fruta_y, cor):
    pygame.draw.rect(fundo, cor, [pos_fruta_x, pos_fruta_y, tamanho_cobra, tamanho_cobra])


def placar(pontos):
    texto("Pontos: "+str(pontos), azul, 25, 0, 10)


def jogo():
    sair = False
    fimdejogo = False
    pos_x = random.randrange(0, janela_largura - tamanho_cobra, 10)
    pos_y = random.randrange(0, janela_altura - tamanho_cobra, 10)
    pos_fruta_x = random.randrange(0, janela_largura - tamanho_cobra, 10)
    pos_fruta_y = random.randrange(0, janela_altura - tamanho_cobra, 10)

    velocidade_x = 0
    velocidade_y = 0
    CobraXY = []
    comprimentocobra = 1
    pontos = 0

    while not sair:
        while fimdejogo:
            fundo.fill(preto)
            texto("Fim de jogo! Para continuar tecle C ou S para sair", vermelho, 25, janela_largura/8, janela_altura/2)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sair = True
                    fimdejogo = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        sair = False
                        fimdejogo = False
                        pos_x = random.randrange(0, janela_largura - tamanho_cobra, 10)
                        pos_y = random.randrange(0, janela_altura - tamanho_cobra, 10)
                        pos_fruta_x = random.randrange(0, janela_largura - tamanho_cobra, 10)
                        pos_fruta_y = random.randrange(0, janela_altura - tamanho_cobra, 10)
                        velocidade_x = 0
                        velocidade_y = 0
                        CobraXY = []
                        comprimentocobra = 1
                        pontos = 0
                    if event.key == pygame.K_s:
                        sair = True
                        fimdejogo = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and velocidade_x != tamanho_cobra:
                    velocidade_y = 0
                    velocidade_x = -tamanho_cobra
                if event.key == pygame.K_RIGHT and velocidade_x != -tamanho_cobra:
                    velocidade_y = 0
                    velocidade_x = tamanho_cobra
                if event.key == pygame.K_UP and velocidade_y != tamanho_cobra:
                    velocidade_x = 0
                    velocidade_y = -tamanho_cobra
                if event.key == pygame.K_DOWN and velocidade_y != -tamanho_cobra:
                    velocidade_x = 0
                    velocidade_y = tamanho_cobra
                if event.key == pygame.K_SPACE:
                    comprimentocobra += 2

        fundo.fill(preto)
        pos_x += velocidade_x
        pos_y += velocidade_y

        if pos_x >= janela_largura:
            pos_x = 0
        elif pos_x < 0:
            pos_x = janela_largura
        elif pos_y >= janela_altura:
            pos_y = 0
        elif pos_y < 0:
            pos_y = janela_altura

        if pos_x == pos_fruta_x and pos_y == pos_fruta_y:
            pos_fruta_x = random.randrange(0, janela_largura - tamanho_cobra, 10)
            pos_fruta_y = random.randrange(0, janela_altura - tamanho_cobra, 10)
            comprimentocobra += 1
            pontos += 1

        Cabecacobra = []
        Cabecacobra.append(pos_x)
        Cabecacobra.append(pos_y)
        CobraXY.append(Cabecacobra)
        if len(CobraXY) > comprimentocobra:
            del CobraXY[0]
        if any(Bloco == Cabecacobra for Bloco in CobraXY[:-1]):
            fimdejogo = True

        desenha_cobra(CobraXY, tamanho_cobra)
        desenha_fruta(pos_fruta_x, pos_fruta_y, verde)
        placar(pontos)
        relogio.tick(25)
        pygame.display.update()

jogo()

pygame.quit()
