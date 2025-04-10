import pygame
import sys
from board import Board
from player import Player
from controlUI import ControlUI
from tables import Table

WIDTH = 1200
HEIGHT = 800
FPS = 60


def init_board(width: int, height: int) -> Board:
    game_area_rect = pygame.Rect(0, 0, width, (height / 3) * 2)
    ui_area_rect = pygame.Rect(0, (height / 3) * 2, width, height / 3)
    return Board(width, height, game_area_rect, ui_area_rect)


def init_screen(width: int, height: int) -> pygame.Surface:
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("BUFFET BOT LOW BUDGET")
    return screen


def init_player(board: Board) -> Player:
    player_width, player_height = 30, 30
    initial_x = board.game_area_rect.centerx - player_width // 2
    initial_y = board.game_area_rect.centery - player_height // 2
    return Player(initial_x, initial_y, player_width, player_height, board.game_area_rect)


def init_controlUI(board: Board) -> ControlUI:
    return ControlUI(board.ui_area_rect)


def run_gameloop(board: Board, player: Player, clock: pygame.time.Clock, screen: pygame.Surface,
                 control_ui: ControlUI, tables: list) -> None:
    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if player:
            player.update(keys, tables)  # ✅ FIX: pass tables to player

        # Draw game elements
        board.draw(screen)
        for table in tables:
            table.draw(screen)
        if player:
            player.draw(screen)
        control_ui.draw(screen)

        pygame.display.flip()


def main():
    pygame.init()
    screen = init_screen(WIDTH, HEIGHT)
    board = init_board(WIDTH, HEIGHT)
    player = init_player(board)
    controlUI = init_controlUI(board)
    clock = pygame.time.Clock()

    # Create tables
    cell_size = 50
    tables = [
        Table((4, 3), cell_size),
        Table((8, 5), cell_size),
        Table((12, 7), cell_size)
    ]

    run_gameloop(board, player, clock, screen, controlUI, tables)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
