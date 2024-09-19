class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        max_so_far = 0
        chunks = 0

        for i in range(len(arr)):
            # Track the maximum value in the chunk
            max_so_far = max(max_so_far, arr[i])
            if max_so_far == i:  # If the maximum value matches the index, we can make a chunk
                chunks += 1

        return chunks


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    arr1 = [4, 3, 2, 1, 0]
    print(sol.maxChunksToSorted(arr1))  # Expected output: 1

    # Test case 2
    arr2 = [1, 0, 2, 3, 4]
    print(sol.maxChunksToSorted(arr2))  # Expected output: 4
