from collections import deque
import random


class SnakeGame:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.snake = deque([(0, 0)])  # Initial snake position
        self.snake_set = set([(0, 0)])  # For O(1) collision checks
        self.food = self._place_food()
        self.directions = {'U': (-1, 0), 'D': (1, 0),
                           'L': (0, -1), 'R': (0, 1)}

    def _place_food(self):
        while True:
            food = (random.randint(0, self.height - 1),
                    random.randint(0, self.width - 1))
            if food not in self.snake_set:
                return food

    def move(self, direction: str) -> int:
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
