class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        # Create a mapping of each character in the alien language to its index
        order_map = {char: index for index, char in enumerate(order)}

        # Compare each word with the next one
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            # Compare the words letter by letter
            for k in range(min(len(word1), len(word2))):
                # If the characters are different, check their order in the alien language
                if word1[k] != word2[k]:
                    if order_map[word1[k]] > order_map[word2[k]]:
                        return False  # Words are not in correct order
                    break  # If they're in correct order, no need to compare further
            else:
                # If all characters are the same but word1 is longer than word2, it's wrong
                if len(word1) > len(word2):
                    return False

        return True


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    words1 = ["hello", "leetcode"]
    order1 = "hlabcdefgijkmnopqrstuvwxyz"
    print(sol.isAlienSorted(words1, order1))  # Expected output: True

    # Test case 2
    words2 = ["word", "world", "row"]
    order2 = "worldabcefghijkmnpqstuvxyz"
    print(sol.isAlienSorted(words2, order2))  # Expected output: False

    # Test case 3
    words3 = ["apple", "app"]
    order3 = "abcdefghijklmnopqrstuvwxyz"
    print(sol.isAlienSorted(words3, order3))  # Expected output: False
