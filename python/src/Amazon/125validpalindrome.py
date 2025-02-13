"""
LeetCode 125. Valid Palindrome

Problem Statement:
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
and removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:
- 1 <= s.length <= 2 * 10^5
- s consists only of printable ASCII characters
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Two-pointer approach.
        Time complexity: O(n)
        Space complexity: O(1)
        """
        left, right = 0, len(s) - 1

        while left < right:
            # Skip non-alphanumeric characters from left
            while left < right and not s[left].isalnum():
                left += 1
            # Skip non-alphanumeric characters from right
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare characters
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True

    def isPalindromeWithCleaning(self, s: str) -> bool:
        """
        Clean string first approach.
        Time complexity: O(n)
        Space complexity: O(n)
        """
        # Clean the string: remove non-alphanumeric and convert to lowercase
        cleaned = ''.join(char.lower() for char in s if char.isalnum())

        # Compare with its reverse
        return cleaned == cleaned[::-1]

    def isPalindromeWithVisualization(self, s: str) -> tuple[bool, list[tuple[int, int]]]:
        """
        Returns whether string is palindrome and list of comparison positions.
        Time complexity: O(n)
        Space complexity: O(n)
        """
        comparisons = []
        left, right = 0, len(s) - 1

        while left < right:
            # Skip non-alphanumeric characters from left
            while left < right and not s[left].isalnum():
                left += 1
            # Skip non-alphanumeric characters from right
            while left < right and not s[right].isalnum():
                right -= 1

            # Store comparison positions
            if left < right:
                comparisons.append((left, right))

            # Compare characters
            if s[left].lower() != s[right].lower():
                return False, comparisons

            left += 1
            right -= 1

        return True, comparisons


def visualize_palindrome_check(s: str, comparisons: list[tuple[int, int]]) -> None:
    """Helper function to visualize palindrome checking process"""
    print(f"\nString: {s}")
    print("Checking process:")

    # Print string with position numbers
    print("\nPositions:")
    for i in range(len(s)):
        print(f"{i:2}", end=" ")
    print("\nCharacters:")
    for char in s:
        print(f"{char:2}", end=" ")
    print("\n")

    # Show each comparison
    for i, (left, right) in enumerate(comparisons, 1):
        line = ""
        for j in range(len(s)):
            if j == left:
                line += f"[{s[j]}]"
            elif j == right:
                line += f"[{s[j]}]"
            else:
                line += f" {s[j]} "
        print(f"Step {i}: Comparing positions {left} and {right}: "
              f"'{s[left].lower()}' vs '{s[right].lower()}'")
        print(line)
        print()


def test_valid_palindrome():
    solution = Solution()

    test_cases = [
        {
            "s": "A man, a plan, a canal: Panama",
            "expected": True,
            "description": "Classic palindrome with punctuation"
        },
        {
            "s": "race a car",
            "expected": False,
            "description": "Non-palindrome"
        },
        {
            "s": " ",
            "expected": True,
            "description": "Empty string after cleaning"
        },
        {
            "s": "0P",
            "expected": False,
            "description": "Alphanumeric characters"
        },
        {
            "s": "Was it a car or a cat I saw?",
            "expected": True,
            "description": "Longer palindrome with spaces and punctuation"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        s = test_case["s"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nTest case {i}: {description}")

        # Test all implementations
        result1 = solution.isPalindrome(s)
        result2 = solution.isPalindromeWithCleaning(s)
        result3, comparisons = solution.isPalindromeWithVisualization(s)

        # Visualize the checking process
        visualize_palindrome_check(s, comparisons)

        print(
            f"Cleaned string: {''.join(char.lower() for char in s if char.isalnum())}")
        print(f"Is palindrome: {result1}")

        assert result1 == expected and result2 == expected and result3 == expected, \
            f"Expected {expected}, but got {result1} (two-pointer), " \
            f"{result2} (cleaning), {result3} (visualization)"
        print("✓ Test case passed!")


if __name__ == "__main__":
    test_valid_palindrome()
    print("\nAll test cases passed! 🎉")
