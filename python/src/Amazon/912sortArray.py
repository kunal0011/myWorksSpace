from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Helper function for merge
        def merge(left, right):
            sorted_list = []
            i = j = 0

            # Merge two sorted arrays
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    sorted_list.append(left[i])
                    i += 1
                else:
                    sorted_list.append(right[j])
                    j += 1

            # Add remaining elements from left and right
            while i < len(left):
                sorted_list.append(left[i])
                i += 1
            while j < len(right):
                sorted_list.append(right[j])
                j += 1

            return sorted_list

        # Helper function for merge sort
        def merge_sort(arr):
            # Base case: a single element or empty array is already sorted
            if len(arr) <= 1:
                return arr

            # Divide the array into two halves
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

            # Merge the sorted halves
            return merge(left, right)

        # Sort the array using merge sort
        return merge_sort(nums)
