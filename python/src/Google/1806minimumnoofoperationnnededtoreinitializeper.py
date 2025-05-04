"""
LeetCode 1806. Minimum Number of Operations to Reinitialize a Permutation

Problem Statement:
You are given an even integer n. You initially have a permutation perm of size n where perm[i] == i (0-indexed).
In one operation, you will create a new array arr, and for each i:
- If i % 2 == 0, then arr[i] = perm[i/2]
- If i % 2 == 1, then arr[i] = perm[n/2 + (i-1)/2]
You will then assign arr to perm.
Return the minimum non-zero number of operations you need to perform on perm to return the permutation to its initial value.

Time Complexity: O(n) per operation
Space Complexity: O(n) for storing permutations
"""


class Solution:
    def reinitializePermutation(self, n: int) -> int:
        # Logic:
        # 1. Start with initial permutation [0,1,2,...,n-1]
        # 2. Apply the given operation repeatedly:
        #    - For even indices i: arr[i] = perm[i/2]
        #    - For odd indices i: arr[i] = perm[n/2 + (i-1)/2]
        # 3. Count operations until we get back to initial permutation
        # 4. Return the count

        perm = list(range(n))
        original = list(range(n))
        count = 0

        while True:
            new_perm = [0] * n
            for i in range(n):
                if i % 2 == 0:
                    new_perm[i] = perm[i // 2]
                else:
                    new_perm[i] = perm[n // 2 + (i - 1) // 2]

            count += 1
            perm = new_perm

            # Check if the permutation is back to the original
            if perm == original:
                break

        return count


# Test driver
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        2,    # Expected: 1
        4,    # Expected: 2
        6,    # Expected: 4
        8,    # Expected: 3
        10    # Expected: 6
    ]

    for i, n in enumerate(test_cases):
        result = solution.reinitializePermutation(n)
        print(f"Test case {i + 1}:")
        print(f"n = {n}")
        print(f"Minimum operations needed: {result}")

        # Show the permutation after each operation for verification
        perm = list(range(n))
        print("Permutation changes:")
        print(f"Initial: {perm}")
        for op in range(result):
            new_perm = [0] * n
            for i in range(n):
                if i % 2 == 0:
                    new_perm[i] = perm[i // 2]
                else:
                    new_perm[i] = perm[n // 2 + (i - 1) // 2]
            perm = new_perm
            print(f"After operation {op + 1}: {perm}")
        print()
