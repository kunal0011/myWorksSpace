"""
LeetCode 2126 - Destroying Asteroids

Problem Statement:
You are given an integer mass, which represents the initial mass of a planet. You are further given an array 
asteroids where asteroids[i] is the mass of the ith asteroid. You can arrange for the planet to collide with 
the asteroids in any arbitrary order. If the mass of the planet is greater than or equal to the mass of the 
asteroid, the asteroid is destroyed and the planet gains the mass of the asteroid. Otherwise, the planet is 
destroyed. Return true if all asteroids can be destroyed.

Time Complexity: O(n log n) due to sorting
Space Complexity: O(1) as we only modify the input array in place
"""


class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: list[int]) -> bool:
        """
        Logic:
        1. Sort asteroids in ascending order
           - This ensures we tackle smaller asteroids first
           - Greedy approach: if we can destroy a larger asteroid, we can destroy all smaller ones
        2. For each asteroid:
           - If planet mass >= asteroid mass:
             * Planet can destroy it and gain its mass
           - Else:
             * Planet is destroyed, return False
        3. If all asteroids processed, return True

        Args:
            mass: Initial mass of the planet
            asteroids: List of asteroid masses
        Returns:
            True if all asteroids can be destroyed, False otherwise
        """
        asteroids.sort()

        for asteroid in asteroids:
            if mass >= asteroid:
                mass += asteroid
            else:
                return False

        return True


# Test driver
def main():
    # Test cases
    test_cases = [
        {
            'mass': 10,
            'asteroids': [3, 9, 19, 5, 21],
            'expected': True
        },
        {
            'mass': 5,
            'asteroids': [4, 9, 23, 4],
            'expected': False
        },
        {
            'mass': 1,
            'asteroids': [1],
            'expected': True
        }
    ]

    solution = Solution()

    for i, test in enumerate(test_cases, 1):
        result = solution.asteroidsDestroyed(test['mass'], test['asteroids'])
        status = "PASSED" if result == test['expected'] else "FAILED"
        print(f"Test {i}: {status}")
        print(f"Input: mass = {test['mass']}, asteroids = {test['asteroids']}")
        print(f"Output: {result}")
        print(f"Expected: {test['expected']}\n")


if __name__ == "__main__":
    main()
