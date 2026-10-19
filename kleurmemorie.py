#!/usr/bin/env python3

import random
import pygame

WIDTH = 600
HEIGHT = 650
COLORS = [
    ((143, 32, 32), (255, 77, 77)),
    ((29, 79, 145), (77, 154, 255)),
    ((35, 115, 58), (77, 255, 122)),
    ((143, 117, 28), (255, 227, 77)),
]
SQUARES = [
    pygame.Rect(80, 150, 200, 180),
    pygame.Rect(320, 150, 200, 180),
    pygame.Rect(80, 370, 200, 180),
    pygame.Rect(320, 370, 200, 180),
]


def draw_game(screen, font, message, score, light=-1):
    screen.fill((25, 25, 25))

    title = font.render("Colour Memory", True, "white")
    text = font.render(message, True, "white")
    points = font.render(f"Ronde: {score}", True, "white")
    screen.blit(title, (200, 25))
    screen.blit(text, (200, 75))
    screen.blit(points, (235, 105))

    for number, square in enumerate(SQUARES):
        if number == light:
            color = COLORS[number][1]
        else:
            color = COLORS[number][0]
        pygame.draw.rect(screen, color, square, border_radius=12)

    pygame.display.flip()


def show_sequence(screen, font, sequence, score):
    for color_number in sequence:
        draw_game(screen, font, "Onthoud de kleuren...", score, color_number)
        pygame.time.delay(400)
        draw_game(screen, font, "Onthoud de kleuren...", score)
        pygame.time.delay(150)


def get_player_answer(screen, font, sequence, score):
    position = 0

    while position < len(sequence):
        draw_game(screen, font, "Jouw beurt", score)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None

            if event.type == pygame.MOUSEBUTTONDOWN:
                for number, square in enumerate(SQUARES):
                    if square.collidepoint(event.pos):
                        draw_game(screen, font, "Jouw beurt", score, number)
                        pygame.time.delay(180)

                        if number != sequence[position]:
                            return False

                        position += 1

    return True


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Colour Memory")
    font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()

    sequence = []
    score = 0
    playing = True

    while playing:
        sequence.append(random.randrange(4))
        show_sequence(screen, font, sequence, score)
        answer = get_player_answer(screen, font, sequence, score)

        if answer is None:
            playing = False
        elif answer:
            score += 1
            draw_game(screen, font, "Goed gedaan!", score)
            pygame.time.delay(700)
        else:
            draw_game(screen, font, "Fout! Druk op Enter.", score)
            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        playing = False
                        waiting = False
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        sequence = []
                        score = 0
                        waiting = False
                clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
