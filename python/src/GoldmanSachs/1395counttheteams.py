class Solution:
    def numTeams(self, rating):
        n = len(rating)
        count = 0

        for i in range(n):
            less_left = less_right = greater_left = greater_right = 0

            for j in range(i):
                if rating[j] < rating[i]:
                    less_left += 1
                elif rating[j] > rating[i]:
                    greater_left += 1

            for k in range(i + 1, n):
                if rating[k] < rating[i]:
                    less_right += 1
                elif rating[k] > rating[i]:
                    greater_right += 1

            count += less_left * greater_right + greater_left * less_right

        return count


rating = [2, 5, 3, 4, 1]
solution = Solution()
print(solution.numTeams(rating))
