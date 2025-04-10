import pygame

class Table:
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

        self.image = pygame.image.load("assets/table/table_trimmed_final.png").convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (self.width, self.height))

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

    def get_blocking_pos(self):
        return [
            (self.grid_pos[0], self.grid_pos[1]),
            (self.grid_pos[0] + 1, self.grid_pos[1])
        ]

    def collides_with(self, rect: pygame.Rect) -> bool:
        return self.rect.colliderect(rect)
