"""
LeetCode 401 - Binary Watch

A binary watch has 4 LEDs on top to represent hours (0-11) and 6 LEDs on bottom to represent
minutes (0-59). Each LED represents a number in increasing order:
- Hours: 1, 2, 4, 8
- Minutes: 1, 2, 4, 8, 16, 32

Given an integer turnedOn which represents the number of LEDs that are currently on,
return all possible times the watch could represent.

Example 1:
Input: turnedOn = 1
Output: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]

Example 2:
Input: turnedOn = 9
Output: []
"""

from typing import List

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        def count_bits(n: int) -> int:
            return bin(n).count('1')
        
        result = []
        # Try all possible hour (0-11) and minute (0-59) combinations
        for hour in range(12):
            for minute in range(60):
                # If the total number of 1's in binary representation of
                # both hour and minute equals turnedOn, we found a valid time
                if count_bits(hour) + count_bits(minute) == turnedOn:
                    # Format the time string properly
                    result.append(f"{hour}:{minute:02d}")
        
        return result


# Test driver
def main():
    solution = Solution()
    
    # Test cases
    test_cases = [
        1,  # Should return ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
        2,  # Should return multiple valid combinations
        9,  # Should return []
        0   # Should return ["0:00"]
    ]
    
    for turnedOn in test_cases:
        result = solution.readBinaryWatch(turnedOn)
        print(f"\nInput: turnedOn = {turnedOn}")
        print(f"Output: {result}")


if __name__ == "__main__":
    main()