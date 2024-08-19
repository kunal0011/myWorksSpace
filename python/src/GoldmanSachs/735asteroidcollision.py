from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            # Process current asteroid
            while stack and asteroid < 0 < stack[-1]:
                # Check if a collision occurs
                if stack[-1] < -asteroid:
                    stack.pop()  # Destroy the top of the stack (right-moving asteroid)
                elif stack[-1] == -asteroid:
                    stack.pop()  # Both asteroids are of the same size, destroy both
                    break
                else:
                    break  # The right-moving asteroid is larger; the current asteroid is destroyed
            else:
                # If no collision occurs, add the current asteroid to the stack
                stack.append(asteroid)

        return stack
