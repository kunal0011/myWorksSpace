from collections import Counter


class Solution:
    def countCharacters(self, words, chars):
        # Count the frequency of each character in 'chars'
        chars_count = Counter(chars)
        total_length = 0

        # Iterate through each word
        for word in words:
            word_count = Counter(word)

            # Check if we can form the word with 'chars'
            can_form = True
            for char in word_count:
                if word_count[char] > chars_count.get(char, 0):
                    can_form = False
                    break

            # If we can form the word, add its length to the total
            if can_form:
                total_length += len(word)

        return total_length


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    words1 = ["cat", "bt", "hat", "tree"]
    chars1 = "atach"
    result1 = sol.countCharacters(words1, chars1)
    print(result1)  # Expected output: 6 ("cat" and "hat" can be formed)

    # Test case 2
    words2 = ["hello", "world", "leetcode"]
    chars2 = "welldonehoneyr"
    result2 = sol.countCharacters(words2, chars2)
    print(result2)  # Expected output: 10 ("hello" and "world" can be formed)
