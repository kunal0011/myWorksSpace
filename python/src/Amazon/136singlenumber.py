class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        unique_number = 0
        for num in nums:
            unique_number ^= num  # XORing all numbers
        return unique_number
