import random
import arcade


class Apple(arcade.Sprite):
    def __init__(self, game):
        super().__init__("apple.png")
        self.width = 20
        self.height = 20
        self.center_x = random.randint(10, game.width - 10)
        self.center_y = random.randint(10, game.height - 10)


class Snake(arcade.Sprite):
    def __init__(self, game):
        super().__init__()
        self.width = 30
        self.height = 30
        self.center_x = game.width // 2
        self.center_y = game.width // 2
        self.color = arcade.color.GREEN
        self.change_x = 0
        self.change_y = 0
        self.speed = 4

    def draw(self):
        arcade.draw_rectangle_filled(
            self.center_x, self.center_y, self.width, self.height, self.color)

    def move(self):
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=480, height=480, title="Super Snake 🐍 V1")
        arcade.set_background_color(arcade.color.KHAKI)
        self.food = Apple(self)
        self.snake = Snake(self)

    def on_draw(self):
        arcade.start_render()
        self.food.draw()
        self.snake.draw()

        arcade.finish_render()

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.UP:
            self.snake.change_x = 0
            self.snake.change_y = 1

        elif symbol == arcade.key.DOWN:
            self.snake.change_x = 0
            self.snake.change_y = -1

        elif symbol == arcade.key.LEFT:
            self.snake.change_x = -1
            self.snake.change_y = 0

        elif symbol == arcade.key.RIGHT:
            self.snake.change_x = 1
            self.snake.change_y = 0

    def on_update(self, delta_time):
        self.snake.move()


if __name__ == "__main__":
    game = Game()
    arcade.run()
