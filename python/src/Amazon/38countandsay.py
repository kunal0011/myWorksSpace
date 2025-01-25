"""
LeetCode 38. Count and Say

Problem Statement:
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
- countAndSay(1) = "1"
- countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), 
  which is then converted into a different digit string.

To determine how you "say" a digit string, split it into minimal groups of the same digit. 
Then for each group, say the number of digits, then say the digit. Finally, concatenate every said digit.

Example 1:
Input: n = 1
Output: "1"

Example 2:
Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "1211"

Constraints:
1 <= n <= 30
"""


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        # Get previous sequence
        prev = self.countAndSay(n - 1)

        # Count consecutive digits
        result = []
        count = 1
        current = prev[0]

        # Process each digit
        for i in range(1, len(prev)):
            if prev[i] == current:
                count += 1
            else:
                result.extend([str(count), current])
                count = 1
                current = prev[i]

        # Add last group
        result.extend([str(count), current])

        return "".join(result)


def explain_sequence(n: int) -> None:
    """
    Function to explain how the count-and-say sequence is generated
    """
    solution = Solution()

    print(f"\nGenerating count-and-say sequence up to n = {n}")
    print("=" * 50)

    for i in range(1, n + 1):
        result = solution.countAndSay(i)

        if i == 1:
            print(f"n = {i}: {result}")
            print("Base case")
        else:
            prev = solution.countAndSay(i - 1)
            print(f"\nn = {i}: {result}")
            print(f"Previous term: {prev}")
            print("Reading it out loud:")

            # Explain the counting process
            count = 1
            current = prev[0]
            explanation = []

            for j in range(1, len(prev)):
                if prev[j] == current:
                    count += 1
                else:
                    explanation.append(f"{count} {current}'s")
                    count = 1
                    current = prev[j]

            explanation.append(f"{count} {current}'s")
            print(" + ".join(explanation))

    print("\nFinal sequence:", result)


def test_count_and_say():
    """
    Test function to verify the countAndSay solution with various test cases
    """
    solution = Solution()

    # Test cases
    test_cases = [
        {
            "n": 1,
            "expected": "1",
            "description": "Base case"
        },
        {
            "n": 2,
            "expected": "11",
            "description": "Two ones"
        },
        {
            "n": 3,
            "expected": "21",
            "description": "One two, one one"
        },
        {
            "n": 4,
            "expected": "1211",
            "description": "One one, one two, two ones"
        },
        {
            "n": 5,
            "expected": "111221",
            "description": "Longer sequence"
        },
        {
            "n": 6,
            "expected": "312211",
            "description": "Even longer sequence"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        n = test_case["n"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nRunning test case {i}: {description}")
        print(f"Input: n = {n}")

        result = solution.countAndSay(n)

        assert result == expected, \
            f"\nTest case {i} failed!\nExpected: {expected}\nGot: {result}"
        print(f"✓ Test case {i} passed!")


if __name__ == "__main__":
    try:
        test_count_and_say()
        print("\nAll test cases passed successfully! 🎉")

        # Explain the sequence generation for n = 5
        explain_sequence(5)
    except AssertionError as e:
        print(f"Test failed! {str(e)}")
