"""
LeetCode 2103 - Rings and Rods

Problem Statement:
There are n rings and each ring is either red, green, or blue. The rings are distributed across
ten rods labeled from 0 to 9. You are given a string rings of length 2n that describes the n rings 
that are placed onto the rods. Every two characters in rings forms a color-position pair that is
used to describe each ring where:
- The first character of the ith pair denotes the ith ring's color ('R', 'G', 'B').
- The second character of the ith pair denotes the rod where the ith ring is placed (0 to 9).
Return the number of rods that have all three colors of rings on them.

Time Complexity: O(n) where n is the length of rings string
Space Complexity: O(1) as we use fixed size lists/sets (maximum 10 rods)
"""


class Solution:
    def countPoints(self, rings: str) -> int:
        """
        Logic:
        1. Create a list of sets for each rod (0-9) to track unique colors
        2. Iterate through rings string in pairs:
           - First character is color (R/G/B)
           - Second character is rod number (0-9)
           - Add color to corresponding rod's set
        3. Count rods that have all three colors (R,G,B)

        Args:
            rings: String representing color-position pairs
        Returns:
            Number of rods with all three colors
        """
        # Initialize a list of sets to track colors on each rod (index 0 to 9)
        rods = [set() for _ in range(10)]

        # Traverse the string in pairs
        for i in range(0, len(rings), 2):
            color = rings[i]
            rod = int(rings[i + 1])
            rods[rod].add(color)

        # Count the number of rods that contain all three colors
        count = 0
        for rod in rods:
            if {'R', 'G', 'B'}.issubset(rod):
                count += 1

        return count


# Test driver
def main():
    # Test cases
    test_cases = [
        {
            'rings': "B0B6G0R6R0R6G9",
            'expected': 1
        },
        {
            'rings': "B0R0G0R9R0B0G0",
            'expected': 1
        },
        {
            'rings': "G4",
            'expected': 0
        },
        {
            'rings': "R2G2B2",
            'expected': 1
        }
    ]

    solution = Solution()

    for i, test in enumerate(test_cases, 1):
        result = solution.countPoints(test['rings'])
        status = "PASSED" if result == test['expected'] else "FAILED"
        print(f"Test {i}: {status}")
        print(f"Input: rings = {test['rings']}")
        print(f"Output: {result}")
        print(f"Expected: {test['expected']}\n")


if __name__ == "__main__":
    main()
