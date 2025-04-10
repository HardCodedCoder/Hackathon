import pygame

class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet_path, frame_width, frame_height, boundary_rect, pos=(0, 0), zoom=3):
        super().__init__()
        # Load the spritesheet
        self.spritesheet = pygame.image.load(sheet_path).convert_alpha()
        
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.zoom = zoom  # Factor to scale the sprite frames
        self.pos = pos
        self.boundary_rect = boundary_rect
        
        # Get the overall size of the spritesheet
        sheet_rect = self.spritesheet.get_rect()
        self.sheet_width, self.sheet_height = sheet_rect.size
        
        # Calculate the number of columns and rows in the sheet
        self.columns = self.sheet_width // self.frame_width
        self.rows = self.sheet_height // self.frame_height
        
        # We assume the rows are ordered as follows:
        # Row 0: "down", Row 1: "left", Row 2: "right", Row 3: "up"
        self.directions = ['down', 'right', 'up', 'left']
        self.animations = {}
        
        # Extract frames for each direction
        for row in range(self.rows):
            if row < len(self.directions):
                direction = self.directions[row]
                frames = []
                for col in range(self.columns):
                    x = col * self.frame_width
                    y = row * self.frame_height
                    frame_rect = pygame.Rect(x, y, self.frame_width, self.frame_height)
                    frame_image = pygame.Surface((self.frame_width, self.frame_height), pygame.SRCALPHA)
                    frame_image.blit(self.spritesheet, (0, 0), frame_rect)
                    # Apply zoom scaling if necessary
                    if zoom != 1:
                        new_width = int(self.frame_width * zoom)
                        new_height = int(self.frame_height * zoom)
                        frame_image = pygame.transform.scale(frame_image, (new_width, new_height))
                    frames.append(frame_image)
                self.animations[direction] = frames
        
        # Initial state: default to "down"
        self.current_direction = 'down'
        self.frames = self.animations[self.current_direction]
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect(topleft=self.pos)
        
        # Animation settings
        self.animation_speed = 1000  # in milliseconds per frame
        self.last_update = pygame.time.get_ticks()

    def set_direction(self, direction):
        """
        Switches the animation based on the given direction.
        """
        if direction in self.animations and direction != self.current_direction:
            self.current_direction = direction
            self.frames = self.animations[self.current_direction]
            self.current_frame = 0
            self.last_update = pygame.time.get_ticks()
            self.image = self.frames[self.current_frame]

    def update(self, keys: dict, tables=list, buffets=list):
        """
        Updates the animation.
        Animation frame updates occur only when 'moving' is True.
        If 'moving' is False, the first frame of the current animation is displayed.
        """
        now = pygame.time.get_ticks()
        
        original_position = self.rect.copy()
        
        if keys[pygame.K_LEFT]:
            self.set_direction("left")
            self.rect.x -= 5
        elif keys[pygame.K_RIGHT]:
            self.set_direction("right")
            self.rect.x += 5
        elif keys[pygame.K_UP]:
            self.set_direction("up")
            self.rect.y -= 5
        elif keys[pygame.K_DOWN]:
            self.set_direction("down")
            self.rect.y += 5
            
        if now - self.last_update > self.animation_speed:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]

        # Prevent leaving board boundaries.
        if self.rect.left < self.boundary_rect.left:
            self.rect.left = self.boundary_rect.left
        if self.rect.right > self.boundary_rect.right:
            self.rect.right = self.boundary_rect.right
        if self.rect.top < self.boundary_rect.top:
            self.rect.top = self.boundary_rect.top
        if self.rect.bottom > self.boundary_rect.bottom:
            self.rect.bottom = self.boundary_rect.bottom

        # Check collision with tables.
        for table in tables:
            if table.collides_with(self.rect.inflate(-70, -70)):
                self.rect = original_position
                print("collision table")
                break

        # Check collision with buffets.
        for buffet in buffets:
            # We block movement if colliding with a buffet that hasn't been taken.
            if buffet.collides_with(self.rect.inflate(-70, -70)) and not buffet.taken:
                self.rect = original_position
                print("collision buffet")
                break
