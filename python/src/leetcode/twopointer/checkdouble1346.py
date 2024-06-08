# Given an array arr of integers, check if there exist two indices i and j such that :

# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]
 

# Example 1:

# Input: arr = [10,2,5,3]
# Output: true
# Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]
# Example 2:

# Input: arr = [3,1,7,11]
# Output: false
# Explanation: There is no i and j that satisfy the conditions.
 

# Constraints:

# 2 <= arr.length <= 500
# -103 <= arr[i] <= 103

from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        #arr.sort()
        # index1=-1
        # for i in range(len(arr)):
        #     if arr[i]<0:
        #         index1=i
        # if index1 >= 1:
        #     arr = arr[:index1+1][::-1]+arr[index1+1:]
        negatives = [x for x in arr if x < 0]
        non_negatives = [x for x in arr if x >= 0]
        
        # Step 2: Sort negative numbers in reverse order
        negatives.sort(reverse=True)
        
        # Step 3: Sort non-negative numbers in ascending order
        non_negatives.sort()
        
        # Step 4: Combine the sorted parts
        arr = negatives + non_negatives
        left = 0
        right = len(arr)-1

        while left < right:
            if arr[left]*2 == arr[right]:
                return True
            elif arr[left]*2 > arr[right]:
                right -= 1
            else:
                r = right
                while(left<r):
                    if arr[left]*2 == arr[r]:
                        return True
                    r -= 1
                left += 1
        return False
    

class Solution1:
    def checkIfExist(self, arr: List[int]) -> bool:
            seen = set()
            for num in arr:
                if num * 2 in seen or (num % 2 == 0 and num // 2 in seen):
                    return True
                seen.add(num)
    
            return False

    
if __name__ == '__main__':
    s = Solution1()
    print(s.checkIfExist([3,1,7,11]))
    print(s.checkIfExist([10,2,5,3]))
    print(s.checkIfExist([-20,8,-6,-14,0,-19,14,4]))
    print(s.checkIfExist([-10,12,-20,-8,15]))