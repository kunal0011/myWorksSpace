"""
LeetCode 245 - Shortest Word Distance III

Problem Statement:
Given an array of strings wordsDict and two strings word1 and word2, return the shortest distance
between these two words in the array. Note that word1 and word2 may be the same. In this case,
we should return the shortest distance between two same words.

Solution Logic:
1. Similar to Shortest Word Distance I but handle same word case
2. Track latest indices for both words
3. When words are same:
   - Update distance only when finding second occurrence
   - Keep track of previous index
4. Time: O(n), Space: O(1)
"""

from typing import List


class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        index1, index2 = -1, -1
        min_distance = float('inf')
        same_word = (word1 == word2)

        for i, word in enumerate(wordsDict):
            if word == word1:
                if same_word:
                    if index1 != -1:
                        min_distance = min(min_distance, i - index1)
                    index1 = i
                else:
                    index1 = i
                    if index2 != -1:
                        min_distance = min(min_distance, abs(index1 - index2))

            elif word == word2:
                index2 = i
                if index1 != -1:
                    min_distance = min(min_distance, abs(index1 - index2))

        return min_distance


def test_shortest_word_distance():
    solution = Solution()
    
    # Test Case 1: Different words
    words1 = ["practice", "makes", "perfect", "coding", "makes"]
    print("Test 1: Different words")
    print(f"Array: {words1}")
    print(f"Distance between 'coding' and 'practice': "
          f"{solution.shortestWordDistance(words1, 'coding', 'practice')}")  # Expected: 3
    
    # Test Case 2: Same word
    words2 = ["practice", "makes", "practice", "coding", "practice"]
    print("\nTest 2: Same word")
    print(f"Array: {words2}")
    print(f"Distance between 'practice' and 'practice': "
          f"{solution.shortestWordDistance(words2, 'practice', 'practice')}")  # Expected: 2
    
    # Test Case 3: Adjacent occurrences
    words3 = ["a","a","b","b"]
    print("\nTest 3: Adjacent occurrences")
    print(f"Array: {words3}")
    print(f"Distance between 'a' and 'a': "
          f"{solution.shortestWordDistance(words3, 'a', 'a')}")  # Expected: 1

if __name__ == "__main__":
    test_shortest_word_distance()
