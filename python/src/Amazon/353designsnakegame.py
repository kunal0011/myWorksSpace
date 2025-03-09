"""
LeetCode 353: Design Snake Game

Problem Statement:
Design a Snake game that is played on a device with screen size height x width. The snake starts at position (0,0) 
and moves in one of 4 directions: up (U), left (L), right (R), or down (D). The game objective is to collect as 
much food as possible. When the snake eats the food, its body grows longer. The snake game ends when:
1. The snake bites its own body, or
2. The snake hits the screen boundaries

Each piece of food appears at a fixed point on the screen. For example, food = [[1,2], [0,1]] means the first 
food is at position (1,2), the second is at position (0,1).

Example:
Given width = 3, height = 2, and food = [[1,2],[0,1]]
Snake snake = new Snake(width, height, food);
snake.move("R"); -> Returns 0
snake.move("D"); -> Returns 0
snake.move("R"); -> Returns 1 (Snake eats the first food)
snake.move("U"); -> Returns 1
snake.move("L"); -> Returns 2 (Snake eats the second food)
snake.move("U"); -> Returns -1 (Game over because snake hits border)

Logic:
1. Use a deque to store snake body positions
   - Head is at index 0
   - Tail is at last index
2. Use a set to efficiently check for body collisions
3. For each move:
   - Calculate new head position
   - Check for wall collision
   - Check for self collision
   - Check for food
   - If food found:
     * Increment score and food index
     * Don't remove tail (snake grows)
   - If no food:
     * Remove tail from both deque and set
   - Add new head to both deque and set
4. Return -1 for game over, otherwise return current score
"""

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


def run_test_cases():
    # Test case 1: Example from problem statement
    print("Test case 1: Basic game flow")
    game1 = SnakeGame(3, 2, [[1,2], [0,1]])
    moves1 = ["R", "D", "R", "U", "L", "U"]
    expected1 = [0, 0, 1, 1, 2, -1]
    
    for i, move in enumerate(moves1):
        result = game1.move(move)
        print(f"Move {i+1}: {move}")
        print(f"Expected: {expected1[i]}")
        print(f"Got: {result}")
        print(f"Pass? {result == expected1[i]}\n")
    
    # Test case 2: Snake growing and self collision
    print("\nTest case 2: Snake growing and self collision")
    game2 = SnakeGame(3, 3, [[0,1], [0,2], [1,2], [1,1]])
    moves2 = ["R", "R", "D", "L", "L"]  # Snake will collide with itself
    expected2 = [1, 2, 3, 4, -1]
    
    for i, move in enumerate(moves2):
        result = game2.move(move)
        print(f"Move {i+1}: {move}")
        print(f"Expected: {expected2[i]}")
        print(f"Got: {result}")
        print(f"Pass? {result == expected2[i]}\n")
    
    # Test case 3: Wall collision
    print("\nTest case 3: Wall collision")
    game3 = SnakeGame(2, 2, [[0,1]])
    moves3 = ["R", "U", "U"]  # Snake will hit the wall
    expected3 = [1, 1, -1]
    
    for i, move in enumerate(moves3):
        result = game3.move(move)
        print(f"Move {i+1}: {move}")
        print(f"Expected: {expected3[i]}")
        print(f"Got: {result}")
        print(f"Pass? {result == expected3[i]}\n")
    
    # Test case 4: No food
    print("\nTest case 4: Moving without food")
    game4 = SnakeGame(3, 3, [])
    moves4 = ["R", "R", "D"]  # No food to eat
    expected4 = [0, 0, 0]
    
    for i, move in enumerate(moves4):
        result = game4.move(move)
        print(f"Move {i+1}: {move}")
        print(f"Expected: {expected4[i]}")
        print(f"Got: {result}")
        print(f"Pass? {result == expected4[i]}\n")
    
    # Test case 5: Invalid move
    print("\nTest case 5: Invalid move")
    game5 = SnakeGame(2, 2, [[0,1]])
    result = game5.move("X")  # Invalid direction
    print(f"Move: X")
    print(f"Expected: -1")
    print(f"Got: {result}")
    print(f"Pass? {result == -1}")


if __name__ == "__main__":
    run_test_cases()
