#!/usr/bin/env python3

import kleurmemorie, memorie, pygame

kleurMemorieRect = pygame.Rect(100, 515, 200, 150)
memorieRect = pygame.Rect(400, 515, 200, 150)

def main():
    needsInit = True
    while True:
        if needsInit:
            pygame.init()
            screen = pygame.display.set_mode((1920, 1080))
            pygame.display.set_caption("Keuze menu")
            font = pygame.font.Font(None, 36)
            needsInit = False
        pygame.draw.rect(screen, (255, 255, 255), kleurMemorieRect)
        kleurMemorieText = font.render("Kleurmemorie", True, (0, 0, 0))
        screen.blit(kleurMemorieText, (110, 572))
        pygame.draw.rect(screen, (255, 255, 255), memorieRect)
        memorieText = font.render("Memorie", True, (0, 0, 0))
        screen.blit(memorieText, (410, 572))
        # print("Kies een spel om te spelen:")
        # print("1. Kleurmemorie")
        # print("2. Memorie")
        pygame.display.flip()
        keuze = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if kleurMemorieRect.collidepoint(mouse_pos):
                    keuze = 1
                elif memorieRect.collidepoint(mouse_pos):
                    keuze = 2
                # elif 400 <= mouse_pos[0] <= 600 and 515 <= mouse_pos[1] <= 665:
                #     keuze = 2

        # keuze = input("Voer het nummer van het spel in (1 of 2): ")
        if keuze == 0:
            continue
        elif keuze == 1:
            kleurmemorie.main()
            needsInit = True
        elif keuze == 2:
            memorie.main()
            needsInit = True
        else:
            print("Ongeldige keuze. Voer 1 of 2 in.")
    pygame.quit()

if __name__ == "__main__":
    main()