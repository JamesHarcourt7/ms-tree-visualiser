import pygame
from MinimumSpanningTree import Kruskals


def main():
    # Initialise pygame and display
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    running = True

    # Main loop
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #Logic

        # Update display
        screen.fill((255, 255, 255))
        pygame.display.update()

    # Quit
    pygame.quit()


def text_demo():
    vertices = [n for n in range(7)]
    edges = [(0, 1, 1), (0, 3, 4), (1, 2, 2), (1, 3, 6), (1, 4, 4), (3, 4, 3), (3, 6, 4), (2, 4, 5), (2, 5, 6),
             (4, 5, 8), (5, 6, 3), (4, 6, 7)]
    Kruskals(edges, vertices)


if __name__ == "__main__":
    text_demo()
