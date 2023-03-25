import random
import arcade


class Fruit(arcade.Sprite):
    def __init__(self, game):
        super().__init__("apple.png")
        self.width = 20
        self.height = 20
        self.center_x = random.randint(10, game.width - 10)
        self.center_y = random.randint(10, game.height - 10)


class Apple(Fruit):
    def __init__(self, game):
        super().__init__(game)
        self.width = 20
        self.height = 20
        self.center_x = random.randint(10, game.width - 10)
        self.center_y = random.randint(10, game.height - 10)


class Pear(Fruit):
    def __init__(self, game):
        super().__init__(game)
        self.width = 20
        self.height = 20
        self.center_x = random.randint(10, game.width - 10)
        self.center_y = random.randint(10, game.height - 10)


class Shit(Fruit):
    def __init__(self, game):
        super().__init__(game)
        self.width = 20
        self.height = 20
        self.center_x = random.randint(10, game.width - 10)
        self.center_y = random.randint(10, game.height - 10)
