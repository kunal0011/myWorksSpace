class Solution:
    def palindromePairs(self, words):
        def is_palindrome(check):
            return check == check[::-1]

        # Dictionary to store the word and its index.
        word_dict = {word: i for i, word in enumerate(words)}
        res = []

        # Iterate over every word and check possible palindrome pairs
        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                # Split the word into two parts: prefix and suffix
                prefix = word[:j]
                suffix = word[j:]

                # Case 1: If the prefix is a palindrome, check if the reversed suffix exists in the dictionary
                if is_palindrome(prefix):
                    reversed_suffix = suffix[::-1]
                    if reversed_suffix in word_dict and word_dict[reversed_suffix] != i:
                        res.append([word_dict[reversed_suffix], i])

                # Case 2: If the suffix is a palindrome, check if the reversed prefix exists in the dictionary
                # Ensure that suffix isn't empty to avoid duplication of the same result.
                if j != len(word) and is_palindrome(suffix):
                    reversed_prefix = prefix[::-1]
                    if reversed_prefix in word_dict and word_dict[reversed_prefix] != i:
                        res.append([i, word_dict[reversed_prefix]])

        return res
