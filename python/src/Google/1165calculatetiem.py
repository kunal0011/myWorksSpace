class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        position = {char: i for i, char in enumerate(keyboard)}
        total_time = 0
        current_position = 0

        for char in word:
            total_time += abs(position[char] - current_position)
            current_position = position[char]

        return total_time
