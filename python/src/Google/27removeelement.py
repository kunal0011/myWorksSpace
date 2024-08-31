class Solution:
    def removeElement(self, nums, val):
        # Pointer for the position of the new array
        pos = 0

        # Iterate through the list
        for i in range(len(nums)):
            # If the current element is not the one to be removed
            if nums[i] != val:
                # Place it at the next position
                nums[pos] = nums[i]
                pos += 1

        # Return the new length of the array
        return pos
