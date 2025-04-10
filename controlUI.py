import pygame

class ControlUI:
    FONT_SIZE = 24
    FONT_COLOR = (255, 255, 255)  # Weiß
    
    def __init__(self, ui_rect: pygame.Rect):
        """
        Initialisiert das ControlUI mit dem gegebenen UI-Bereich.
        
        :param ui_rect: pygame.Rect, der den UI-Bereich definiert.
        """
        self.ui_rect = ui_rect
        self.font = pygame.font.SysFont(None, self.FONT_SIZE)
    
    def draw(self, screen: pygame.Surface):
        """
        Zeichnet die Steuerungselemente im UI-Bereich.
        Hier wird z. B. ein Text mit den Steuerungsinformationen angezeigt.
        
        :param screen: Die pygame.Surface, auf der der Text gezeichnet wird.
        """
        # Beispieltext: Steuerungshinweise
        text = "Controls: W - Up | A - Left | S - Down | D - Right"
        rendered_text = self.font.render(text, True, self.FONT_COLOR)
        # Zentriere den Text im UI-Bereich
        text_rect = rendered_text.get_rect(center=self.ui_rect.center)
        screen.blit(rendered_text, text_rect)
