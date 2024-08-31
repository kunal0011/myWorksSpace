class Solution:
    def isIdealPermutation(self, A) -> bool:
        for i in range(len(A)):
            if abs(A[i] - i) > 1:
                return False
        return True


# Example usage
solution = Solution()
A1 = [1, 0, 2]  # Output should be True
A2 = [1, 2, 0]  # Output should be False

print(solution.isIdealPermutation(A1))  # Output: True
print(solution.isIdealPermutation(A2))  # Output: False
