class Solution:
    def minimizeTheDifference(self, mat: list[list[int]], target: int) -> int:
        possible_sums = {0}

        for row in mat:
            new_sums = set()
            for num in row:
                for current_sum in possible_sums:
                    new_sums.add(current_sum + num)
            possible_sums = new_sums

        # Find the minimum absolute difference
        return min(abs(s - target) for s in possible_sums)
