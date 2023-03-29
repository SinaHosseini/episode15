import random
import arcade
from snake import Snake
from fruit import Apple
from fruit import Pear
from fruit import Shit


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=480, height=480, title="Super Snake 🐍 V1")
        arcade.set_background_color(arcade.color.KHAKI)
        self.background = arcade.load_texture("GreenCheckeredGrassBoard.jpg")
        self.apple = Apple(self)
        self.snake = Snake(self)
        self.fruit_counter = "apple"
        self.status = "normal"
        self.game_over_bg = arcade.load_texture(
            "episode14\photo_2023-03-23_21-50-37.jpg")

    def on_draw(self):
        arcade.start_render()

        if self.status == "normal":
            arcade.draw_lrwh_rectangle_textured(
                0, 0, self.width, self.height, self.background)
            self.apple.draw()
            self.snake.draw()
            score_text = f"Score: {self.snake.score}"
            arcade.draw_text(score_text, self.width - 100,
                             20, arcade.color.WHITE, 15)

        elif self.status == "game over":
            arcade.draw_lrwh_rectangle_textured(
                0, 0, self.width, self.height, self.game_over_bg)

        arcade.finish_render()

    def on_update(self, delta_time):

        if self.snake.center_x < self.apple.center_x:
            self.snake.change_x = 1
            self.snake.change_y = 0
            self.snake.move()

        elif self.snake.center_x > self.apple.center_x:
            self.snake.change_x = -1
            self.snake.change_y = 0
            self.snake.move()

        if self.snake.center_y < self.apple.center_y:
            self.snake.change_x = 0
            self.snake.change_y = 1
            self.snake.move()

        elif self.snake.center_y > self.apple.center_y:
            self.snake.change_x = 0
            self.snake.change_y = -1
            self.snake.move()

        if arcade.check_for_collision(self.snake, self.apple):
            self.fruit_counter = "apple"
            self.snake.eat(self)
            self.apple = Apple(self)

        if self.snake.center_x == 5 or self.snake.center_x == self.width - 5 or self.snake.center_y == 5 or self.snake.center_y == self.height - 5:
            self.status = "game over"
            self.on_draw()

        if self.snake.score == -1:
            self.status = "game over"
            self.on_draw()


if __name__ == "__main__":
    game = Game()
    arcade.run()
