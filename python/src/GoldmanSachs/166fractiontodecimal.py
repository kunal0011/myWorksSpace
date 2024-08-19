class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        result = []

        # Determine the sign of the result
        if (numerator < 0) ^ (denominator < 0):
            result.append("-")

        # Convert to absolute values to avoid issues with negative numbers
        numerator = abs(numerator)
        denominator = abs(denominator)

        # Append the integer part
        integer_part = numerator // denominator
        result.append(str(integer_part))

        # Compute the remainder
        remainder = numerator % denominator

        # If there is no remainder, return the result as it is the complete decimal representation
        if remainder == 0:
            return "".join(result)

        # Otherwise, handle the fractional part
        result.append(".")

        # A dictionary to store the index of the first occurrence of a remainder
        remainder_index_map = {}

        while remainder != 0:
            # If the remainder has been seen before, then a repeating sequence is found
            if remainder in remainder_index_map:
                start_index = remainder_index_map[remainder]
                result.insert(start_index, "(")
                result.append(")")
                break

            # Store the index at which this remainder is first seen
            remainder_index_map[remainder] = len(result)

            remainder *= 10
            quotient_part = remainder // denominator
            result.append(str(quotient_part))
            remainder %= denominator

        return "".join(result)
