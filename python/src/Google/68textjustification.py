from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        current_line = []
        num_of_letters = 0

        for word in words:
            # If adding the next word exceeds the maxWidth, process the current line
            if num_of_letters + len(word) + len(current_line) > maxWidth:
                for i in range(maxWidth - num_of_letters):
                    # Distribute extra spaces from left to right
                    current_line[i % (len(current_line) - 1 or 1)] += ' '
                result.append(''.join(current_line))
                current_line, num_of_letters = [], 0

            current_line.append(word)
            num_of_letters += len(word)

        # Handle the last line: left-justified with spaces at the end
        result.append(' '.join(current_line).ljust(maxWidth))
        return result


print(Solution().fullJustify(
    ["This", "is", "an", "example", "of", "text", "justification."], 16))
