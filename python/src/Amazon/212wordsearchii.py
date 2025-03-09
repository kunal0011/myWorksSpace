"""
LeetCode 212 - Word Search II

Problem Statement:
Given an m x n board of characters and a list of strings words, return all words on the board.
Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells 
are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Solution Logic:
1. Build Trie from words list for efficient search
2. Use DFS with backtracking on board
3. Mark visited cells using '#' during traversal
4. Store found words in set to avoid duplicates
5. Time: O(M*N*4^L) where M,N=board dimensions, L=max word length
6. Space: O(sum of word lengths) for Trie
"""

from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # Store complete word at leaf nodes

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Build Trie
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word
        
        def dfs(row: int, col: int, node: TrieNode) -> None:
            # Check if we found a word
            if node.word:
                found_words.add(node.word)
                node.word = None  # Remove found word to avoid duplicates
            
            # Save original character and mark as visited
            if not (0 <= row < m and 0 <= col < n):
                return
            char = board[row][col]
            if char not in node.children:
                return
            
            board[row][col] = '#'  # Mark as visited
            
            # Check all four directions
            for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
                new_row, new_col = row + dx, col + dy
                if 0 <= new_row < m and 0 <= new_col < n and board[new_row][new_col] != '#':
                    dfs(new_row, new_col, node.children[char])
            
            board[row][col] = char  # Restore original character
        
        m, n = len(board), len(board[0])
        found_words = set()
        
        # Start DFS from each cell
        for i in range(m):
            for j in range(n):
                dfs(i, j, root)
                
        return list(found_words)

def test_word_search():
    solution = Solution()
    
    # Test Case 1: Basic case
    board1 = [
        ["o","a","a","n"],
        ["e","t","a","e"],
        ["i","h","k","r"],
        ["i","f","l","v"]
    ]
    words1 = ["oath","pea","eat","rain"]
    print("Test 1:")
    print("Board:", board1)
    print("Words:", words1)
    print("Found words:", solution.findWords(board1, words1))  # Expected: ["eat","oath"]
    
    # Test Case 2: No words found
    board2 = [["a","b"],["c","d"]]
    words2 = ["xyz"]
    print("\nTest 2:")
    print("Board:", board2)
    print("Words:", words2)
    print("Found words:", solution.findWords(board2, words2))  # Expected: []
    
    # Test Case 3: Single cell board
    board3 = [["a"]]
    words3 = ["a"]
    print("\nTest 3:")
    print("Board:", board3)
    print("Words:", words3)
    print("Found words:", solution.findWords(board3, words3))  # Expected: ["a"]

if __name__ == "__main__":
    test_word_search()
