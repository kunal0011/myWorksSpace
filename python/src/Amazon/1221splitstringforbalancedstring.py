class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = 0
        count = 0

        # Traverse through the string
        for char in s:
            # Increase balance for 'L', decrease for 'R'
            if char == 'L':
                balance += 1
            else:
                balance -= 1

            # When balance is 0, we found a balanced string
            if balance == 0:
                count += 1

        return count


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    s1 = "RLRRLLRLRL"
    result1 = sol.balancedStringSplit(s1)
    assert result1 == 4, f"Test case 1 failed: {result1}"

    # Test case 2
    s2 = "RLLLLRRRLR"
    result2 = sol.balancedStringSplit(s2)
    assert result2 == 3, f"Test case 2 failed: {result2}"

    # Test case 3
    s3 = "LLLLRRRR"
    result3 = sol.balancedStringSplit(s3)
    assert result3 == 1, f"Test case 3 failed: {result3}"

    print("All test cases passed!")
