"""
LeetCode 388 - Longest Absolute File Path

Problem Statement:
Suppose we have a file system that stores both files and directories. Given a string input representing the file system in the format of a n-ary tree structure:
- The string contains newline characters '\n'
- A directory name consists of letters, digits, and/or spaces
- A file name consists of letters, digits, spaces, and a dot '.'
- Each directory and file begins with a tab character '\t' to indicate its depth. More tabs means deeper level.

Return the length of the longest absolute path to a file in the file system. If there is no file in the input, return 0.

Example:
Input: "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
Output: 20
Explanation: We have only one file and its path is: dir/subdir2/file.ext, length = 20

Time Complexity: O(n), where n is the length of the input string
Space Complexity: O(d), where d is the maximum depth of the file system
"""

class Solution:
    def lengthLongestPath(self, input: str) -> int:
        # Dictionary to store path lengths at each depth
        path_len = {-1: 0}  # Initialize with depth -1 to handle root
        max_len = 0
        
        # Split input into lines and process each
        for line in input.split('\n'):
            # Count depth by number of tabs
            depth = line.count('\t')
            # Remove tabs to get actual name
            name = line.replace('\t', '')
            
            # If it's a file (contains a dot)
            if '.' in name:
                # Calculate current path length:
                # Previous path length + current name length + depth (for '/' separators)
                curr_len = path_len[depth-1] + len(name)
                max_len = max(max_len, curr_len)
            else:
                # For directory, store its path length for next level
                path_len[depth] = path_len[depth-1] + len(name) + 1  # +1 for '/'
        
        return max_len


def test_longest_file_path():
    solution = Solution()
    
    # Test cases
    test_cases = [
        (
            "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext",
            20  # dir/subdir2/file.ext
        ),
        (
            "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext",
            32  # dir/subdir2/subsubdir2/file2.ext
        ),
        (
            "a",
            0   # No file in the input
        ),
        (
            "file1.txt\nfile2.txt\nlongfile.txt",
            12  # longfile.txt
        ),
        (
            "dir\n    file.txt",
            12  # dir/file.txt
        )
    ]
    
    for i, (input_str, expected) in enumerate(test_cases, 1):
        result = solution.lengthLongestPath(input_str)
        print(f"Test case {i}:")
        print(f"Input:")
        print(input_str)
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"Pass: {result == expected}\n")


if __name__ == "__main__":
    test_longest_file_path()