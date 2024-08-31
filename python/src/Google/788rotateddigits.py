class Solution:
    def rotatedDigits(self, N: int) -> int:
        good_count = 0

        # Define the sets of digits
        valid = {'0', '1', '8', '2', '5', '6', '9'}
        different = {'2', '5', '6', '9'}

        # Iterate through each number from 1 to N
        for i in range(1, N + 1):
            s = str(i)
            if set(s).issubset(valid) and any(d in s for d in different):
                good_count += 1

        return good_count


# Example usage
solution = Solution()
N = 10
result = solution.rotatedDigits(N)
print(result)  # Output: 4
