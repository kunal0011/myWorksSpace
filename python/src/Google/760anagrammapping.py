class Solution:
    def anagramMappings(self, nums1, nums2):
        # Create a hashmap to store the value and its corresponding index in nums2
        index_map = {value: index for index, value in enumerate(nums2)}

        # Create the result list by mapping each value in nums1 to its index in nums2
        result = [index_map[num] for num in nums1]

        return result
