from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        from collections import defaultdict
        fruit_count = defaultdict(int)
        start = 0
        max_fruits = 0

        for end in range(len(fruits)):
            # Add the current fruit to the window
            fruit_count[fruits[end]] += 1

            # If we have more than two types of fruits, shrink the window from the left
            while len(fruit_count) > 2:
                fruit_count[fruits[start]] -= 1
                if fruit_count[fruits[start]] == 0:
                    del fruit_count[fruits[start]]
                start += 1

            # Update the maximum number of fruits we can collect
            max_fruits = max(max_fruits, end - start + 1)

        return max_fruits
