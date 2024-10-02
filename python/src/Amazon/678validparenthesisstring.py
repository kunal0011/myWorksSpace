class Solution:
    def checkValidString(self, s: str) -> bool:
        minOpen = 0  # Minimum number of open parentheses
        maxOpen = 0  # Maximum number of open parentheses

        for char in s:
            if char == '(':
                minOpen += 1
                maxOpen += 1
            elif char == ')':
                # Decrease but minOpen cannot go below 0
                minOpen = max(minOpen - 1, 0)
                maxOpen -= 1
            else:  # char == '*'
                minOpen = max(minOpen - 1, 0)  # '*' can be treated as ')'
                maxOpen += 1  # '*' can be treated as '('

            # If at any point maxOpen is negative, there are too many closing parentheses
            if maxOpen < 0:
                return False

        # If minOpen is 0, we can balance all open parentheses
        return minOpen == 0


# Test the Solution
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    s = "(*))"
    # Output: True
    print(f"Is the string '{s}' valid? {solution.checkValidString(s)}")

    # Test case 2
    s = "(*)"
    # Output: True
    print(f"Is the string '{s}' valid? {solution.checkValidString(s)}")

    # Test case 3
    s = "(*()"
    # Output: True
    print(f"Is the string '{s}' valid? {solution.checkValidString(s)}")

    # Test case 4
    s = "(()))"
    # Output: False
    print(f"Is the string '{s}' valid? {solution.checkValidString(s)}")
