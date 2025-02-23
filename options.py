class options:
    def __init__(self):
        self.screen_caption = "Ball Breakers"
        self.screen_color = (0,0,0)
        self.screen_width = 800
        self.screen_height = 600

        self.player_color = (0,0,255)
        self.player_width = 100
        self.player_height = 15
        self.player_x = (self.screen_width / 2) - (self.player_width / 2)
        self.player_y = self.screen_height - (self.player_height * 2)
        self.player_speed = 5

        self.ball_color = (0,255,0)
        self.ball_radius = 10
        self.ball_speed_x = 3
        self.ball_speed_y = -3

        self.block_init_x = 10
        self.block_x = 10
        self.block_y = 10
        self.block_width = 50
        self.block_height = 20
        self.block_gap = 15
        self.block_rows = 5
        self.block_color_min = 128
        self.block_color_max = 255
