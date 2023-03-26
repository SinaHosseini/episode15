import arcade


class Snake(arcade.Sprite):
    def __init__(self, game):
        super().__init__()
        self.width = 25
        self.height = 25
        self.center_x = game.width // 2
        self.center_y = game.width // 2
        self.color = arcade.color.DARK_GREEN
        self.change_x = 0
        self.change_y = 0
        self.speed = 3
        self.score = 0
        self.body = []

    def draw(self):
        arcade.draw_rectangle_filled(
            self.center_x, self.center_y, self.width, self.height, self.color)
        if self.score % 2 == 0:
            for part in self.body:
                arcade.draw_rectangle_filled(
                    part['x'], part['y'], self.width, self.height, arcade.color.DARK_GREEN)

        elif self.score % 2 == 1:
            for part in self.body:
                arcade.draw_rectangle_filled(
                    part['x'], part['y'], self.width, self.height, arcade.color.GREEN)

    def move(self):
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed
        self.body.append({'x': self.center_x, 'y': self.center_y})
        if len(self.body) > self.score + 1:
            self.body.pop(0)

    def eat(self, game):
        if game.fruit_counter == "apple":
            del game.apple
            self.score += 1

        elif game.fruit_counter == "pear":
            del game.pear
            self.score += 2
