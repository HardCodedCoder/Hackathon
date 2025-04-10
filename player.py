import pygame

class Player:
    COLOR = (255, 0, 0)  # Red
    SPEED = 5  # pixels per frame

    def __init__(self, x: int, y: int, width: int, height: int, boundary_rect: pygame.Rect):
        """
        Initializes the player with its start position and size.
        :param x: initial x-coordinate
        :param y: initial y-coordinate
        :param width: player's width
        :param height: player's height
        :param boundary_rect: area in which the player is allowed to move
        """
        self.rect = pygame.Rect(x, y, width, height)
        self.boundary_rect = boundary_rect

    def update(self, keys: dict, tables: list, buffets: list):
        original_position = self.rect.copy()

        if keys[pygame.K_w]:
            self.rect.y -= self.SPEED
        if keys[pygame.K_s]:
            self.rect.y += self.SPEED
        if keys[pygame.K_a]:
            self.rect.x -= self.SPEED
        if keys[pygame.K_d]:
            self.rect.x += self.SPEED

        # Prevent leaving board boundaries.
        if self.rect.left < self.boundary_rect.left:
            self.rect.left = self.boundary_rect.left
        if self.rect.right > self.boundary_rect.right:
            self.rect.right = self.boundary_rect.right
        if self.rect.top < self.boundary_rect.top:
            self.rect.top = self.boundary_rect.top
        if self.rect.bottom > self.boundary_rect.bottom:
            self.rect.bottom = self.boundary_rect.bottom

        # Check collision with tables.
        for table in tables:
            if table.collides_with(self.rect):
                self.rect = original_position
                break

        # Check collision with buffets.
        for buffet in buffets:
            # We block movement if colliding with a buffet that hasn't been taken.
            if buffet.collides_with(self.rect) and not buffet.taken:
                self.rect = original_position
                break

    def draw(self, screen: pygame.Surface):
        """Draws the player as a rectangle on the screen."""
        pygame.draw.rect(screen, self.COLOR, self.rect)
