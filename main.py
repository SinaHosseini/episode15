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
        self.pear = Pear(self)
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
            if random.randint(1, 6) == 6:
                self.pear.draw()
            score_text = f"Score: {self.snake.score}"
            arcade.draw_text(score_text, self.width - 100,
                             20, arcade.color.WHITE, 15)

        elif self.status == "game over":
            arcade.draw_lrwh_rectangle_textured(
                0, 0, self.width, self.height, self.game_over_bg)

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

        if arcade.check_for_collision(self.snake, self.apple):
            self.fruit_counter = "apple"
            self.snake.eat(self)
            self.apple = Apple(self)


        if arcade.check_for_collision(self.snake, self.pear):
            self.fruit_counter = "pear"
            self.snake.eat(self)
            self.pear = Pear(self)

        if self.snake.score == -1:
            self.status = "game over"
            self.on_draw()


if __name__ == "__main__":
    game = Game()
    arcade.run()
