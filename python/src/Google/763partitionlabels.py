class Solution:
    def partitionLabels(self, S: str):
        # Step 1: Create a dictionary to store the last occurrence of each character
        last_occurrence = {c: i for i, c in enumerate(S)}

        # Step 2: Traverse the string to create partitions
        partitions = []
        start, end = 0, 0

        for i, c in enumerate(S):
            # Update the end to the farthest last occurrence of the current character
            end = max(end, last_occurrence[c])

            # If the current index reaches the end of the partition
            if i == end:
                partitions.append(end - start + 1)
                start = i + 1

        return partitions


# Example usage
solution = Solution()
S1 = "ababcbacadefegdehijhklij"

print(solution.partitionLabels(S1))  # Output: [9, 7, 8]
