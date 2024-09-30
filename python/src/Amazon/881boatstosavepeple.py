class Solution:
    def numRescueBoats(self, people, limit: int) -> int:
        # Sort the list of people based on their weights
        people.sort()

        # Initialize two pointers
        left, right = 0, len(people) - 1

        # Count for the number of boats
        boats = 0

        # Use the two-pointer technique to find the minimum boats
        while left <= right:
            # If the lightest and the heaviest person can share a boat
            if people[left] + people[right] <= limit:
                left += 1  # Move the left pointer to the next lightest person
            # In all cases, move the right pointer because the heaviest person must take a boat
            right -= 1
            boats += 1  # One boat used

        return boats


# Test the solution with a test case
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Example 1 from the problem
    people = [1, 2]
    limit = 3
    result = solution.numRescueBoats(people, limit)
    print(f"Number of boats required: {result}")  # Expected output: 1

    # Test case 2: Example 2 from the problem
    people = [3, 2, 2, 1]
    limit = 3
    result = solution.numRescueBoats(people, limit)
    print(f"Number of boats required: {result}")  # Expected output: 3

    # Test case 3: Example 3 from the problem
    people = [3, 5, 3, 4]
    limit = 5
    result = solution.numRescueBoats(people, limit)
    print(f"Number of boats required: {result}")  # Expected output: 4
