"""
LeetCode 243 - Shortest Word Distance

Problem Statement:
Given an array of strings wordsDict and two different strings word1 and word2 that are in wordsDict,
return the shortest distance between these two words in the array. The distance between two words is
the minimum number of steps required to go from one word to another in the array.

Solution Logic:
1. Keep track of latest indices for both words
2. Update indices as we scan through array
3. When either word is found, calculate minimum distance
4. Time: O(n), Space: O(1)
"""

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

def test_shortest_distance():
    solution = Solution()
    
    # Test Case 1: Basic case
    words1 = ["practice", "makes", "perfect", "coding", "makes"]
    print("Test 1: Basic case")
    print(f"Array: {words1}")
    print(f"Distance between 'coding' and 'practice': "
          f"{solution.shortestDistance(words1, 'coding', 'practice')}")  # Expected: 3
    
    # Test Case 2: Adjacent words
    words2 = ["a", "b", "c", "d"]
    print("\nTest 2: Adjacent words")
    print(f"Array: {words2}")
    print(f"Distance between 'a' and 'b': "
          f"{solution.shortestDistance(words2, 'a', 'b')}")  # Expected: 1
    
    # Test Case 3: Multiple occurrences
    words3 = ["a","c","b","a","b"]
    print("\nTest 3: Multiple occurrences")
    print(f"Array: {words3}")
    print(f"Distance between 'a' and 'b': "
          f"{solution.shortestDistance(words3, 'a', 'b')}")  # Expected: 1

if __name__ == "__main__":
    test_shortest_distance()
