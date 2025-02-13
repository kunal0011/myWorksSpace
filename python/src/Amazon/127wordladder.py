"""
LeetCode 127. Word Ladder

Problem Statement:
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence
of words beginWord -> s1 -> s2 -> ... -> sk such that:
- Every adjacent pair of words differs by a single letter
- Every si for 1 <= i <= k must be in wordList
- Note that beginWord does not need to be in wordList
- sk == endWord

Given two words (beginWord and endWord), and a dictionary's word list, return the number of words in
the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

Example 1:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
which is 5 words long.

Example 2:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, so no transformation sequence exists.

Constraints:
- 1 <= beginWord.length <= 10
- endWord.length == beginWord.length
- 1 <= wordList.length <= 5000
- wordList[i].length == beginWord.length
- beginWord, endWord, and wordList[i] consist of lowercase English letters
- beginWord != endWord
- All the words in wordList are unique
"""

from collections import defaultdict, deque
from typing import List, Set, Dict, Tuple


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        BFS approach with pattern matching.
        Time complexity: O(N * M * 26) where N is length of wordList and M is length of each word
        Space complexity: O(N * M)
        """
        # If endWord is not in wordList, no transformation sequence exists
        if endWord not in wordList:
            return 0

        # Create pattern to word mapping
        # e.g., "hot" -> "*ot", "h*t", "ho*"
        pattern_to_words = defaultdict(list)
        word_length = len(beginWord)

        # Add beginWord patterns
        for i in range(word_length):
            pattern = beginWord[:i] + '*' + beginWord[i+1:]
            pattern_to_words[pattern].append(beginWord)

        # Add wordList patterns
        for word in wordList:
            for i in range(word_length):
                pattern = word[:i] + '*' + word[i+1:]
                pattern_to_words[pattern].append(word)

        # BFS
        queue = deque([(beginWord, 1)])
        visited = {beginWord}

        while queue:
            current_word, level = queue.popleft()

            # Try all possible patterns for current word
            for i in range(word_length):
                pattern = current_word[:i] + '*' + current_word[i+1:]

                # Check all words that match this pattern
                for next_word in pattern_to_words[pattern]:
                    if next_word == endWord:
                        return level + 1

                    if next_word not in visited:
                        visited.add(next_word)
                        queue.append((next_word, level + 1))

                # Clear the list of words for this pattern as we've processed them
                pattern_to_words[pattern] = []

        return 0

    def ladderLengthWithPath(self, beginWord: str, endWord: str,
                             wordList: List[str]) -> Tuple[int, List[str]]:
        """
        BFS approach that also returns the transformation sequence.
        Time complexity: O(N * M * 26)
        Space complexity: O(N * M)
        """
        if endWord not in wordList:
            return 0, []

        # Create pattern to word mapping
        pattern_to_words = defaultdict(list)
        word_length = len(beginWord)

        for word in [beginWord] + wordList:
            for i in range(word_length):
                pattern = word[:i] + '*' + word[i+1:]
                pattern_to_words[pattern].append(word)

        # BFS with path tracking
        queue = deque([(beginWord, [beginWord])])
        visited = {beginWord}

        while queue:
            current_word, path = queue.popleft()

            for i in range(word_length):
                pattern = current_word[:i] + '*' + current_word[i+1:]

                for next_word in pattern_to_words[pattern]:
                    if next_word == endWord:
                        return len(path) + 1, path + [endWord]

                    if next_word not in visited:
                        visited.add(next_word)
                        queue.append((next_word, path + [next_word]))

        return 0, []


def visualize_transformation(path: List[str]) -> None:
    """Helper function to visualize word transformation sequence"""
    if not path:
        print("No transformation sequence exists.")
        return

    word_length = len(path[0])

    for i in range(len(path) - 1):
        current_word = path[i]
        next_word = path[i + 1]

        # Find the differing position
        diff_pos = next(j for j in range(word_length)
                        if current_word[j] != next_word[j])

        # Create visualization
        print(f"Step {i + 1}: {current_word} -> {next_word}")
        print("Change:", end=" ")
        for j in range(word_length):
            if j == diff_pos:
                print(f"[{current_word[j]}->{next_word[j]}]", end=" ")
            else:
                print(f" {current_word[j]} ", end=" ")
        print("\n")


def test_word_ladder():
    solution = Solution()

    test_cases = [
        {
            "beginWord": "hit",
            "endWord": "cog",
            "wordList": ["hot", "dot", "dog", "lot", "log", "cog"],
            "expected": 5,
            "description": "Standard case with solution"
        },
        {
            "beginWord": "hit",
            "endWord": "cog",
            "wordList": ["hot", "dot", "dog", "lot", "log"],
            "expected": 0,
            "description": "No solution (endWord not in wordList)"
        },
        {
            "beginWord": "log",
            "endWord": "dog",
            "wordList": ["dog"],
            "expected": 2,
            "description": "Direct transformation"
        },
        {
            "beginWord": "hit",
            "endWord": "hat",
            "wordList": ["hot", "hat"],
            "expected": 2,
            "description": "Short transformation"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        beginWord = test_case["beginWord"]
        endWord = test_case["endWord"]
        wordList = test_case["wordList"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nTest case {i}: {description}")
        print(f"Begin word: {beginWord}")
        print(f"End word: {endWord}")
        print(f"Word list: {wordList}")

        # Test both implementations
        result1 = solution.ladderLength(beginWord, endWord, wordList)
        length, path = solution.ladderLengthWithPath(
            beginWord, endWord, wordList)

        if path:
            print("\nTransformation sequence:")
            visualize_transformation(path)
            print(f"Sequence length: {length}")
        else:
            print("\nNo valid transformation sequence exists.")

        assert result1 == expected and length == expected, \
            f"Expected {expected}, but got {result1} (basic), {length} (with path)"
        print("✓ Test case passed!")


if __name__ == "__main__":
    test_word_ladder()
    print("\nAll test cases passed! 🎉")
