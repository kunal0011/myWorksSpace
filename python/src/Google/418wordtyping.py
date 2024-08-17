from typing import List


class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        # Step 1: Create the sentence string with spaces in between words
        sentence_str = " ".join(sentence) + " "
        n = len(sentence_str)
        pos = 0

        # Step 2: Simulate the row-by-row fitting process
        for _ in range(rows):
            pos += cols  # Move the position forward by the number of columns

            # If pos lands on a space, move to the next row
            if sentence_str[pos % n] == ' ':
                pos += 1
            else:
                # If pos lands on a character, backtrack to the start of the current word
                while pos > 0 and sentence_str[(pos-1) % n] != ' ':
                    pos -= 1

        # Step 3: Calculate how many times the sentence fits in the screen
        return pos // n
