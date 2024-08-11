from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0  # Index to write the compressed string
        read = 0   # Index to read through the chars array

        while read < len(chars):
            char = chars[read]
            count = 0

            # Count the number of occurrences of the current character
            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1

            # Write the character
            chars[write] = char
            write += 1

            # If the character count is greater than 1, write the count as well
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write


# Example usage:
chars = ["a", "a", "b", "b", "c", "c", "c"]
new_length = Solution().compress(chars)
print(new_length)  # Output: 6
print(chars[:new_length])  # Output: ["a","2","b","2","c","3"]
