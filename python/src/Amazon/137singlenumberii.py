class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        # Initialize a variable to hold the result
        result = 0

        # Loop through each bit position (from 0 to 31)
        for i in range(32):
            bit_sum = 0
            for num in nums:
                # Count the number of 1's in the ith bit position across all numbers
                bit_sum += (num >> i) & 1

            # If bit_sum is not a multiple of 3, it means the ith bit in the single number is set
            if bit_sum % 3 != 0:
                # Set the ith bit in the result
                if i == 31:
                    # Handle the sign bit for negative numbers
                    result -= (1 << i)
                else:
                    result |= (1 << i)

        return result


# Test the Solution class
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: The single number is 3, while other numbers appear 3 times.
    nums = [2, 2, 3, 2]
    print(f"The single number is: {solution.singleNumber(nums)}")  # Output: 3

    # Test case 2: The single number is -4.
    nums = [0, 1, 0, 1, 0, 1, -4]
    print(f"The single number is: {solution.singleNumber(nums)}")  # Output: -4
