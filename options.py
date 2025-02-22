class options:
    def __init__(self):
        self.screen_caption = "Ball Breakers"
        self.screen_color = (0,0,0)
        self.screen_width = 800
        self.screen_height = 600

        self.player_color = (0,255,0)
        self.player_width = 200
        self.player_height = 15
        self.player_x = (self.screen_width / 2) - (self.player_width / 2)
        self.player_y = self.screen_height - (self.player_height * 2)
        self.player_speed = 5

        self.ball_color = (0,0,255)
        self.ball_x = self.screen_width / 2
        self.ball_y = self.screen_height / 2
        self.ball_radius = 10
        self.ball_speed_x = 3
        self.ball_speed_y = 3
