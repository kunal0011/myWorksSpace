class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True


class Solution:
    def __init__(self):
        self.result = set()
        self.trie = Trie()

    def findWords(self, board, words):
        # Insert all words into the Trie
        for word in words:
            self.trie.insert(word)

        # Initialize the board dimensions
        self.rows = len(board)
        self.cols = len(board[0])

        # Start DFS from each cell in the board
        for r in range(self.rows):
            for c in range(self.cols):
                self._dfs(board, r, c, "", self.trie.root)

        return list(self.result)

    def _dfs(self, board, row, col, path, node):
        # Boundary check and visited check
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols or board[row][col] == '#':
            return

        char = board[row][col]
        if char not in node.children:
            return

        # Move to the next node in the Trie
        node = node.children[char]
        path += char

        # Check if we found a word
        if node.is_end_of_word:
            self.result.add(path)

        # Mark the cell as visited
        board[row][col] = '#'

        # Explore neighbors in 4 directions
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_row, new_col = row + dr, col + dc
            self._dfs(board, new_row, new_col, path, node)

        # Unmark the cell (backtrack)
        board[row][col] = char
