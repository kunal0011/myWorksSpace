class Solution:
    def maximumSwap(self, num: int) -> int:
        # Convert the number to a list of digits
        digits = list(str(num))

        # Create a list to store the last occurrence of each digit
        last = {int(x): i for i, x in enumerate(digits)}

        # Traverse through each digit
        for i, x in enumerate(digits):
            # Check if there is a larger digit after the current one
            for d in range(9, int(x), -1):
                if last.get(d, -1) > i:
                    # Swap the current digit with the larger one
                    digits[i], digits[last[d]] = digits[last[d]], digits[i]
                    # Convert the list back to an integer and return the result
                    return int(''.join(digits))

        # If no swap can increase the number, return the original number
        return num


# Test the solution with some test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: num = 2736
    num = 2736
    # Expected output: 7236
    print(f"Maximum number after swap for {num}: {solution.maximumSwap(num)}")

    # Test case 2: num = 9973
    num = 9973
    # Expected output: 9973 (no swap increases the value)
    print(f"Maximum number after swap for {num}: {solution.maximumSwap(num)}")

    # Test case 3: num = 98368
    num = 98368
    # Expected output: 98863
    print(f"Maximum number after swap for {num}: {solution.maximumSwap(num)}")
