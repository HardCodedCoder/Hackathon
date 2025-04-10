import pygame

class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet_path, frame_width, frame_height, pos=(0, 0)):
        super().__init__()
        # Spritesheet laden
        self.spritesheet = pygame.image.load(sheet_path).convert_alpha()
        
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.pos = pos

        # Gesamtgröße des Spritesheets
        sheet_rect = self.spritesheet.get_rect()
        self.sheet_width, self.sheet_height = sheet_rect.size
        
        # Anzahl der Spalten und Zeilen im Sheet
        self.columns = self.sheet_width // self.frame_width
        self.rows = self.sheet_height // self.frame_height
        
        # Wir gehen davon aus, dass die Reihen in folgender Reihenfolge vorliegen:
        # Zeile 0: "down", Zeile 1: "left", Zeile 2: "right", Zeile 3: "up"
        self.directions = ['down', 'left', 'right', 'up']
        self.animations = {}
        
        # Frames jeweils für jede Richtung ausschneiden
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
                    frames.append(frame_image)
                self.animations[direction] = frames
        
        # Startzustand: Standardrichtung "down"
        self.current_direction = 'down'
        self.frames = self.animations[self.current_direction]
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect(topleft=self.pos)
        
        # Animationseinstellungen
        self.animation_speed = 150  # in Millisekunden pro Frame
        self.last_update = pygame.time.get_ticks()

    def set_direction(self, direction):
        """
        Wechselt die Animation basierend auf der übergebenen Richtung.
        """
        if direction in self.animations and direction != self.current_direction:
            self.current_direction = direction
            self.frames = self.animations[self.current_direction]
            self.current_frame = 0
            self.last_update = pygame.time.get_ticks()
            self.image = self.frames[self.current_frame]

    def update(self, moving=False):
        """
        Aktualisiert die Animation.
        Wird nur animiert (Frames wechseln), wenn moving True ist.
        Ist moving False, wird der erste Frame der aktuellen Animation angezeigt.
        """
        now = pygame.time.get_ticks()
        if moving:
            if now - self.last_update > self.animation_speed:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.frames)
                self.image = self.frames[self.current_frame]
        else:
            # Im Idle-Zustand einfach den ersten Frame anzeigen.
            self.current_frame = 0
            self.image = self.frames[self.current_frame]