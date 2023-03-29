import arcade


class Snake(arcade.Sprite):
    def __init__(self, game):
        super().__init__()
        self.width = 25
        self.height = 25
        self.center_x = game.width // 2
        self.center_y = game.width // 2
        self.color1 = arcade.color.DARK_GREEN
        self.color2 = arcade.color.GREEN
        self.change_x = 0
        self.change_y = 0
        self.speed = 4
        self.score = 0
        self.body = []

    def draw(self):
        arcade.draw_rectangle_filled(
            self.center_x, self.center_y, self.width, self.height, self.color1)
        counter = 0
        for part in self.body:
            if counter % 2 == 0:
                arcade.draw_rectangle_filled(
                    part['x'], part['y'], self.width, self.height, self.color2)

            elif counter % 2 == 1:
                arcade.draw_rectangle_filled(
                    part['x'], part['y'], self.width, self.height, self.color1)
            counter += 1

    def move(self):
        self.body.append({'x': self.center_x, 'y': self.center_y})
        if len(self.body) > self.score + 1:
            self.body.pop(0)
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed

    def eat(self, game):
        if game.fruit_counter == "apple":
            del game.apple
            self.score += 1

        elif game.fruit_counter == "pear":
            del game.pear
            self.score += 2

        elif game.fruit_counter == "poop":
            del game.poop
            del game.apple
            self.score -= 1
