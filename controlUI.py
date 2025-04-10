import pygame

class ControlUI:
    FONT_SIZE = 40
    FONT_COLOR = (255, 255, 255)  # white

    def __init__(self, ui_rect: pygame.Rect):
        """
        Initializes the ControlUI in the given area.
        
        :param ui_rect: pygame.Rect, defines the UI area.
        """
        self.ui_rect = ui_rect
        self.font = pygame.font.SysFont(None, self.FONT_SIZE)
        
        self.score = 0
        self.table = "-"
        self.food_ordered = "-"
        self.error_message = ""  # New attribute for error display
        
        # define the control keys with the corresponding key icon
        self.controls = [
            ("Move left", "assets/controls/keyboard_key_a.png"),
            ("Move right", "assets/controls/keyboard_key_d.png"),
            ("Move up", "assets/controls/keyboard_key_w.png"),
            ("Move down", "assets/controls/keyboard_key_s.png"),
            ("Interact", "assets/controls/keyboard_key_e.png")
        ]
        
        # pre-load and scale the icons
        self.control_items = []
        for label, icon_path in self.controls:
            try:
                icon_image = pygame.image.load(icon_path).convert_alpha()
                icon_image = pygame.transform.scale(icon_image, (self.FONT_SIZE, self.FONT_SIZE))
            except Exception as e:
                print(f"Error loading {icon_path}: {e}")
                icon_image = None
            self.control_items.append((label, icon_image))
    
    def draw(self, screen: pygame.Surface):
        """
        Draws the control UI in the UI area with formatted text and icons.
        The control texts are drawn horizontally next to each other,
        and each corresponding control icon is placed directly below its text.
        Also, the dynamic texts (score, table, food ordered) are drawn in the top-right.
        If an error message exists, it is drawn in red in the center of the UI area.
        
        :param screen: The pygame.Surface to draw on.
        """
        padding = 10
        gap_between_text_and_icon = 5
        horizontal_spacing = 30  # spacing between control items
        
        # Draw control items (left side)
        current_x = self.ui_rect.left + padding
        top_y = self.ui_rect.top + padding
        for label, icon in self.control_items:
            label_surface = self.font.render(label, True, self.FONT_COLOR)
            label_rect = label_surface.get_rect(topleft=(current_x, top_y))
            screen.blit(label_surface, label_rect)
            
            if icon is not None:
                icon_rect = icon.get_rect(midtop=(label_rect.centerx, label_rect.bottom + gap_between_text_and_icon))
                screen.blit(icon, icon_rect)
            
            element_width = max(label_rect.width, self.FONT_SIZE)
            current_x += element_width + horizontal_spacing

        # Draw dynamic texts (top-right)
        score_text = f"Score: {self.score}"
        table_text = f"Table: {self.table}"
        food_text = f"Food ordered: {self.food_ordered}"
        
        score_surface = self.font.render(score_text, True, self.FONT_COLOR)
        table_surface = self.font.render(table_text, True, self.FONT_COLOR)
        food_surface = self.font.render(food_text, True, self.FONT_COLOR)
        
        current_y_right = self.ui_rect.top + padding
        
        score_rect = score_surface.get_rect(topright=(self.ui_rect.right - padding, current_y_right))
        screen.blit(score_surface, score_rect)
        
        current_y_right = score_rect.bottom + 5
        table_rect = table_surface.get_rect(topright=(self.ui_rect.right - padding, current_y_right))
        screen.blit(table_surface, table_rect)
        
        current_y_right = table_rect.bottom + 5
        food_rect = food_surface.get_rect(topright=(self.ui_rect.right - padding, current_y_right))
        screen.blit(food_surface, food_rect)

        # Draw the error message, if any, centered in the UI area.
        if self.error_message:
            error_surface = self.font.render(self.error_message, True, (255, 0, 0))  # red color for error
            error_rect = error_surface.get_rect(center=self.ui_rect.center)
            screen.blit(error_surface, error_rect)
