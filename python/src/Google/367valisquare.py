"""
LeetCode 367 - Valid Perfect Square

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.

Example 1:
Input: num = 16
Output: true
Explanation: 16 is a perfect square (4 * 4 = 16)

Example 2:
Input: num = 14
Output: false
Explanation: 14 is not a perfect square
"""

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
            
        left, right = 2, num // 2
        
        while left <= right:
            mid = (left + right) // 2
            guess_squared = mid * mid
            
            if guess_squared == num:
                return True
            elif guess_squared < num:
                left = mid + 1
            else:
                right = mid - 1
                
        return False

def test_valid_perfect_square():
    solution = Solution()
    test_cases = [
        16,     # true (4*4)
        14,     # false
        1,      # true (1*1)
        4,      # true (2*2)
        9,      # true (3*3)
        25,     # true (5*5)
        30,     # false
    ]
    
    print("Testing Valid Perfect Square:")
    for num in test_cases:
        result = solution.isPerfectSquare(num)
        print(f"Input: {num}, Output: {result}")

if __name__ == "__main__":
    test_valid_perfect_square()
