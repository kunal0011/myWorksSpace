# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:
#     pass

from typing import List


def read4(buf4: List[str]) -> int:
    """
    :param buf4: a buffer that can hold 4 characters, passed by reference.
    :return: the number of characters read.
    """
    pass


class Solution:
    def read(self, buf: List[str], n: int) -> int:
        temp_buf = [''] * 4  # Temporary buffer to store characters from read4
        total_chars_read = 0  # Total characters read so far

        while total_chars_read < n:
            chars_read = read4(temp_buf)  # Read up to 4 chars into temp_buf

            if chars_read == 0:  # End of file
                break

            # Calculate how many characters we can actually copy to buf
            chars_to_copy = min(chars_read, n - total_chars_read)

            # Copy characters from temp_buf to buf
            for i in range(chars_to_copy):
                buf[total_chars_read + i] = temp_buf[i]

            total_chars_read += chars_to_copy

        return total_chars_read
