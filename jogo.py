import pygame
import random
import sys

pygame.init()

L = 600
A = 400

tela = pygame.display.set_mode((L, A))
pygame.display.set_caption("Desvie do Bloco!")

imagem = pygame.image.load("durin.jpeg")
imagem = pygame.transform.scale(imagem,(600,400))
# CORES
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (200, 0, 0)
azul = (0, 80, 200)
amarelo = (255, 255, 0)

# JOGADOR EM DICIONÁRIO
player = {
    "x": L // 2,
    "y": A - 50,
    "vel": 5,
    "tam": 40
}

# OBSTÁCULO EM DICIONÁRIO
obstaculo = {
    "x": random.randint(0, L - 40),
    "y": -50,
    "vel": 5,
    "tam": 40
}

# BÔNUS EM DICIONÁRIO
bonus = {
    "x": random.randint(0, L - 40),
    "y": -50,
    "vel": 5,
    "tam": 40
}

ponto = 0
fonte = pygame.font.SysFont(None, 40)
relogio = pygame.time.Clock()
rodando = True

while rodando:
    relogio.tick(60)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # CONTROLE DO JOGADOR
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and player["x"] > 0:
        player["x"] -= player["vel"]

    if teclas[pygame.K_RIGHT] and player["x"] < L - player["tam"]:
        player["x"] += player["vel"]

    # MOVIMENTO DOS OBJETOS
    obstaculo["y"] += obstaculo["vel"]
    bonus["y"] += bonus["vel"]

    # RESETAR OBSTÁCULO
    if obstaculo["y"] > A:
        obstaculo["y"] = -obstaculo["tam"]
        obstaculo["x"] = random.randint(0, L - obstaculo["tam"])
        ponto += 1
        obstaculo["vel"] += 0.2

    # RESETAR BÔNUS
    if bonus["y"] > A:
        bonus["y"] = -bonus["tam"]
        bonus["x"] = random.randint(0, L - bonus["tam"])

    # TRANSFORMAR EM RECT
    rect_player = pygame.Rect(player["x"], player["y"], player["tam"], player["tam"])
    rect_obs = pygame.Rect(obstaculo["x"], obstaculo["y"], obstaculo["tam"], obstaculo["tam"])
    rect_bonus = pygame.Rect(bonus["x"], bonus["y"], bonus["tam"], bonus["tam"])

    # COLISÃO COM OBSTÁCULO
    if rect_player.colliderect(rect_obs):
        print("Game Over!")
        rodando = False

    # COLISÃO COM BÔNUS
    if rect_player.colliderect(rect_bonus):
        ponto += 2
        bonus["vel"] += 0.5
        bonus["y"] = -bonus["tam"]
        bonus["x"] = random.randint(0, L - bonus["tam"])

    # DESENHO
    tela.fill(preto)
    tela.blit(imagem, (0, 0))

    pygame.draw.rect(tela, azul, rect_player)
    pygame.draw.rect(tela, vermelho, rect_obs)
    pygame.draw.circle(tela, amarelo, rect_bonus.center,rect_bonus.width//2)

    texto = fonte.render(f"Pontos: {ponto}", True, branco)
    tela.blit(texto, (10, 10))

    pygame.display.update()

pygame.quit()