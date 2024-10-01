class Solution:
    def numTrees(self, n: int) -> int:
        '''
        dp[3] =
        dp[0] * dp[2]
        (If 1 is the root, the left subtree must not exist, and the right subtree can have two numbers)

        +

        dp[1] * dp[1]
        (If 2 is the root, the left and right subtrees can each have a number)

        +

        dp[2] * dp[0]
        (If 3 is the root, the left subtree can have two numbers, and the right subtree must not exist)
        '''
        catalan = [0] * (n + 1)

        # Base case
        catalan[0] = 1

        # Fill the array using the recursive formula
        for i in range(1, n + 1):
            for j in range(i):
                catalan[i] += catalan[j] * catalan[i - 1 - j]

        return catalan[n]
