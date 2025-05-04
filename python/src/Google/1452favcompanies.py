"""
LeetCode 1452. People Whose List of Favorite Companies Is Not a Subset of Another List

Problem Statement:
Given the array favoriteCompanies where favoriteCompanies[i] is the list of favorites companies 
for the ith person (indexed from 0). Return the indices of people whose list of favorite 
companies is not a subset of any other list. You must return the indices in increasing order.

Time Complexity: O(n^2 * m) where n is number of people and m is average length of company lists
Space Complexity: O(n * m) for storing sets
"""


class Solution:
    def peopleIndexes(self, favoriteCompanies: list[list[str]]) -> list[int]:
        # Logic:
        # 1. Convert each person's company list to a set for O(1) lookup
        # 2. For each person i:
        #    - Check if their company set is a subset of any other person's set
        #    - If not a subset of any other set, add index i to result
        # 3. Return indices in increasing order (naturally maintained)

        sets = [set(fav) for fav in favoriteCompanies]
        result = []

        for i, current_set in enumerate(sets):
            if all(not current_set.issubset(other_set)
                   for j, other_set in enumerate(sets) if i != j):
                result.append(i)

        return result


# Test driver
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        [["leetcode", "google", "facebook"],
         ["google", "microsoft"],
         ["google", "facebook"],
         ["google"],
         ["amazon"]],

        [["leetcode", "google", "facebook"],
         ["leetcode", "amazon"],
         ["facebook", "google"]],

        [["leetcode"],
         ["google"],
         ["facebook"],
         ["amazon"]]
    ]

    for i, companies in enumerate(test_cases):
        result = solution.peopleIndexes(companies)
        print(f"Test case {i + 1}:")
        print(f"Favorite Companies:")
        for j, comp in enumerate(companies):
            print(f"Person {j}: {comp}")
        print(f"Result indices: {result}")
        print()
