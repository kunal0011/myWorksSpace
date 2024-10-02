class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        # Step 1: Mark numbers that are present in the array
        for i in range(len(nums)):
            # Get the index corresponding to the current number
            index = abs(nums[i]) - 1
            # Mark the number at this index as negative to indicate that the number `index + 1` exists
            if nums[index] > 0:
                nums[index] = -nums[index]

        # Step 2: Collect all the indices where the number is still positive
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)  # Add the missing number (i + 1)

        return result


# Test the Solution
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    # Output: [5, 6]
    print(f"Missing numbers: {solution.findDisappearedNumbers(nums)}")

    # Test case 2
    nums = [1, 1]
    # Output: [2]
    print(f"Missing numbers: {solution.findDisappearedNumbers(nums)}")
