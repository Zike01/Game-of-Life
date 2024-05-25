import time
import pygame
import numpy as np

BG_COLOR = (0, 0, 0)
GRID_COLOR = (40, 40, 40)
WHITE = (255, 255, 255)


def iterate(screen, board, size):
    # Initialise new state of the board
    updated_board = np.zeros((board.shape[0], board.shape[1]))

    for row, col in np.ndindex(board.shape):
        # calculate the number of alive neighboring cells
        live = np.sum(board[row - 1 : row + 2, col - 1 : col + 2]) - board[row, col]
        color = BG_COLOR if board[row, col] == 0 else WHITE

        if board[row, col] == 1:
            if 2 <= live <= 3:
                updated_board[row, col] = 1
        else:
            if live == 3:
                updated_board[row, col] = 1

        pygame.draw.rect(screen, color, (col * size, row * size, size - 1, size - 1))

    return updated_board


def main():
    # Pygame setup
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Conway's Game of Life")

    # Initialise board
    board = np.zeros((60, 80))
    screen.fill(GRID_COLOR)
    iterate(screen, board, 10)

    pygame.display.flip()
    pygame.display.update()

    running = False

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    return

                # Play/pause the game when the user presses the 'Space' key
                if event.key == pygame.K_SPACE:
                    running = not running

                # Clear the entire screen when the user presses the 'C' key
                if event.key == pygame.K_c:
                    running = False
                    board = np.zeros((60, 80))

            # Get the user's mouse position to draw and clear cells before starting the game
            pos = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if click[0]:  # Left click
                board[pos[1] // 10, pos[0] // 10] = 1
            elif click[2]:  # Right click
                board[pos[1] // 10, pos[0] // 10] = 0

            iterate(screen, board, 10)
            pygame.display.update()

        if running:
            board = iterate(screen, board, 10)
            pygame.display.update()

        time.sleep(0.05)


if __name__ == "__main__":
    main()
