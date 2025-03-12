"""
LeetCode 520 - Detect Capital

We define the usage of capitals in a word to be right when one of the following cases holds:
1. All letters in this word are capitals, like "USA".
2. All letters in this word are not capitals, like "leetcode".
3. Only the first letter in this word is capital, like "Google".

Given a string word, return true if the usage of capitals in it is right.

Example 1:
Input: word = "USA"
Output: true
Explanation: All letters are capitals.

Example 2:
Input: word = "FlaG"
Output: false
Explanation: Not all letters are capitals, and not only the first letter is capital.
"""

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # Optimization: Early return for single character or empty string
        if len(word) <= 1:
            return True
        
        # Case 1: If first letter is uppercase
        if word[0].isupper():
            # Get the capitalization of the second character
            is_second_upper = len(word) > 1 and word[1].isupper()
            
            # All remaining characters must match the second character's case
            return all(c.isupper() == is_second_upper for c in word[2:])
        
        # Case 2: If first letter is lowercase, all must be lowercase
        return all(c.islower() for c in word[1:])

    def detectCapitalUse_alternative(self, word: str) -> bool:
        """Alternative solution using count approach"""
        caps = sum(1 for c in word if c.isupper())
        return caps == len(word) or caps == 0 or (caps == 1 and word[0].isupper())


def test_detect_capital():
    """Test function to verify both solution approaches"""
    solution = Solution()
    
    test_cases = [
        ("USA", True),
        ("leetcode", True),
        ("Google", True),
        ("FlaG", False),
        ("", True),
        ("a", True),
        ("A", True),
        ("mL", False),
        ("FFFFFFFFFFFFFFFFFFff", False),
        ("FFFFFFFFFFFFFFFFFFf", False),
        ("FFFFFFFFFFFFFFFFFf", False),
        ("Python", True),
        ("javascript", True),
        ("HTMLParser", False),
        ("iPhone", True)
    ]
    
    for i, (word, expected) in enumerate(test_cases, 1):
        # Test main solution
        result_main = solution.detectCapitalUse(word)
        # Test alternative solution
        result_alt = solution.detectCapitalUse_alternative(word)
        
        status_main = "✓" if result_main == expected else "✗"
        status_alt = "✓" if result_alt == expected else "✗"
        
        print(f"Test {i}:")
        print(f"Input: word = '{word}'")
        print(f"Main Solution: {status_main} Got: {result_main}")
        print(f"Alternative Solution: {status_alt} Got: {result_alt}")
        print(f"Expected: {expected}\n")


if __name__ == "__main__":
    test_detect_capital()
