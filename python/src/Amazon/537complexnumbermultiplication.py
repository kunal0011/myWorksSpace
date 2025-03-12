"""
LeetCode 537 - Complex Number Multiplication

A complex number can be represented as a string on the form "real+imaginaryi" where:
- real is the real part and is an integer in the range [-100, 100].
- imaginary is the imaginary part and is an integer in the range [-100, 100].
- i² == -1.

Given two complex numbers num1 and num2 as strings, return a string of the complex number that represents their multiplications.

Example 1:
Input: num1 = "1+1i", num2 = "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i + i + i² = 1 + 2i - 1 = 0 + 2i

Example 2:
Input: num1 = "1+-1i", num2 = "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 - i - i + i² = 1 - 2i - 1 = 0 - 2i
"""

class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        # Parse first complex number
        real1, imag1 = self._parse_complex(num1)
        # Parse second complex number
        real2, imag2 = self._parse_complex(num2)
        
        # Multiply complex numbers: (a + bi)(c + di) = (ac - bd) + (ad + bc)i
        real_part = real1 * real2 - imag1 * imag2
        imag_part = real1 * imag2 + imag1 * real2
        
        # Format result
        return f"{real_part}+{imag_part}i"
    
    def _parse_complex(self, num: str) -> tuple[int, int]:
        """Helper function to parse complex number string into real and imaginary parts"""
        # Split at '+' and remove 'i' from imaginary part
        real_str, imag_str = num.split('+')
        return int(real_str), int(imag_str[:-1])

    def complexNumberMultiply_alternative(self, num1: str, num2: str) -> str:
        """Alternative implementation using regex for parsing"""
        import re
        
        def parse_complex(num: str) -> tuple[int, int]:
            # Use regex to extract numbers, handling optional signs
            match = re.match(r'(-?\d+)\+(-?\d+)i', num)
            if match:
                return int(match.group(1)), int(match.group(2))
            raise ValueError(f"Invalid complex number format: {num}")
        
        # Parse numbers
        real1, imag1 = parse_complex(num1)
        real2, imag2 = parse_complex(num2)
        
        # Calculate result
        real_result = real1 * real2 - imag1 * imag2
        imag_result = real1 * imag2 + imag1 * real2
        
        return f"{real_result}+{imag_result}i"


def test_complex_multiplication():
    """Test function to verify both solution approaches"""
    solution = Solution()
    
    test_cases = [
        # Basic test cases from problem description
        ("1+1i", "1+1i", "0+2i"),
        ("1+-1i", "1+-1i", "0+-2i"),
        
        # Additional test cases
        ("0+0i", "0+0i", "0+0i"),
        ("1+0i", "0+1i", "0+1i"),
        ("1+-0i", "1+0i", "1+0i"),
        ("78+-76i", "-86+72i", "-6816+-13296i"),
        ("-1+-1i", "-1+-1i", "0+2i"),
        ("100+100i", "-100+-100i", "-0+-20000i"),
        ("0+1i", "0+1i", "-1+0i"),
        ("3+-4i", "4+5i", "32+-7i")
    ]
    
    for i, (num1, num2, expected) in enumerate(test_cases, 1):
        # Test main solution
        result = solution.complexNumberMultiply(num1, num2)
        # Test alternative solution
        result_alt = solution.complexNumberMultiply_alternative(num1, num2)
        
        status = "✓" if result == expected else "✗"
        status_alt = "✓" if result_alt == expected else "✗"
        
        print(f"\nTest {i}:")
        print(f"Input: num1 = {num1}, num2 = {num2}")
        print(f"Main Solution: {status} Got: {result}")
        print(f"Alternative Solution: {status_alt} Got: {result_alt}")
        print(f"Expected: {expected}")
        
        # Additional verification: multiply the results back
        if status == "✗":
            print("Main solution failed!")
            print(f"Expected: {expected}, but got: {result}")
        if status_alt == "✗":
            print("Alternative solution failed!")
            print(f"Expected: {expected}, but got: {result_alt}")


if __name__ == "__main__":
    test_complex_multiplication()
