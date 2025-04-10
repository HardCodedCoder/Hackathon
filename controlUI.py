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
        
        :param screen: The pygame.Surface to draw on.
        """
        padding = 10
        gap_between_text_and_icon = 5
        horizontal_spacing = 30  # spacing between control items
        
        # Start drawing the control texts from the top-left of the UI area
        current_x = self.ui_rect.left + padding
        top_y = self.ui_rect.top + padding
        
        # draw each control element
        for label, icon in self.control_items:
            # Render the control text
            label_surface = self.font.render(label, True, self.FONT_COLOR)
            label_rect = label_surface.get_rect(topleft=(current_x, top_y))
            screen.blit(label_surface, label_rect)
            
            # calculate the icon-rect, so the icon is centered directly below the text
            if icon is not None:
                icon_rect = icon.get_rect(midtop=(label_rect.centerx, label_rect.bottom + gap_between_text_and_icon))
                screen.blit(icon, icon_rect)
            
            # set current_x for the next control element. 
            # The width of the element is the max width of text and icon
            element_width = max(label_rect.width, self.FONT_SIZE)
            current_x += element_width + horizontal_spacing

        # dynamic texts in the top-right
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
