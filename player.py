import pygame


class Player:
    COLOR = (255, 0, 0)  # Rot
    SPEED = 5  # Geschwindigkeit in Pixeln pro Frame

    def __init__(self, x: int, y: int, width: int, height: int, boundary_rect: pygame.Rect):
        """
        Initializes the player setting its start position and size. s
        :param x: Anfangs-x-Koordinate
        :param y: Anfangs-y-Koordinate
        :param width: Breite des Spieler-Rechtecks
        :param height: Höhe des Spieler-Rechtecks
        :param boundary_rect: Bereich (z. B. das Spielfeld), in dem sich der Spieler bewegen darf
        """
        self.rect = pygame.Rect(x, y, width, height)
        self.boundary_rect = boundary_rect

    def update(self, keys: dict, tables: list):
        original_position = self.rect.copy()

        if keys[pygame.K_w]:
            self.rect.y -= self.SPEED
        if keys[pygame.K_s]:
            self.rect.y += self.SPEED
        if keys[pygame.K_a]:
            self.rect.x -= self.SPEED
        if keys[pygame.K_d]:
            self.rect.x += self.SPEED

        # Prevent leaving board
        if self.rect.left < self.boundary_rect.left:
            self.rect.left = self.boundary_rect.left
        if self.rect.right > self.boundary_rect.right:
            self.rect.right = self.boundary_rect.right
        if self.rect.top < self.boundary_rect.top:
            self.rect.top = self.boundary_rect.top
        if self.rect.bottom > self.boundary_rect.bottom:
            self.rect.bottom = self.boundary_rect.bottom

        # Ask each table if the player collided
        for table in tables:
            if table.collides_with(self.rect):
                self.rect = original_position
                break

    def draw(self, screen: pygame.Surface):
        """Zeichnet den Spieler als Rechteck auf den Bildschirm."""
        pygame.draw.rect(screen, self.COLOR, self.rect)
