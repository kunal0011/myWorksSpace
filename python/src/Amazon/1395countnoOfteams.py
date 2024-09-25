class Solution:
    def numTeams(self, rating: list[int]) -> int:
        n = len(rating)
        count = 0

        for i in range(1, n - 1):
            # Count increasing triplets
            left_smaller = sum(rating[j] < rating[i] for j in range(i))
            right_larger = sum(rating[k] > rating[i] for k in range(i + 1, n))
            count += left_smaller * right_larger

            # Count decreasing triplets
            left_larger = sum(rating[j] > rating[i] for j in range(i))
            right_smaller = sum(rating[k] < rating[i] for k in range(i + 1, n))
            count += left_larger * right_smaller

        return count
