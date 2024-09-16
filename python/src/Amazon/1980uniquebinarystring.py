class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        n = len(nums)

        # Build the binary string using Cantor's diagonalization
        result = []
        for i in range(n):
            # Flip the ith character of the ith string (0 -> 1, 1 -> 0)
            if nums[i][i] == '0':
                result.append('1')
            else:
                result.append('0')

        return ''.join(result)


# Testing the solution
if __name__ == "__main__":
    solution = Solution()

    # Test case
    nums = ["111", "011", "001"]
    # Expected output: "100"
    print("Unique Binary String:", solution.findDifferentBinaryString(nums))
