#memorie

from os import remove
import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 700))
pygame.display.set_caption("Kuper Koole Kemorie")

base_color = (255, 255, 255)

colors = [
    (255, 0, 0),       
    (0, 255, 0),       
    (0, 0, 255),       
    (255, 255, 0),     
    (255, 0, 255),     
    (0, 255, 255),     
    (255, 128, 0),     
    (128, 0, 255)      
]
        

kleuren_voor_vierkantjes = colors * 2
random.shuffle(kleuren_voor_vierkantjes)

vierkantjes = [
    (pygame.Rect(100, 100, 100, 100), kleuren_voor_vierkantjes[0]),
    (pygame.Rect(250, 100, 100, 100), kleuren_voor_vierkantjes[1]),
    (pygame.Rect(400, 100, 100, 100), kleuren_voor_vierkantjes[2]),
    (pygame.Rect(550, 100, 100, 100), kleuren_voor_vierkantjes[3]),

    (pygame.Rect(100, 250, 100, 100), kleuren_voor_vierkantjes[4]),
    (pygame.Rect(250, 250, 100, 100), kleuren_voor_vierkantjes[5]),
    (pygame.Rect(400, 250, 100, 100), kleuren_voor_vierkantjes[6]),
    (pygame.Rect(550, 250, 100, 100), kleuren_voor_vierkantjes[7]),

    (pygame.Rect(100, 400, 100, 100), kleuren_voor_vierkantjes[8]),
    (pygame.Rect(250, 400, 100, 100), kleuren_voor_vierkantjes[9]),
    (pygame.Rect(400, 400, 100, 100), kleuren_voor_vierkantjes[10]),
    (pygame.Rect(550, 400, 100, 100), kleuren_voor_vierkantjes[11]),

    (pygame.Rect(100, 550, 100, 100), kleuren_voor_vierkantjes[12]),
    (pygame.Rect(250, 550, 100, 100), kleuren_voor_vierkantjes[13]),
    (pygame.Rect(400, 550, 100, 100), kleuren_voor_vierkantjes[14]),
    (pygame.Rect(550, 550, 100, 100), kleuren_voor_vierkantjes[15])
]


spel_gestart = False
aantal_keer_geklikt = 0
keuzes = []
zichtbare_vierkantjes = []

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            
            for vierkant in drawn_vierkantjes:
                if vierkant[0].collidepoint(mouse_pos):
                    if vierkant not in zichtbare_vierkantjes:
                        zichtbare_vierkantjes.append(vierkant)
                        keuzes.append(vierkant)
                        aantal_keer_geklikt += 1
        if event.type == pygame.QUIT:
            running = False

    else:
        font = pygame.font.Font(None, 36)
        score_teskt = font.render(
            f"Aantal keer geklikt: {aantal_keer_geklikt}", True, (255, 255, 255)
        )
        screen.blit(score_teskt, (20, 20))

    drawn_vierkantjes = []
    for vierkant in vierkantjes:
        if vierkant in zichtbare_vierkantjes:
            kleur = vierkant[1]
        else:
            kleur = base_color

        pygame.draw.rect(screen, kleur, vierkant[0])
        drawn_vierkantjes.append(vierkant)



    if drawn_vierkantjes:
        for vierkant in drawn_vierkantjes:
            if vierkant[0].collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, (255, 255, 255), vierkant[0], 5)

    if len(drawn_vierkantjes) == 0:
        font = pygame.font.Font(None, 74)
        font2 = pygame.font.Font(None, 36)
        text = font.render("Wowie Zowie slimmerd!", True, (255, 255, 255))
        text2 = font.render("Druk op Enter om een nieuw spel te starten.", True, (255, 255, 255))
        text_rect = text.get_rect(center=(400, 350))
        screen.blit(text, text_rect)
        text2_rect = text2.get_rect(center=(300, 500))
        screen.blit(text2, text2_rect)

    
            
    
    pygame.display.flip()

    if len(keuzes) == 2:
        if keuzes[0][1] == keuzes[1][1]:
            vierkantjes.remove(keuzes[0])
            vierkantjes.remove(keuzes[1])
        else:
            pygame.time.delay(800)
        zichtbare_vierkantjes = []
        keuzes = []

    pygame.time.Clock().tick(60)