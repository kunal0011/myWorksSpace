from collections import deque
from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(string):
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        queue = deque([s])
        visited = set([s])
        found = False
        result = []

        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                current = queue.popleft()

                if is_valid(current):
                    result.append(current)
                    found = True

                if found:
                    continue

                # Generate all possible states by removing one parenthesis
                for i in range(len(current)):
                    if current[i] not in '()':
                        continue
                    next_state = current[:i] + current[i+1:]
                    if next_state not in visited:
                        visited.add(next_state)
                        queue.append(next_state)

            if found:
                break

        return result
