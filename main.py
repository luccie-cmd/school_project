#!/usr/bin/env python3

import kleurmemorie, memorie, pygame

FONT_SIZE = 36

def main():
    needsInit = True
    screenWidth, screenHeight = (0, 0)
    while True:
        if needsInit:
            pygame.init()
            screenWidth, screenHeight = pygame.display.get_desktop_sizes()[0]
            screen = pygame.display.set_mode((screenWidth, screenHeight))
            pygame.display.set_caption("Keuze menu")
            font = pygame.font.Font(None, FONT_SIZE)
            needsInit = False
        kleurMemorieRect = pygame.Rect(screenWidth // 2 - 200 - 100, screenHeight // 2 - 75, 200, 150)
        memorieRect = pygame.Rect(screenWidth // 2 + 200 - 100, screenHeight // 2 - 75, 200, 150)
        pygame.draw.rect(screen, (255, 255, 255), kleurMemorieRect)
        kleurMemorieText = font.render("Kleurmemorie", True, (0, 0, 0))
        screen.blit(kleurMemorieText, (kleurMemorieRect.x + 10, kleurMemorieRect.y + (kleurMemorieRect.height - FONT_SIZE) // 2))
        pygame.draw.rect(screen, (255, 255, 255), memorieRect)
        memorieText = font.render("Memorie", True, (0, 0, 0))
        screen.blit(memorieText, (memorieRect.x + 10, memorieRect.y + (memorieRect.height - FONT_SIZE) // 2))
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