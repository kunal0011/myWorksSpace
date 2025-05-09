class Solution:
    def myAtoi(self, s: str) -> int:
        # Initialize the index, sign, and result
        i = 0
        sign = 1
        result = 0
        n = len(s)

        # Step 1: Ignore leading whitespaces
        while i < n and s[i] == ' ':
            i += 1

        # Step 2: Check for the sign
        if i < n and s[i] == '-':
            sign = -1
            i += 1
        elif i < n and s[i] == '+':
            i += 1

        # Step 3: Convert the digits to an integer
        while i < n and s[i].isdigit():
            digit = int(s[i])

            # Step 4: Handle overflow
            if result > (2**31 - 1 - digit) // 10:
                return 2**31 - 1 if sign == 1 else -2**31

            result = result * 10 + digit
            i += 1

        # Step 5: Apply the sign to the result
        return sign * result
