import pygame
import sys
from board import Board
from AnimatedSprite import AnimatedSprite
from controlUI import ControlUI
from tables import Table 
from buffet import Buffet

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

def init_player(board: Board):
    """
    Initializes the player at the center of the game area.
    :param board: Board-Object holding the board data relevant for calculation
    """
    player = AnimatedSprite("assets/player/Prototype_Character.png", 32, 32, pos=(board.game_area_rect.width / 2, board.game_area_rect.height / 2))
    all_sprites = pygame.sprite.Group(player)
    return all_sprites
    
def init_controlUI(board: Board) -> ControlUI:
    """
    Initializes the control UI.
    :return: ControlUI
    """
    
    # Create the control UI in the bottom of the screen
    control_ui = ControlUI(board.ui_area_rect)
    return control_ui

def init_buffet(board: Board) -> Buffet:
    """
    Initializes the buffet on the right side of the game area.
    :param board: Board object
    :return: Buffet object with a given food item.
    """
    buffet_width, buffet_height = 100, 100
    # Position the buffet within the game area: 20px from the right edge with an offset from the top.
    buffet_x = board.game_area_rect.right - buffet_width - 20
    buffet_y = board.game_area_rect.top + 100
    buffet_rect = pygame.Rect(buffet_x, buffet_y, buffet_width, buffet_height)
    return Buffet(buffet_rect, "Pizza")

def run_gameloop(board: Board,  player: pygame.sprite.Group, clock: pygame.time.Clock, 
                 screen: pygame.Surface, control_ui: ControlUI, buffet: Buffet, tables: list) -> None:
    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if player:
            player.update(keys, tables)  # ✅ FIX: pass tables to player

        # Check for buffet interaction: if player collides with the buffet and presses "E"
        if keys[pygame.K_e] and player.rect.colliderect(buffet.rect) and not buffet.taken:
            buffet.taken = True
            control_ui.food_ordered = buffet.food
            # TODO: set player.carrying_food = buffet.food
            
        # draw the board and the player
        board.draw(screen)
        for table in tables:
            table.draw(screen)
        if player:
            player.draw(screen)
        control_ui.draw(screen)
        
        # Draw the buffet
        buffet.draw(screen)
        
        pygame.display.flip()


def main():
    pygame.init()
    screen = init_screen(width = WIDTH, height = HEIGHT)
    board = init_board(width=WIDTH,height=HEIGHT)
    player = init_player(board=board)
    controlUI = init_controlUI(board=board)
    buffet = init_buffet(board)
    
    clock = pygame.time.Clock()

    # Create tables
    cell_size = 50
    tables = [
        Table((4, 3), cell_size, table_number=1),
        Table((8, 5), cell_size, table_number=2),
        Table((12, 7), cell_size, table_number=3)
    ]
    for table in tables:
        table.draw(screen)
    
    # main game loop
    run_gameloop(board=board, player=player, clock=clock, screen=screen, control_ui=controlUI, buffet=buffet, tables=tables)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
