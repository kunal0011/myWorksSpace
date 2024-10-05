class Solution:
    def romanToInt(self, s: str) -> int:
        # Roman numeral to integer mapping
        roman_to_int = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        total = 0
        prev_value = 0

        # Iterate through the Roman numeral string from left to right
        for char in s:
            current_value = roman_to_int[char]

            # If the previous value is smaller than the current, subtract it twice (once from the previous addition)
            if prev_value < current_value:
                total += current_value - 2 * prev_value
            else:
                total += current_value

            # Update previous value
            prev_value = current_value

        return total
