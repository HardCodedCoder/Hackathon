import pygame
import sys
import random
from enum import Enum
from board import Board
from player import Player
from controlUI import ControlUI
from tables import Table 
from buffet import Buffet

WIDTH = 1200
HEIGHT = 800
FPS = 60

class BuffetFood(Enum):
    PIZZA = "Pizza"
    VEGETARIAN = "Vegetarian"
    DESSERT = "Dessert"
    STEAK = "Steak"

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
    control_ui = ControlUI(board.ui_area_rect)
    return control_ui

def init_buffets(board: Board) -> list:
    """
    Initializes buffets on the board.
    The number of buffets equals the number of BuffetFood enum elements.
    Each buffet is placed at a random position within the game area.
    """
    buffets = []
    buffet_width, buffet_height = 100, 100
    game_area = board.game_area_rect
    for food in BuffetFood:
        x = random.randint(game_area.left, game_area.right - buffet_width)
        y = random.randint(game_area.top, game_area.bottom - buffet_height)
        buffet_rect = pygame.Rect(x, y, buffet_width, buffet_height)
        buffets.append(Buffet(buffet_rect, food.value))
    return buffets

def run_gameloop(board: Board, player: Player, clock: pygame.time.Clock, 
                 screen: pygame.Surface, control_ui: ControlUI, 
                 buffets: list, tables: list) -> None:
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if player:
            prev_pos = player.rect.topleft
            # Now pass both tables and buffets to update().
            player.update(keys, tables, buffets)
            # Clear error message if movement keys are pressed or if player's position changed.
            if keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d]:
                control_ui.error_message = ""
            elif player.rect.topleft != prev_pos:
                control_ui.error_message = ""

        # Check for buffet interaction (when player presses "E")
        if keys[pygame.K_e]:
            for buffet in buffets:
                if player.rect.colliderect(buffet.rect.inflate(20, 20)):
                    if not buffet.taken:
                        if buffet.food == control_ui.food_ordered:
                            buffet.taken = True
                            control_ui.score += 1
                        else:
                            control_ui.error_message = "Wrong food!"
                    break  # process one buffet per interact press

        # Draw all objects.
        board.draw(screen)
        for table in tables:
            table.draw(screen)
        for buffet in buffets:
            buffet.draw(screen)
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

    cell_size = 50
    tables = [
        Table((4, 3), cell_size),
        Table((8, 5), cell_size),
        Table((12, 7), cell_size)
    ]

    buffets = init_buffets(board)

    # Randomly choose a table number based on the number of tables.
    table_number = random.randint(1, len(tables))
    controlUI.table = str(table_number)
    
    # Randomly select an ordered food from BuffetFood.
    ordered_food = random.choice(list(BuffetFood)).value
    controlUI.food_ordered = ordered_food

    run_gameloop(board=board, player=player, clock=clock, screen=screen, 
                 control_ui=controlUI, buffets=buffets, tables=tables)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
