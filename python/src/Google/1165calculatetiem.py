"""
LeetCode 1165: Single-Row Keyboard

Problem Statement:
There is a special keyboard with all keys in a single row. Given a string keyboard of length 26 indicating
the layout of the keyboard (indexed from 0 to 25), initially your finger is at index 0.
To type a character, you have to move your finger to the index of the desired character.
The time taken to move your finger from index i to index j is |i - j|.
You want to type a string word. Write a function to calculate how much time it takes to type it.

Logic:
1. Create a dictionary mapping each character to its position in keyboard
2. Track current finger position (starts at 0)
3. For each character in word:
   - Calculate absolute distance from current position
   - Update current position
4. Return total time (sum of all moves)

Time Complexity: O(n) where n is length of word
Space Complexity: O(1) since keyboard is fixed size 26
"""


class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        position = {char: i for i, char in enumerate(keyboard)}
        total_time = 0
        current_position = 0

        for char in word:
            total_time += abs(position[char] - current_position)
            current_position = position[char]

        return total_time


def test_calculate_time():
    solution = Solution()

    # Test case 1: Basic case
    keyboard1 = "abcdefghijklmnopqrstuvwxyz"
    word1 = "cba"
    result1 = solution.calculateTime(keyboard1, word1)
    assert result1 == 4, f"Test case 1 failed. Expected 4, got {result1}"
    print(f"Test case 1 passed: moves = {result1}")

    # Test case 2: Same character repeated
    keyboard2 = "abcdefghijklmnopqrstuvwxyz"
    word2 = "aaa"
    result2 = solution.calculateTime(keyboard2, word2)
    assert result2 == 0, f"Test case 2 failed. Expected 0, got {result2}"
    print(f"\nTest case 2 passed: moves = {result2}")

    # Test case 3: Custom keyboard layout
    keyboard3 = "zyxwvutsrqponmlkjihgfedcba"
    word3 = "abc"
    result3 = solution.calculateTime(keyboard3, word3)
    assert result3 == 50, f"Test case 3 failed. Expected 50, got {result3}"
    print(f"\nTest case 3 passed: moves = {result3}")

    # Test case 4: Single character
    keyboard4 = "abcdefghijklmnopqrstuvwxyz"
    word4 = "z"
    result4 = solution.calculateTime(keyboard4, word4)
    assert result4 == 25, f"Test case 4 failed. Expected 25, got {result4}"
    print(f"\nTest case 4 passed: moves = {result4}")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_calculate_time()
