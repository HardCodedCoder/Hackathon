import pygame
import sys
import random
from enum import Enum
from board import Board
from player import Player
from controlUI import ControlUI
from tables import Table 
from buffet import Buffet
from AnimatedSprite import AnimatedSprite

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

def init_player(board: Board):
    """
    Initializes the player at the center of the game area.
    :param board: Board-Object holding the board data relevant for calculation
    """
    player = AnimatedSprite("assets/player/Prototype_Character.png", 32, 32, board.game_area_rect, pos=(board.game_area_rect.width / 2, board.game_area_rect.height - 100))
    all_sprites = pygame.sprite.Group(player)
    return all_sprites

def init_controlUI(board: Board) -> ControlUI:
    control_ui = ControlUI(board.ui_area_rect)
    return control_ui

def init_buffets(board: Board, tables: list, player_rect: pygame.Rect) -> list:
    """
    Initializes buffets on the board.
    The number of buffets equals the number of BuffetFood enum elements.
    Each buffet is placed at a random position within the game area.
    The position is re-rolled until the buffet does not collide with any table, 
    the player's starting rectangle, or any previously placed buffet.
    """
    buffets = []
    buffet_width, buffet_height = 100, 100
    game_area = board.game_area_rect
    max_attempts = 100

    for food in BuffetFood:
        attempts = 0
        valid = False
        while not valid and attempts < max_attempts:
            # Generate a random rectangle within the game area.
            x = random.randint(game_area.left, game_area.right - buffet_width)
            y = random.randint(game_area.top, game_area.bottom - buffet_height)
            buffet_rect = pygame.Rect(x, y, buffet_width, buffet_height)

            # Assume valid until any collision is detected.
            valid = True

            # Check collision with tables.
            for table in tables:
                if table.collides_with(buffet_rect.inflate(25,25)):
                    valid = False
                    break

            # Check collision with the player's starting rectangle.
            if player_rect.colliderect(buffet_rect):
                valid = False

            # Check collision with already placed buffets.
            if valid:  # Only check if still valid so far.
                for other_buffet in buffets:
                    if other_buffet.collides_with(buffet_rect.inflate(25,25)):
                        valid = False
                        break

            attempts += 1

        # If valid or reached the max_attempts (using last tried position), add the buffet.
        buffets.append(Buffet(buffet_rect, food.value))
    return buffets


def run_gameloop(board: Board, player: AnimatedSprite, clock: pygame.time.Clock, 
                 screen: pygame.Surface, control_ui: ControlUI, 
                 buffets: list, tables: list) -> None:
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        # Get the single player sprite from the group.
        player_sprite = player.sprites()[0]
        if player_sprite:
            prev_pos = player_sprite.rect.topleft
            # Pass both tables and buffets to update().
            player_sprite.update(keys, tables, buffets)
            # Clear error message when movement happens.
            if keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d]:
                control_ui.error_message = ""
                control_ui.success_message = ""
            elif player_sprite.rect.topleft != prev_pos:
                control_ui.error_message = ""
                control_ui.success_message = ""

        # Interaction check when pressing "E"
        if keys[pygame.K_e]:
            # If the player is not carrying food, check buffet interactions.
            if not hasattr(player_sprite, 'carrying_food') or player_sprite.carrying_food is None:
                for buffet in buffets:
                    # Use an inflated collision rectangle so that near-collision is enough.
                    if buffet.collides_with(player_sprite.rect.inflate(10, 10)):
                        if not buffet.taken:
                            if buffet.food == control_ui.food_ordered:
                                # Successful pickup.
                                player_sprite.carrying_food = buffet.food
                                player_sprite.origin_buffet = buffet
                                buffet.taken = True
                                control_ui.error_message = ""
                            else:
                                control_ui.error_message = "Wrong food!"
                        break  # Process only one buffet per interact press.
            else:
                # Player is carrying food; check table interactions.
                for table in tables:
                    if table.collides_with(player_sprite.rect.inflate(10, 10)):
                        # Verify that this is the target table (compare table numbers).
                        # Assuming control_ui.table is a string and table.table_number is an integer.
                        if table.table_number == int(control_ui.table):
                            # Deposit the food.
                            player_sprite.carrying_food = None
                            if hasattr(player_sprite, 'origin_buffet') and player_sprite.origin_buffet:
                                # Reset the buffet color by marking it not taken.
                                player_sprite.origin_buffet.taken = False
                            player_sprite.origin_buffet = None
                            # Change the ordered food to a new random one.
                            # Set a success message.
                            control_ui.success_message = "Food delivered!"
                            control_ui.score += 1
                            new_order = random.choice(list(BuffetFood)).value
                            control_ui.food_ordered = new_order
                            # Change the target table to a new random table number.
                            new_table = random.choice(tables).table_number
                            control_ui.table = str(new_table)
                            control_ui.error_message = ""
                        else:
                            control_ui.error_message = "Wrong table!"
                        break  # Process one table interaction per press.

        # Draw the game objects.
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
    player_group = init_player(board)  # player_group is a pygame.sprite.Group containing your player
    controlUI = init_controlUI(board)
    clock = pygame.time.Clock()

    cell_size = 50
    tables = [
        Table((4, 3), cell_size, table_number=1),
        Table((8, 5), cell_size, table_number=2),
        Table((12, 7), cell_size, table_number=3)
    ]

    # Get the player's starting rectangle.
    player_sprite = player_group.sprites()[0]
    player_start_rect = player_sprite.rect
    player_sprite.carrying_food = None
    player_sprite.origin_buffet = None
    
    # Now initialize buffets so that they do not intersect tables or the player's starting area.
    buffets = init_buffets(board, tables, player_start_rect)

    # Randomly choose a table number based on the number of tables.
    table_number = random.randint(1, len(tables))
    controlUI.table = str(table_number)
    
    # Randomly select an ordered food from BuffetFood.
    ordered_food = random.choice(list(BuffetFood)).value
    controlUI.food_ordered = ordered_food

    run_gameloop(board=board, player=player_group, clock=clock, screen=screen, 
                 control_ui=controlUI, buffets=buffets, tables=tables)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
