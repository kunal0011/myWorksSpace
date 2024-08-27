class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        # Step 1: Sort the unique elements
        sorted_unique = sorted(set(arr))

        # Step 2: Create a rank map (element -> rank)
        rank_map = {num: rank + 1 for rank, num in enumerate(sorted_unique)}

        # Step 3: Replace each element with its rank
        return [rank_map[num] for num in arr]
