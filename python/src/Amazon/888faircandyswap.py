class Solution:
    def fairCandySwap(self, AliceSizes, BobSizes):
        sumA = sum(AliceSizes)
        sumB = sum(BobSizes)
        delta = (sumA - sumB) // 2

        # Use a set to make lookups faster for BobSizes
        setB = set(BobSizes)

        for x in AliceSizes:
            # We need y = x - delta for the swap to be fair
            if (x - delta) in setB:
                return [x, x - delta]


# Test case
if __name__ == "__main__":
    solution = Solution()
    AliceSizes = [1, 1]
    BobSizes = [2, 2]
    print(f"Fair swap: {solution.fairCandySwap(AliceSizes, BobSizes)}")
