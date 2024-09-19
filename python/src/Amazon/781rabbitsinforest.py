from collections import Counter


class Solution:
    def numRabbits(self, answers: list[int]) -> int:
        count = Counter(answers)  # Count occurrences of each answer
        total_rabbits = 0

        for answer, num_rabbits in count.items():
            group_size = answer + 1  # Group size is answer + 1
            # How many full groups needed
            groups_needed = (num_rabbits + group_size - 1) // group_size
            total_rabbits += groups_needed * group_size  # Add the rabbits from all groups

        return total_rabbits


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    answers1 = [1, 1, 2]
    print(sol.numRabbits(answers1))  # Expected output: 5

    # Test case 2
    answers2 = [10, 10, 10]
    print(sol.numRabbits(answers2))  # Expected output: 11

    # Test case 3
    answers3 = []
    print(sol.numRabbits(answers3))  # Expected output: 0
