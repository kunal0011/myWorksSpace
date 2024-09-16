class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        max_ones = max_zeros = 0  # To track longest segments
        current_ones = current_zeros = 0  # To track current segments

        for char in s:
            if char == '1':
                current_ones += 1
                current_zeros = 0  # Reset zeros
            else:
                current_zeros += 1
                current_ones = 0  # Reset ones

            max_ones = max(max_ones, current_ones)  # Update max ones
            max_zeros = max(max_zeros, current_zeros)  # Update max zeros

        # Return True if the longest 1-segment is longer than the longest 0-segment
        return max_ones > max_zeros


# Testing the solution
if __name__ == "__main__":
    solution = Solution()

    # Test case
    s = "1101"
    # Expected output: True
    print("Longer ones than zeros:", solution.checkZeroOnes(s))
