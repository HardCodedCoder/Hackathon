import pygame

class Buffet:
    def __init__(self, rect: pygame.Rect, food: str):
        """
        Initializes the Buffet with a rectangle area and the food item available.
        
        :param rect: pygame.Rect that defines the area for the buffet.
        :param food: The food item available at the buffet.
        """
        self.rect = rect
        self.food = food
        self.taken = False

    def draw(self, screen: pygame.Surface):
        """
        Draws the buffet on the screen.
        The buffet is drawn as a rectangle (yellow if available, dark yellow if food has been taken).
        
        :param screen: The pygame.Surface to draw on.
        """
        # Choose color based on whether the food is still available
        color = (255, 255, 0) if not self.taken else (150, 150, 0)
        pygame.draw.rect(screen, color, self.rect)
        
        # Optionally, display the food name centered on the buffet
        font = pygame.font.SysFont(None, 24)
        food_surface = font.render(self.food, True, (0, 0, 0))
        food_rect = food_surface.get_rect(center=self.rect.center)
        screen.blit(food_surface, food_rect)
