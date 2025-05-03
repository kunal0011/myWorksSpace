"""
LeetCode 353 - Design Snake Game

Design a Snake game that is played on a device with screen size = width x height.
The snake is initially positioned at the top left corner (0,0) with length = 1 unit.

You are given a list of food positions in row-column order. When a snake eats the food,
its length and the game's score both increase by 1.

Each food appears one by one on the screen. For example, the second food will not
appear until the first food was eaten by the snake.

The game is over if the snake goes out of bounds or if it moves onto itself.

Implement the SnakeGame class:
- SnakeGame(int width, int height) Initializes the object with screen width = width and height = height
- int move(String direction) Returns the score after applying one direction move by the snake
"""
from collections import deque
import random


class SnakeGame:
    def __init__(self, width: int, height: int):
        """Initialize your data structure here.
        @param width - screen width
        @param height - screen height
        """
        self.width = width
        self.height = height
        self.snake = deque([(0, 0)])  # Initial snake position
        self.snake_set = set([(0, 0)])  # For O(1) collision checks
        self.food = self._place_food()
        self.directions = {'U': (-1, 0), 'D': (1, 0),
                           'L': (0, -1), 'R': (0, 1)}

    def _place_food(self) -> tuple:
        """Places food at random location not occupied by snake.
        @return tuple: (row, col) coordinates of food
        """
        while True:
            food = (random.randint(0, self.height - 1),
                    random.randint(0, self.width - 1))
            if food not in self.snake_set:
                return food

    def move(self, direction: str) -> int:
        """Moves the snake in the given direction.
        @param direction: 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        @return: The game's score after the move (-1 if game over)
        """
        head_x, head_y = self.snake[0]
        move_x, move_y = self.directions[direction]
        new_head = (head_x + move_x, head_y + move_y)

        # Check if new head is out of bounds or collides with the snake itself
        if (new_head[0] < 0 or new_head[0] >= self.height or
            new_head[1] < 0 or new_head[1] >= self.width or
                new_head in self.snake_set):
            return -1  # Game over

        # Check if new head is on food
        if new_head == self.food:
            self.snake.appendleft(new_head)  # Grow the snake
            self.snake_set.add(new_head)
            self.food = self._place_food()  # Place new food
            return 1  # Food eaten

        # Move the snake
        tail = self.snake.pop()  # Remove the tail
        self.snake_set.remove(tail)  # Remove from set

        self.snake.appendleft(new_head)  # Add new head
        self.snake_set.add(new_head)  # Add to set

        return 0  # Move successful


def test_snake_game():
    """Test driver for the Snake Game implementation"""
    # Test Case 1: Basic movement
    print("Test Case 1: Basic movement")
    game = SnakeGame(4, 4)
    print(f"Initial state: Snake at {list(game.snake)}, Food at {game.food}")

    moves = ['R', 'D', 'R', 'U', 'L']
    for move in moves:
        result = game.move(move)
        print(f"Move {move}: Score = {result}, Snake at {list(game.snake)}")

    # Test Case 2: Growing snake
    print("\nTest Case 2: Growing snake")
    game = SnakeGame(3, 3)
    food_reached = 0
    moves = ['D', 'D', 'R', 'U', 'U', 'L']
    for move in moves:
        result = game.move(move)
        if result > food_reached:
            food_reached = result
        print(f"Move {move}: Score = {result}, Snake length = {len(game.snake)}")

    # Test Case 3: Game over scenarios
    print("\nTest Case 3: Game over scenarios")
    game = SnakeGame(2, 2)
    moves = ['R', 'D', 'L', 'U', 'R']  # Should cause collision
    for move in moves:
        result = game.move(move)
        print(f"Move {move}: {'Game Over' if result == -1 else 'Score = ' + str(result)}")


if __name__ == "__main__":
    test_snake_game()
