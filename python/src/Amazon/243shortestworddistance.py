from typing import List


class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        index1, index2 = -1, -1  # Store the latest indices of word1 and word2
        min_distance = float('inf')  # Initialize with a large number

        for i, word in enumerate(wordsDict):
            if word == word1:
                index1 = i  # Update the index for word1
            elif word == word2:
                index2 = i  # Update the index for word2

            # If both words have been seen at least once, calculate the distance
            if index1 != -1 and index2 != -1:
                min_distance = min(min_distance, abs(index1 - index2))

        return min_distance

# Example usage:
# solution = Solution()
# wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
# word1 = "coding"
# word2 = "practice"
# print(solution.shortestDistance(wordsDict, word1, word2))  # Output: 3
