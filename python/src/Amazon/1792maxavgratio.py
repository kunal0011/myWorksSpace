import heapq


class Solution:
    def maxAverageRatio(self, classes: list[list[int]], extraStudents: int) -> float:
        # Function to calculate the improvement in pass ratio if we add one student
        def improvement(passed, total):
            return (passed + 1) / (total + 1) - passed / total

        # Create a max heap based on the improvement in pass ratio
        max_heap = []
        for passed, total in classes:
            heapq.heappush(
                max_heap, (-improvement(passed, total), passed, total))

        # Add extra students
        for _ in range(extraStudents):
            # Get the class with the maximum improvement potential
            imp, passed, total = heapq.heappop(max_heap)
            passed += 1
            total += 1
            # Recalculate the improvement and push back into the heap
            heapq.heappush(
                max_heap, (-improvement(passed, total), passed, total))

        # Calculate the final average pass ratio
        total_avg = 0
        for _, passed, total in max_heap:
            total_avg += passed / total

        return total_avg / len(classes)


# Testing the solution
if __name__ == "__main__":
    solution = Solution()

    # Test case
    classes = [[1, 2], [3, 5], [2, 2]]
    extraStudents = 2
    print("Max average pass ratio:", solution.maxAverageRatio(
        classes, extraStudents))  # Expected output: ~0.78333
