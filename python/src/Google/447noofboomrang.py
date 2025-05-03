"""
LeetCode 447: Number of Boomerangs

Problem Statement:
You are given n points in the plane that are all distinct, where points[i] = [xi, yi].
A boomerang is a tuple of points (i, j, k) such that the distance between i and j equals
the distance between i and k (the order of the tuple matters).

Return the number of boomerangs.

Constraints:
- n == points.length
- 1 <= n <= 500
- points[i].length == 2
- -10^4 <= xi, yi <= 10^4
- All points are distinct
"""


def numberOfBoomerangs(points: list[list[int]]) -> int:
    def distance(p1: list[int], p2: list[int]) -> int:
        # Calculate squared distance to avoid floating point issues
        return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

    result = 0

    # For each point as center point
    for i in range(len(points)):
        # Map to store count of points at each distance
        distances = {}

        # Calculate distance to all other points
        for j in range(len(points)):
            if i != j:
                dist = distance(points[i], points[j])
                distances[dist] = distances.get(dist, 0) + 1

        # For each distance, calculate number of boomerangs
        # If we have n points at distance d, we can form n * (n-1) boomerangs
        for count in distances.values():
            result += count * (count - 1)

    return result

# Test driver


def run_tests():
    test_cases = [
        {
            "points": [[0, 0], [1, 0], [2, 0]],
            "expected": 2,
            "explanation": "The two boomerangs are [(1,0),(0,0),(2,0)] and [(1,0),(2,0),(0,0)]"
        },
        {
            "points": [[1, 1], [2, 2], [3, 3]],
            "expected": 2,
            "explanation": "Points form a line with equal distances"
        },
        {
            "points": [[0, 0]],
            "expected": 0,
            "explanation": "Single point, no boomerangs possible"
        },
        {
            "points": [[0, 0], [1, 0], [2, 0], [3, 0]],
            "expected": 12,
            "explanation": "Multiple points in a line with various possible combinations"
        }
    ]

    for i, test in enumerate(test_cases, 1):
        result = numberOfBoomerangs(test["points"])
        status = "PASSED" if result == test["expected"] else "FAILED"
        print(f"Test {i}: {status}")
        print(f"Points: {test['points']}")
        print(f"Expected: {test['expected']}")
        print(f"Got: {result}")
        print(f"Explanation: {test['explanation']}\n")


if __name__ == "__main__":
    print("Running test cases for Number of Boomerangs problem:\n")
    run_tests()

"""
Solution Logic Explanation:

1. Key Insight:
   - For each point i, find points j and k that are equidistant from i
   - Order matters, so we need to consider permutations

2. Algorithm Steps:
   - For each point as center:
     * Calculate distances to all other points
     * Group points by their distances using a hash map
     * For each group of size n, we can form n * (n-1) boomerangs
       (first select one point out of n, then another out of remaining n-1)

3. Optimizations:
   - Use squared distance to avoid floating point precision issues
   - Use hash map for O(1) lookup of points at same distance
   - Process one center point at a time to reuse distance map

Time Complexity: O(n^2) where n is number of points
Space Complexity: O(n) for the distance hash map
"""
