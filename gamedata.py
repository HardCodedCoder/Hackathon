class GameData:
    def __init__(self):
        self.player = None
        self.tables = []
        self.buffetTables = []
        self.score = 0
        self.game_over = False

    def reset(self):
        self.player = None
        self.tables.clear()
        self.buffetTables.clear()
        self.level = 1
        self.score = 0
        self.game_over = False

    def update_score(self, points):
        self.score += points

    def set_game_over(self):
        self.game_over = True