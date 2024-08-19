from collections import defaultdict
import heapq
# Problem Summary:
# You are given a 2D array items, where each subarray represents a student's score record. Each subarray contains three elements: id (student's ID), score (score received), and timestamp (the time at which the score was recorded). Your task is to compute the average of the top five scores for each student.

# Solution:
# To solve this problem, you can use the following approach:

# Store Scores: Use a dictionary to keep track of scores for each student.
# Sort and Compute: For each student, sort their scores in descending order and calculate the average of the top five scores.


class Solution:
    def highFive(self, items):
        # Dictionary to store scores for each student
        scores = defaultdict(list)

        # Fill the dictionary with scores
        for student_id, score, _ in items:
            heapq.heappush(scores[student_id], score)
            # Ensure that we only keep the top 5 scores
            if len(scores[student_id]) > 5:
                heapq.heappop(scores[student_id])

        # Prepare the result with the average of top 5 scores for each student
        result = []
        for student_id in sorted(scores.keys()):
            top_scores = scores[student_id]
            # Use integer division
            average_score = sum(top_scores) // len(top_scores)
            result.append([student_id, average_score])

        return result


# Example usage
solution = Solution()
items = [
    [1, 91, 1], [1, 92, 2], [1, 60, 3], [1, 65, 4], [1, 70, 5],
    [2, 50, 1], [2, 60, 2], [2, 70, 3], [2, 80, 4], [2, 90, 5],
    [2, 100, 6]
]

print(solution.highFive(items))  # Output: [[1, 70], [2, 80]]
