import pygame

class Table:
    def __init__(self, grid_pos, cell_size, table_number=1):
        self.grid_pos = grid_pos
        self.cell_size = cell_size
        self.width = cell_size * 2
        self.height = cell_size
        self.table_number = table_number

        self.rect = pygame.Rect(
            grid_pos[0] * cell_size,
            grid_pos[1] * cell_size,
            self.width,
            self.height
        )

        self.image = pygame.image.load("assets/table/table_trimmed_final.png").convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (self.width, self.height))

        # Font for numbers (bigger + bold style)
        self.font = pygame.font.SysFont("Arial", 36, bold=True)

    def draw(self, screen):
        # Draw the table image
        screen.blit(self.image, self.rect.topleft)

        # Minimal number display (small, clean, subtle)
        font = pygame.font.SysFont("Arial", 20)
        number_str = str(self.table_number)
        text_color = (230, 230, 230)  # soft gray-white

        text = font.render(number_str, True, text_color)

        # Align below the table (or slightly lower inside it)
        text_rect = text.get_rect(center=(self.rect.centerx, self.rect.bottom - 10))
        screen.blit(text, text_rect)

    def get_blocking_pos(self):
        return [
            (self.grid_pos[0], self.grid_pos[1]),
            (self.grid_pos[0] + 1, self.grid_pos[1])
        ]

    def collides_with(self, rect: pygame.Rect) -> bool:
        return self.rect.colliderect(rect)
