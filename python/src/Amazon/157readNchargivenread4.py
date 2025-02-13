"""
LeetCode 157. Read N Characters Given Read4

Problem Statement:
Given a file and assume that you can only read the file using a given method read4, 
implement a method to read n characters.

Method read4:
The API read4 reads four consecutive characters from file, then writes those characters 
into the buffer array buf4.
The return value is the number of actual characters read.

Note that read4() has its own file pointer, much like FILE *fp in C.

Definition of read4:
    Parameter:  char[] buf4
    Returns:    int

buf4[] is a destination, not a source. The results from read4 will be copied to buf4[].

Method read:
By using the read4 method, implement the method read that reads n characters from file 
and store it in the buffer array buf. Consider that you cannot manipulate file directly.

The return value is the number of actual characters read.

Example 1:
Input: file = "abc", n = 4
Output: 3
Explanation: After calling your read method, buf should contain "abc". 
We read a total of 3 characters from the file, so return 3.

Example 2:
Input: file = "abcde", n = 5
Output: 5
Explanation: After calling your read method, buf should contain "abcde". 
We read a total of 5 characters from the file, so return 5.

Constraints:
- 1 <= file.length <= 500
- file consists of English letters and digits
- 1 <= n <= 1000
"""

from typing import List


def read4(buf4):
    """
    The read4 API is already defined for you.
    @param buf4, a list of characters
    @return an integer
    """
    # This is a mock implementation for testing
    return 0


class Solution:
    def read(self, buf: List[str], n: int) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        copied = 0  # Total characters copied to buf
        buf4 = [''] * 4  # Temporary buffer for read4

        while copied < n:
            # Read up to 4 characters from the file
            count = read4(buf4)

            if count == 0:  # Reached end of file
                break

            # Only copy up to n characters
            count = min(count, n - copied)

            # Copy from temporary buffer to output buffer
            for i in range(count):
                buf[copied] = buf4[i]
                copied += 1

        return copied


def test_read():
    """
    Test function with mock implementation.
    Note: Since read4 is an API call, we can only test the logic here.
    """
    class MockRead4Solution(Solution):
        def __init__(self, file_content):
            self.file_content = file_content
            self.file_pointer = 0

        def read4(self, buf4):
            chars_read = 0
            while chars_read < 4 and self.file_pointer < len(self.file_content):
                buf4[chars_read] = self.file_content[self.file_pointer]
                chars_read += 1
                self.file_pointer += 1
            return chars_read

        def read(self, buf, n):
            copied = 0
            buf4 = [''] * 4

            while copied < n:
                count = self.read4(buf4)
                if count == 0:
                    break

                count = min(count, n - copied)
                for i in range(count):
                    buf[copied] = buf4[i]
                    copied += 1

            return copied

    test_cases = [
        {
            "file": "abc",
            "n": 4,
            "expected_chars": 3,
            "expected_content": "abc",
            "description": "Read more than file length"
        },
        {
            "file": "abcde",
            "n": 5,
            "expected_chars": 5,
            "expected_content": "abcde",
            "description": "Read exact file length"
        },
        {
            "file": "abcdef",
            "n": 3,
            "expected_chars": 3,
            "expected_content": "abc",
            "description": "Read less than file length"
        },
        {
            "file": "a",
            "n": 1,
            "expected_chars": 1,
            "expected_content": "a",
            "description": "Single character"
        },
        {
            "file": "abcdefgh",
            "n": 7,
            "expected_chars": 7,
            "expected_content": "abcdefg",
            "description": "Multiple read4 calls"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        solution = MockRead4Solution(test_case["file"])
        buf = [''] * test_case["n"]
        chars_read = solution.read(buf, test_case["n"])

        assert chars_read == test_case["expected_chars"], \
            f'Test case {i} failed. Expected {test_case["expected_chars"]} chars read, got {chars_read}'

        content = ''.join(buf[:chars_read])
        assert content == test_case["expected_content"], \
            f'Test case {i} failed. Expected content "{test_case["expected_content"]}", got "{content}"'

        print(f'Test case {i} passed: {test_case["description"]}')

    print("\nAll test cases passed! 🎉")


if __name__ == "__main__":
    test_read()
