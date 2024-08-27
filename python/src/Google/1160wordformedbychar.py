from collections import Counter


class Solution:
    def countCharacters(self, words, chars):
        # Step 1: Count the occurrences of each character in chars
        chars_count = Counter(chars)
        total_length = 0

        # Step 2: Check each word in words
        for word in words:
            word_count = Counter(word)
            can_form = True

            # Step 3: Compare character counts
            for ch in word_count:
                if word_count[ch] > chars_count.get(ch, 0):
                    can_form = False
                    break

            # Step 4: If the word can be formed, add its length to the total
            if can_form:
                total_length += len(word)

        return total_length
