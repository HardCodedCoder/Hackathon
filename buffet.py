import pygame

class Buffet:
    # Mapping food names to their icon asset paths.
    FOOD_ICONS = {
        "Pizza": "assets/food/pizza.png",
        "Vegetarian": "assets/food/gemuse.png",
        "Dessert": "assets/food/dessert.png",
        "Steak": "assets/food/steak.png"
    }

    def __init__(self, rect: pygame.Rect, food: str):
        """
        Initializes the Buffet with a rectangle area and the food item available.
        
        :param rect: pygame.Rect that defines the area for the buffet.
        :param food: The food item available at the buffet.
        """
        self.rect = rect
        self.food = food
        self.taken = False

        self.icon = None
        # Try loading the icon corresponding to this food.
        if food in Buffet.FOOD_ICONS:
            try:
                self.icon = pygame.image.load(Buffet.FOOD_ICONS[food]).convert_alpha()
                # Scale the icon to fit inside the buffet rectangle with some padding.
                icon_padding = 10
                icon_width = max(1, self.rect.width - 2 * icon_padding)
                icon_height = max(1, self.rect.height - 2 * icon_padding)
                self.icon = pygame.transform.smoothscale(self.icon, (icon_width, icon_height))
            except Exception as e:
                print(f"Could not load icon for {food}: {e}")
                self.icon = None

    def draw(self, screen: pygame.Surface):
        """
        Draws the buffet on the screen.
        The buffet is drawn as a rectangle (yellow if available, dark yellow if food has been taken).
        Then, the corresponding icon (if loaded) is drawn centered on the buffet.
        
        :param screen: The pygame.Surface to draw on.
        """
        # Choose color based on whether the food is still available.
        color = (255, 255, 0) if not self.taken else (150, 150, 0)
        pygame.draw.rect(screen, color, self.rect)
        
        # If an icon was loaded, draw it; otherwise, display the food name.
        if self.icon:
            icon_rect = self.icon.get_rect(center=self.rect.center)
            screen.blit(self.icon, icon_rect)
        else:
            font = pygame.font.SysFont(None, 24)
            food_surface = font.render(self.food, True, (0, 0, 0))
            food_rect = food_surface.get_rect(center=self.rect.center)
            screen.blit(food_surface, food_rect)

    def collides_with(self, rect: pygame.Rect) -> bool:
        """
        Checks for collision between the buffet and the given rectangle.
        
        :param rect: A pygame.Rect to check collision with.
        :return: True if the rectangles collide, False otherwise.
        """
        return self.rect.colliderect(rect)
