import pygame
import sys
from board import Board

SIZE = 100 # on release allow this value to be changed by the user

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WINDOW_SIZE = 600

def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    board = Board(SIZE)
    board.board[5][5] = 1
    board.board[4][5] = 1
    board.board[3][5] = 1
    board.board[5][4] = 1
    board.board[5][5] = 1

    while 1:
        pygame.time.wait(1000)
        draw_grid(board)
        board.next_generation()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

def draw_grid(board):
    block_size = WINDOW_SIZE // SIZE
    for x in range(WINDOW_SIZE):
        for y in range(WINDOW_SIZE):
            rect = pygame.Rect(x*block_size, y*block_size,
                               block_size, block_size)
            if board.board[(x//SIZE) - 1][(y//SIZE) - 1] == 1:
                pygame.draw.rect(SCREEN, WHITE, rect, 1)
            else:
                pygame.draw.rect(SCREEN, BLACK, rect, 1)


if __name__ == "__main__":
    main()
