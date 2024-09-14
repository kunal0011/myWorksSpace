class Solution:
    def dietPlanPerformance(self, calories, k, lower, upper):
        score = 0
        current_sum = sum(calories[:k])  # Sum of the first 'k' days

        # Check the score for the first window
        if current_sum < lower:
            score -= 1
        elif current_sum > upper:
            score += 1

        # Slide the window across the array
        for i in range(k, len(calories)):
            current_sum += calories[i] - \
                calories[i - k]  # Update the window sum

            # Check the score for the current window
            if current_sum < lower:
                score -= 1
            elif current_sum > upper:
                score += 1

        return score
