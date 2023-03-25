import random
import arcade
from snake import Snake
from fruite import Apple


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
        score_text = f"Score: {self.snake.score}"
        arcade.draw_text(score_text, self.width - 100,
                         20, arcade.color.WHITE, 15)

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

        if arcade.check_for_collision(self.snake, self.food):
            self.snake.eat(self.food)
            self.food = Apple(self)


if __name__ == "__main__":
    game = Game()
    arcade.run()
