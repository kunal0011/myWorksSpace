from collections import deque


class SnakeGame:

    def __init__(self, width: int, height: int, food: list[list[int]]):
        """
        Initialize the snake game.
        :param width: Width of the grid.
        :param height: Height of the grid.
        :param food: List of food positions.
        """
        self.width = width
        self.height = height
        self.food = food
        self.food_index = 0
        self.snake = deque([(0, 0)])  # Snake starts at the top-left corner
        # To track the body of the snake for collision
        self.snake_set = set([(0, 0)])
        self.score = 0

    def move(self, direction: str) -> int:
        """
        Move the snake in the given direction.
        :param direction: Direction can be 'U', 'L', 'R', 'D'.
        :return: The current score or -1 if game is over.
        """
        head_x, head_y = self.snake[0]

        # Calculate the new head position based on the direction
        if direction == "U":
            new_head = (head_x - 1, head_y)
        elif direction == "L":
            new_head = (head_x, head_y - 1)
        elif direction == "R":
            new_head = (head_x, head_y + 1)
        elif direction == "D":
            new_head = (head_x + 1, head_y)
        else:
            return -1

        new_x, new_y = new_head

        # Check if the new head position is out of bounds
        if not (0 <= new_x < self.height and 0 <= new_y < self.width):
            return -1  # Game over: out of bounds

        # Check if the snake collides with itself (excluding the tail since it will move)
        if new_head in self.snake_set and new_head != self.snake[-1]:
            return -1  # Game over: snake hits itself

        # Check if there's food at the new head position
        if self.food_index < len(self.food) and [new_x, new_y] == self.food[self.food_index]:
            # Snake eats food
            self.food_index += 1
            self.score += 1
        else:
            # Move the tail (snake didn't eat food)
            tail = self.snake.pop()
            self.snake_set.remove(tail)

        # Add the new head to the snake's body
        self.snake.appendleft(new_head)
        self.snake_set.add(new_head)

        return self.score


# Test the SnakeGame
if __name__ == "__main__":
    # Initialize the game with a grid and food positions
    game = SnakeGame(3, 3, [[1, 2], [0, 1]])

    # Test movements
    print(game.move("R"))  # Output: 0
    print(game.move("D"))  # Output: 0
    print(game.move("R"))  # Output: 1 (snake eats food)
    print(game.move("U"))  # Output: 1
    print(game.move("L"))  # Output: 2 (snake eats another food)
    print(game.move("U"))  # Output: -1 (game over: snake hits itself)
