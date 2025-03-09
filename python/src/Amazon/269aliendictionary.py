"""
LeetCode 269 - Alien Dictionary (Hard)

There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. 
You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. 
Derive the order of letters in this language.

Example 1:
Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"

Example 2:
Input: words = ["z","x"]
Output: "zx"

Example 3:
Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".

Logic:
1. Create a graph where each vertex is a character and edge a->b means 'a' comes before 'b'
2. Build graph by comparing adjacent words character by character
3. Use Kahn's algorithm (topological sort) to find the order
4. Handle edge cases:
   - If word2 is prefix of word1, return "" (invalid)
   - If graph has cycle, return "" (invalid)
"""

from collections import defaultdict, deque


class Solution:
    def alienOrder(self, words: list[str]) -> str:
        # Step 1: Create a graph (adjacency list) and indegree dictionary
        graph = defaultdict(list)
        indegree = {char: 0 for word in words for char in word}

        # Step 2: Build the graph by comparing consecutive words
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            min_length = min(len(word1), len(word2))

            # Check if word2 is a prefix of word1
            if len(word1) > len(word2) and word1[:min_length] == word2[:min_length]:
                return ""

            # Compare characters to determine the ordering
            for j in range(min_length):
                if word1[j] != word2[j]:
                    graph[word1[j]].append(word2[j])
                    indegree[word2[j]] += 1
                    break

        # Step 3: Perform topological sort using BFS (Kahn's Algorithm)
        queue = deque([char for char in indegree if indegree[char] == 0])
        order = []

        while queue:
            char = queue.popleft()
            order.append(char)

            for neighbor in graph[char]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 4: Check if we have a valid topological order (no cycles)
        if len(order) == len(indegree):
            return ''.join(order)
        else:
            return ""


def test_alien_dictionary():
    """Test cases for alien dictionary problem"""
    solution = Solution()
    
    # Test case 1: Normal case
    assert solution.alienOrder(["wrt","wrf","er","ett","rftt"]) == "wertf", "Test case 1 failed"
    
    # Test case 2: Simple two-letter case
    assert solution.alienOrder(["z","x"]) == "zx", "Test case 2 failed"
    
    # Test case 3: Invalid order (cycle)
    assert solution.alienOrder(["z","x","z"]) == "", "Test case 3 failed"
    
    # Test case 4: Prefix case
    assert solution.alienOrder(["abc","ab"]) == "", "Test case 4 failed"
    
    # Test case 5: Single letter different positions
    assert solution.alienOrder(["ac","ab","zc"]) in ["azc", "zac"], "Test case 5 failed"
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_alien_dictionary()
