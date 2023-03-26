import random
import arcade


class Apple(arcade.Sprite):
    def __init__(self, game):
        super().__init__("apple.png")
        self.width = 20
        self.height = 20
        self.center_x = random.randint(10, game.width - 10)
        self.center_y = random.randint(10, game.height - 10)


class Pear(arcade.Sprite):
    def __init__(self, game):
        super().__init__("pear.png")
        self.width = 25
        self.height = 25
        self.center_x = random.randint(10, game.width - 10)
        self.center_y = random.randint(10, game.height - 10)


class Shit(arcade.Sprite):
    def __init__(self, game):
        super().__init__("poop.png")
        self.width = 20
        self.height = 20
        self.center_x = random.randint(10, game.width - 10)
        self.center_y = random.randint(10, game.height - 10)
