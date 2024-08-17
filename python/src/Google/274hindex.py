from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # Sort the citations in non-decreasing order
        citations.sort(reverse=True)

        h_index = 0
        for i, citation in enumerate(citations):
            # If the number of citations is greater than or equal to the index + 1
            if citation >= i + 1:
                h_index = i + 1
            else:
                break

        return h_index


s = Solution()
print(s.hIndex([3, 0, 6, 1, 5]))
