from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # Sort the pairs by the second element
        pairs.sort(key=lambda x: x[1])

        # Initialize variables
        curr_end = float('-inf')
        count = 0

        # Greedily choose pairs
        for pair in pairs:
            if pair[0] > curr_end:
                curr_end = pair[1]
                count += 1

        return count


# Test the function
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    pairs1 = [[1, 2], [2, 3], [3, 4]]
    print(sol.findLongestChain(pairs1))  # Output: 2

    # Test case 2
    pairs2 = [[1, 2], [7, 8], [4, 5]]
    print(sol.findLongestChain(pairs2))  # Output: 3


class Solution1:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # Sort the pairs by the first element
        pairs.sort(key=lambda x: x[0])

        # Initialize the dp array where dp[i] stores the length of the longest chain ending at index i
        dp = [1] * len(pairs)

        # Fill the dp array
        for i in range(1, len(pairs)):
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


# Test the function
if __name__ == "__main__":
    sol = Solution1()

    # Test case 1
    pairs1 = [[1, 2], [2, 3], [3, 4]]
    print(sol.findLongestChain(pairs1))  # Output: 2

    # Test case 2
    pairs2 = [[1, 2], [7, 8], [4, 5]]
    print(sol.findLongestChain(pairs2))  # Output: 3
