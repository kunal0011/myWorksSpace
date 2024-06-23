class Solution:
    def grayCode(self, n: int) -> List[int]:
        # Start with the base case for 1-bit Gray code
        result = [0]

        for i in range(n):
            # Reflect the current result
            reflected = [x + (1 << i) for x in reversed(result)]
            # Concatenate the original and reflected lists
            result += reflected

        return result


s = Solution()
print(s.grayCode(3))
