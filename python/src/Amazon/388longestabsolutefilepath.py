"""
LeetCode 388: Longest Absolute File Path

Given a string input representing the file system in a special format, return the length of the longest absolute path to a file in the file system. 
If there is no file in the system, return 0.

The string input is a file system representation where:
- '\n' is the delimiter between parts of the string
- All folders will end with a name without extension (no periods '.' in the name)
- All files will have an extension (at least one period '.' in the name)
- The file system starts at root directory and folders are represented by multiple '\t' for depth

Example 1:
Input: "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
Output: 20
Explanation: We have the following paths:
"dir/subdir1" = 11 chars
"dir/subdir2/file.ext" = 20 chars

Example 2:
Input: "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
Output: 32
Explanation: Longest path is "dir/subdir2/subsubdir2/file2.ext" = 32 chars

Time Complexity: O(n) where n is the length of the input string
Space Complexity: O(d) where d is the maximum depth of the file system
"""

from typing import List


class Solution:
    def lengthLongestPath(self, input: str) -> int:
        """
        Calculate the length of longest absolute path to a file.
        Uses a stack to keep track of path lengths at each depth level.
        
        Args:
            input: String representation of file system
            
        Returns:
            int: Length of the longest absolute file path
        """
        # Split input into lines and initialize variables
        max_len = 0
        path_len = {0: 0}  # Dictionary to store path length at each depth
        
        # Process each line in the input
        for line in input.split('\n'):
            # Count number of tabs to determine depth
            depth = line.count('\t')
            # Remove tabs to get actual name
            name = line.replace('\t', '')
            
            # If current item is a file (contains '.')
            if '.' in name:
                # Calculate current path length including separators
                curr_len = path_len[depth] + len(name)
                max_len = max(max_len, curr_len)
            else:
                # For directory, update path length at next depth
                # +1 for the '/' separator
                path_len[depth + 1] = path_len[depth] + len(name) + 1
        
        return max_len


def run_test_cases() -> None:
    """Function to run comprehensive test cases"""
    solution = Solution()
    
    test_cases = [
        # Test case 1: Basic directory structure
        (
            "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext",
            20,
            "Basic directory structure"
        ),
        
        # Test case 2: Complex directory structure
        (
            "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext",
            32,
            "Complex directory structure"
        ),
        
        # Test case 3: Single file
        (
            "file.txt",
            8,
            "Single file"
        ),
        
        # Test case 4: Empty input
        (
            "",
            0,
            "Empty input"
        ),
        
        # Test case 5: Only directories, no files
        (
            "dir\n\tsubdir1\n\t\tsubsubdir1",
            0,
            "Only directories, no files"
        ),
        
        # Test case 6: Multiple files at different levels
        (
            "dir\n\tf1.txt\n\tsubdir1\n\t\tf2.txt\n\t\tf3.txt",
            21,
            "Multiple files at different levels"
        ),
        
        # Test case 7: File with multiple extensions
        (
            "dir\n\tfile.tar.gz",
            16,
            "File with multiple extensions"
        ),
        
        # Test case 8: Deep nesting
        (
            "a\n\tb\n\t\tc\n\t\t\td\n\t\t\t\tfile.txt",
            24,
            "Deep nesting structure"
        )
    ]
    
    # Run all test cases
    for i, (test_input, expected, description) in enumerate(test_cases, 1):
        result = solution.lengthLongestPath(test_input)
        print(f"\nTest Case {i}: {description}")
        print(f"Input:\n{test_input}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"Result: {'PASSED' if result == expected else 'FAILED'}")


if __name__ == "__main__":
    run_test_cases()