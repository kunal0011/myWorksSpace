class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        num_columns = len(strs[0])
        num_deletions = 0

        # Check each column
        for col in range(num_columns):
            for row in range(1, len(strs)):
                # If the current column is not sorted, mark the column for deletion
                if strs[row][col] < strs[row - 1][col]:
                    num_deletions += 1
                    break

        return num_deletions
