class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        # Parse the two complex numbers
        a, b = map(int, num1[:-1].split('+'))
        c, d = map(int, num2[:-1].split('+'))

        # Calculate the real and imaginary parts of the product
        real_part = a * c - b * d
        imaginary_part = a * d + b * c

        # Return the result in the form "real+imaginaryi"
        return f"{real_part}+{imaginary_part}i"
