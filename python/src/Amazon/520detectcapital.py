class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # Case 1: All letters are capitals
        if word.isupper():
            return True

        # Case 2: All letters are lowercase
        if word.islower():
            return True

        # Case 3: Only the first letter is capitalized and the rest are lowercase
        if word[0].isupper() and word[1:].islower():
            return True

        # If none of the conditions are met, return False
        return False


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    word = "USA"
    print(sol.detectCapitalUse(word))  # Expected output: True

    # Test case 2
    word = "leetcode"
    print(sol.detectCapitalUse(word))  # Expected output: True

    # Test case 3
    word = "Google"
    print(sol.detectCapitalUse(word))  # Expected output: True

    # Test case 4
    word = "FlaG"
    print(sol.detectCapitalUse(word))  # Expected output: False
