class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        # Define arrays for basic numbers
        below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve",
                    "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty",
                "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]

        def helper(n):
            if n == 0:
                return ""
            elif n < 20:
                return below_20[n] + " "
            elif n < 100:
                return tens[n // 10] + " " + helper(n % 10)
            else:
                return below_20[n // 100] + " Hundred " + helper(n % 100)

        result = ""
        i = 0

        # Process each chunk of 3 digits
        while num > 0:
            if num % 1000 != 0:
                result = helper(num % 1000) + thousands[i] + " " + result
            num //= 1000
            i += 1

        return result.strip()

def test_solution():
    """
    Test driver for numberToWords solution
    Tests edge cases and regular scenarios:
    - Zero handling
    - Single digits
    - Two digits (below and above 20)
    - Hundreds
    - Thousands
    - Millions
    - Billions
    """
    solution = Solution()
    test_cases = {
        0: "Zero",
        5: "Five",
        15: "Fifteen",
        25: "Twenty Five",
        100: "One Hundred",
        123: "One Hundred Twenty Three",
        1000: "One Thousand",
        12345: "Twelve Thousand Three Hundred Forty Five",
        1000000: "One Million",
        1234567: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven",
        1000000000: "One Billion"
    }
    
    for num, expected in test_cases.items():
        result = solution.numberToWords(num)
        assert result == expected, f"Failed for {num}. Expected '{expected}', but got '{result}'"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()
