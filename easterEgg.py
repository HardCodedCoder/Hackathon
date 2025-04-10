import pygame

class EasterEgg:
    def __init__(self, screen_width, screen_height, margin=50, speed=10):
        """
        Initializes the EasterEgg icon.
        
        :param screen_width: The width of the screen.
        :param screen_height: The height of the screen.
        :param margin: The margin from the screen edge when the icon is fully in.
        :param speed: The number of pixels the icon moves per update.
        """
        self.image = pygame.image.load("assets/hidden/easteregg.jpg").convert_alpha()
        self.rect = self.image.get_rect()
        self.screen_width = screen_width

        # Place the icon off-screen on the right (hidden initially)
        self.rect.left = screen_width
        self.rect.centery = (screen_height // 2) - 100

        # The target x position when the icon is shown.
        self.target_x = screen_width - self.rect.width - margin

        self.speed = speed
        self.visible = False  # Target state: False means hidden

    def toggle(self):
        """
        Toggles the target state for the Easter Egg.
        If currently hidden, it will start sliding in.
        If currently visible, it will start sliding out.
        """
        self.visible = not self.visible

    def update(self):
        """
        Update the icon's position by sliding it in or out based on the current target state.
        """
        # Slide in (if visible is True) until reaching target_x.
        if self.visible:
            if self.rect.left > self.target_x:
                self.rect.left -= self.speed
                # Avoid overshooting.
                if self.rect.left < self.target_x:
                    self.rect.left = self.target_x
        # Slide out (if visible is False) until completely off-screen (screen_width).
        else:
            if self.rect.left < self.screen_width:
                self.rect.left += self.speed
                # Avoid overshooting.
                if self.rect.left > self.screen_width:
                    self.rect.left = self.screen_width

    def draw(self, screen):
        """
        Draws the Easter Egg icon onto the provided screen.
        """
        screen.blit(self.image, self.rect)
