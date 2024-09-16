from collections import defaultdict


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        reserved = defaultdict(set)

        # Mark reserved seats for each row
        for seat in reservedSeats:
            row, col = seat
            reserved[row].add(col)

        total_families = 2 * n  # Initially assume all rows can fit 2 families

        for row in reserved:
            can_place_left = all(
                seat not in reserved[row] for seat in [2, 3, 4, 5])
            can_place_right = all(
                seat not in reserved[row] for seat in [6, 7, 8, 9])
            can_place_middle = all(
                seat not in reserved[row] for seat in [4, 5, 6, 7])

            # Start by assuming no families can be placed in this row
            families_in_this_row = 0

            # Check if left and right blocks can be filled
            if can_place_left:
                families_in_this_row += 1
            if can_place_right:
                families_in_this_row += 1
            # If both left and right are blocked, check the middle block
            if families_in_this_row == 0 and can_place_middle:
                families_in_this_row += 1

            # Reduce from the initial 2 possible families if families can't sit
            total_families -= (2 - families_in_this_row)

        return total_families


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    n1 = 3
    reservedSeats1 = [[1, 2], [1, 3], [1, 8], [2, 6], [3, 1], [3, 10]]
    assert sol.maxNumberOfFamilies(
        n1, reservedSeats1) == 4, f"Test case 1 failed"

    # Test case 2
    n2 = 2
    reservedSeats2 = [[2, 1], [1, 8], [2, 6]]
    assert sol.maxNumberOfFamilies(
        n2, reservedSeats2) == 2, f"Test case 2 failed"

    # Test case 3
    n3 = 4
    reservedSeats3 = [[4, 3], [4, 4], [4, 7], [4, 8], [4, 9], [1, 10], [2, 2]]
    assert sol.maxNumberOfFamilies(
        n3, reservedSeats3) == 4, f"Test case 3 failed"

    print("All test cases passed!")
