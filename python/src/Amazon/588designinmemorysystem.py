"""
LeetCode 588 - Design In-Memory File System

Design a data structure that simulates an in-memory file system.

Implement the FileSystem class:
- FileSystem() Initializes the object of the system.
- List<String> ls(String path)
  * If path is a file path, returns a list containing only this file's name.
  * If path is a directory path, returns the list of file and directory names in this directory.
  * The answer should be in lexicographic order.
- void mkdir(String path) Makes a new directory according to the given path. The given directory path does not exist.
  If the middle directories in the path do not exist, you should create them as well.
- void addContentToFile(String filePath, String content)
  * If filePath does not exist, creates that file containing given content.
  * If filePath already exists, appends the given content to original content.
- String readContentFromFile(String filePath) Returns the content in the file at filePath.

Example:
Input: 
["FileSystem", "ls", "mkdir", "addContentToFile", "ls", "readContentFromFile"]
[[], ["/"], ["/a/b/c"], ["/a/b/c/d", "hello"], ["/"], ["/a/b/c/d"]]
Output:
[null, [], null, null, ["a"], "hello"]

Constraints:
- 1 <= path.length, filePath.length <= 100
- path and filePath are absolute paths which begin with '/' and do not end with '/' except that the path is just "/"
- You can assume that all directory names and file names only contain lowercase letters, and the same names will not exist in the same directory
- You can assume that all operations will be passed valid parameters
- 1 <= content.length <= 50
- At most 300 calls will be made to ls, mkdir, addContentToFile, and readContentFromFile
"""

from typing import List
from collections import defaultdict


class FileSystem:
    class Node:
        def __init__(self):
            self.children = defaultdict(FileSystem.Node)  # For directories
            self.content = ""  # For files
            self.is_file = False

    def __init__(self):
        """
        Initialize your data structure here.
        Using a Trie-like structure for efficient path traversal
        """
        self.root = self.Node()

    def ls(self, path: str) -> List[str]:
        """
        Returns list of files and directories in lexicographic order
        Time Complexity: O(m + nlogn) where m is path length and n is number of entries
        """
        node = self._traverse_path(path)
        
        # If it's a file, return just the file name
        if node.is_file:
            return [path.split('/')[-1]]
            
        # If it's a directory, return sorted list of all entries
        return sorted(node.children.keys())

    def mkdir(self, path: str) -> None:
        """
        Creates a directory path
        Time Complexity: O(m) where m is path length
        """
        self._traverse_path(path)

    def addContentToFile(self, filePath: str, content: str) -> None:
        """
        Add/append content to file
        Time Complexity: O(m + k) where m is path length and k is content length
        """
        node = self._traverse_path(filePath)
        node.is_file = True
        node.content += content

    def readContentFromFile(self, filePath: str) -> str:
        """
        Read file content
        Time Complexity: O(m) where m is path length
        """
        node = self._traverse_path(filePath)
        return node.content

    def _traverse_path(self, path: str) -> Node:
        """Helper method to traverse/create path and return final node"""
        node = self.root
        
        # Handle root path
        if path == "/":
            return node
            
        # Split path and traverse/create nodes
        for part in path.split('/')[1:]:
            node = node.children[part]
            
        return node


def test_file_system():
    """
    Test function with comprehensive test cases
    """
    def print_test_result(test_num: int, operation: str, args: list, expected: any, result: any):
        print(f"\nTest {test_num}: {operation}{args}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        if expected == result:
            print("✅ Test passed!")
        else:
            print("❌ Test failed!")

    # Test Case 1: Basic operations
    print("\nTest Case 1: Basic Operations")
    fs = FileSystem()
    
    # Test empty root directory
    result = fs.ls("/")
    print_test_result(1, "ls", ["/"], [], result)
    
    # Test mkdir
    fs.mkdir("/a/b/c")
    result = fs.ls("/")
    print_test_result(2, "ls", ["/"], ["a"], result)
    
    # Test add content to file
    fs.addContentToFile("/a/b/c/d", "hello")
    result = fs.ls("/a/b/c")
    print_test_result(3, "ls", ["/a/b/c"], ["d"], result)
    
    # Test read content
    result = fs.readContentFromFile("/a/b/c/d")
    print_test_result(4, "readContentFromFile", ["/a/b/c/d"], "hello", result)

    # Test Case 2: Complex directory structure
    print("\nTest Case 2: Complex Directory Structure")
    fs2 = FileSystem()
    
    # Create multiple directories
    fs2.mkdir("/a")
    fs2.mkdir("/b")
    fs2.mkdir("/c")
    result = fs2.ls("/")
    print_test_result(5, "ls", ["/"], ["a", "b", "c"], result)
    
    # Create nested structure
    fs2.mkdir("/a/a1")
    fs2.mkdir("/a/a2")
    fs2.addContentToFile("/a/file1", "content1")
    result = fs2.ls("/a")
    print_test_result(6, "ls", ["/a"], ["a1", "a2", "file1"], result)

    # Test Case 3: File operations
    print("\nTest Case 3: File Operations")
    fs3 = FileSystem()
    
    # Test file creation and appending
    fs3.addContentToFile("/file1", "Hello")
    fs3.addContentToFile("/file1", " World")
    result = fs3.readContentFromFile("/file1")
    print_test_result(7, "readContentFromFile", ["/file1"], "Hello World", result)
    
    # Test file in directory
    fs3.mkdir("/dir")
    fs3.addContentToFile("/dir/file2", "Content2")
    result = fs3.readContentFromFile("/dir/file2")
    print_test_result(8, "readContentFromFile", ["/dir/file2"], "Content2", result)

    # Test Case 4: Edge cases
    print("\nTest Case 4: Edge Cases")
    fs4 = FileSystem()
    
    # Empty directory
    fs4.mkdir("/empty")
    result = fs4.ls("/empty")
    print_test_result(9, "ls", ["/empty"], [], result)
    
    # Single character names
    fs4.mkdir("/a")
    fs4.addContentToFile("/a/b", "c")
    result = fs4.ls("/a")
    print_test_result(10, "ls", ["/a"], ["b"], result)
    
    # Deep directory structure
    fs4.mkdir("/1/2/3/4/5")
    result = fs4.ls("/1/2/3/4")
    print_test_result(11, "ls", ["/1/2/3/4"], ["5"], result)


if __name__ == "__main__":
    test_file_system()