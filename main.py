import pygame
import sys
from board import Board
from AnimatedSprite import AnimatedSprite
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

def init_player(board: Board):
    """
    Initializes the player at the center of the game area.
    :param board: Board-Object holding the board data relevant for calculation
    """
    player = AnimatedSprite("/Users/ginovalentinopensuni/Library/Mobile Documents/com~apple~CloudDocs/Hackathon/assets/player/Prototype_Character.png", 32, 32, pos=(board.game_area_rect.width / 2, board.game_area_rect.height / 2))
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

def run_gameloop(board: Board, player: pygame.sprite.Group, clock: pygame.time.Clock, screen: pygame.Surface, control_ui: ControlUI) -> None:
    running = True
    while running:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # Zeichne das Board und den Spieler
        
        board.draw(screen)
        keys = pygame.key.get_pressed()
        moving = False
        
        # Da 'player' eine Sprite-Gruppe ist, holen wir uns das erste Sprite
        player_sprite = player.sprites()[0]
        
        if keys[pygame.K_LEFT]:
            player_sprite.set_direction("left")
            player_sprite.rect.x -= 5
            moving = True
        elif keys[pygame.K_RIGHT]:
            player_sprite.set_direction("right")
            player_sprite.rect.x += 5
            moving = True
        elif keys[pygame.K_UP]:
            player_sprite.set_direction("up")
            player_sprite.rect.y -= 5
            moving = True
        elif keys[pygame.K_DOWN]:
            player_sprite.set_direction("down")
            player_sprite.rect.y += 5
            moving = True

        # Aktualisiere alle Sprites in der Gruppe (übergibt 'moving' als Argument)
        player.update(moving)
        screen.fill((30,30,30))
        player.draw(screen)
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