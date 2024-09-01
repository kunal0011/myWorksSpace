class Solution:
    def constructArray(self, n, k):
        result = []

        # First, create the first k+1 elements to have k distinct differences
        for i in range(1, k+2):
            if i % 2 != 0:  # Odd index, pick from the start
                result.append((i + 1) // 2)
            else:  # Even index, pick from the end
                result.append(k + 2 - i // 2)

        # Then fill the rest of the numbers sequentially
        for i in range(k + 2, n + 1):
            result.append(i)

        return result
