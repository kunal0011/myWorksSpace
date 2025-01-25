from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # Check if the middle element is the target
            if nums[mid] == target:
                return True

            # If we can't be sure about the halves due to duplicates, move the left pointer
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
                continue
            # Check if the left half is sorted
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Otherwise, the right half must be sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False


def test_search():
    solution = Solution()

    test_cases = [
        {
            "nums": [2, 5, 6, 0, 0, 1, 2],
            "target": 0,
            "expected": True,
            "description": "Target exists"
        },
        {
            "nums": [2, 5, 6, 0, 0, 1, 2],
            "target": 3,
            "expected": False,
            "description": "Target doesn't exist"
        },
        {
            "nums": [1, 0, 1, 1, 1],
            "target": 0,
            "expected": True,
            "description": "Array with duplicates"
        },
        {
            "nums": [1, 1, 1, 1, 1, 1, 1],
            "target": 2,
            "expected": False,
            "description": "All elements same"
        },
        {
            "nums": [1, 1, 1, 1, 1, 2, 1],
            "target": 2,
            "expected": True,
            "description": "Target in mostly duplicate array"
        },
        {
            "nums": [3, 1],
            "target": 1,
            "expected": True,
            "description": "Small array"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        nums = test_case["nums"]
        target = test_case["target"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nTest case {i}: {description}")
        print(f"nums = {nums}")
        print(f"target = {target}")

        result = solution.search(nums, target)

        assert result == expected, \
            f"Expected {expected}, but got {result}"
        print("✓ Test case passed!")


if __name__ == "__main__":
    test_search()
    print("\nAll test cases passed! 🎉")
