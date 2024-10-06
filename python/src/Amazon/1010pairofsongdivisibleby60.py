class Solution:
    def numPairsDivisibleBy60(self, time) -> int:
        remainders = [0] * 60  # To store counts of remainders
        count = 0

        for t in time:
            remainder = t % 60
            complement = (60 - remainder) % 60  # To handle remainder 0 case
            count += remainders[complement]
            remainders[remainder] += 1

        return count

# Test cases


def test_num_pairs_divisible_by_60():
    solution = Solution()

    # Test case 1
    time1 = [30, 20, 150, 100, 40]
    expected_result_1 = 3  # Pairs: (30, 150), (20, 100), (150, 40)
    assert solution.numPairsDivisibleBy60(
        time1) == expected_result_1, "Test case 1 failed"

    # Test case 2
    time2 = [60, 60, 60]
    expected_result_2 = 3  # Three pairs of (60, 60)
    assert solution.numPairsDivisibleBy60(
        time2) == expected_result_2, "Test case 2 failed"

    # Test case 3
    time3 = [10, 50, 90, 30]
    expected_result_3 = 1  # Pair: (10, 50)
    assert solution.numPairsDivisibleBy60(
        time3) == expected_result_3, "Test case 3 failed"

    print("All test cases passed!")


# Run the tests
test_num_pairs_divisible_by_60()
