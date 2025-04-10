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
    """
    Initializes the game board with a specific size and layout.
    :return: Board-Object
    """

    game_area_rect = pygame.Rect(0, 0, width, (height / 3) * 2)
    ui_area_rect = pygame.Rect(0, (height / 3) * 2, width, height / 3)

    board = Board(width, height, game_area_rect, ui_area_rect)
    return board

def init_screen(width: int, height: int) -> pygame.Surface:
    """
    Initializes the screen with a specific size.
    :return: pygame.Surface-Object
    """
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("BUFFET BOT LOW BUDGET")
    return screen

def init_player(board: Board) -> Player:
    """
    Initializes the player at the center of the game area.
    :param board: Board-Object holding the board data relevant for calculation
    """
    player_width, player_height = 30, 30
    initial_x = board.game_area_rect.centerx - player_width // 2
    initial_y = board.game_area_rect.centery - player_height // 2
    player = Player(initial_x, initial_y, player_width, player_height, board.game_area_rect)
    return player

def init_controlUI(board: Board) -> ControlUI:
    """
    Initializes the control UI.
    :return: ControlUI
    """
    
    # Create the control UI in the bottom of the screen
    control_ui = ControlUI(board.ui_area_rect)
    return control_ui

def run_gameloop(board: Board, player: Player, clock: pygame.time.Clock, screen: pygame.Surface, control_ui: ControlUI) -> None:
    running = True
    while running:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Check 
        keys = pygame.key.get_pressed()
        if (player is not None):
            player.update(keys)

        # Zeichne das Board und den Spieler
        
        board.draw(screen)
        if (player is not None):
            player.draw(screen)
        control_ui.draw(screen)
        
        pygame.display.flip()

def main():
    pygame.init()
    screen = init_screen(width = WIDTH, height = HEIGHT)
    board = init_board(width=WIDTH,height=HEIGHT)
    player = init_player(board=board)
    controlUI = init_controlUI(board=board)
    
    clock = pygame.time.Clock()
    
    # Create tables
    cell_size = 40
    tables = [
        Table((10, 5), cell_size),
        Table((12, 6), cell_size),
        Table((14, 7), cell_size)
    ]
    for table in tables:
        table.draw(screen)
    
    # main game loop
    run_gameloop(board=board, player=player, clock=clock, screen=screen, control_ui=controlUI)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()