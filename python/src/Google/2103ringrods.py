class Solution:
    def countPoints(self, rings: str) -> int:
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
