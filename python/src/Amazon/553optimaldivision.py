class Solution:
    def optimalDivision(self, nums: list[int]) -> str:
        # If there's only one number, return it as it is
        if len(nums) == 1:
            return str(nums[0])
        # If there are two numbers, return them divided without parentheses
        elif len(nums) == 2:
            return f"{nums[0]}/{nums[1]}"
        else:
            # For more than two numbers, format as "a/(b/c/d/...)"
            return f"{nums[0]}/(" + "/".join(map(str, nums[1:])) + ")"
