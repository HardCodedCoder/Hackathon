import pygame


class Table:
    COLOR = (139, 69, 19)

    def __init__(self, grid_pos, cell_size):
        self.grid_pos = grid_pos
        self.cell_size = cell_size
        self.width = cell_size * 2
        self.height = cell_size
        self.rect = pygame.Rect(
            grid_pos[0] * cell_size,
            grid_pos[1] * cell_size,
            self.width,
            self.height
        )

    def draw(self, screen):
        pygame.draw.rect(screen, self.COLOR, self.rect)
        font = pygame.font.SysFont(None, 24)
        text = font.render("Table", True, (255, 255, 255))
        screen.blit(text, (self.rect.x + 10, self.rect.y + 10))

    def get_blocking_pos(self):
        return [
            (self.grid_pos[0] + 1, self.grid_pos[1]),
            (self.grid_pos[0] + 1, self.grid_pos[1])
        ]

    def collides_with(self, rect: pygame.Rect) -> bool:
        return self.rect.colliderect(rect)
