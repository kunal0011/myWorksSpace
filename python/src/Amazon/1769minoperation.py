class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        n = len(boxes)
        result = [0] * n

        # Left-to-right pass
        count = 0  # Count of balls encountered
        operations = 0  # Total operations to move balls to the current box
        for i in range(n):
            result[i] += operations  # Add the current number of operations
            count += int(boxes[i])  # Update the count of balls
            operations += count  # Increment the operations for the next index

        # Right-to-left pass
        count = 0
        operations = 0
        for i in range(n-1, -1, -1):
            result[i] += operations  # Add the current number of operations
            count += int(boxes[i])  # Update the count of balls
            operations += count  # Increment the operations for the next index

        return result


# Testing the solution
if __name__ == "__main__":
    solution = Solution()

    # Test case
    boxes = "110"
    # Expected output: [1, 1, 3]
    print("Minimum operations:", solution.minOperations(boxes))
