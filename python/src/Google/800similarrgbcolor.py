"""
LeetCode 800: Similar RGB Color

Problem Statement:
The RGB color "#AABBCC" can be written as "#ABC" in shorthand when AA=A*16+A, BB=B*16+B, and CC=C*16+C.
Given a color string color that follows the format "#AABBCC", return a string of the shorthand color "#ABC" that minimizes the sum
of the absolute difference between the decimal values of the original and shorthand colors for each component (R,G,B).

Logic:
1. For each component (RR, GG, BB):
   - Convert hex to decimal
   - Find closest value that can be represented in shorthand (multiples of 17 (0x11))
   - Round to nearest multiple of 17 since in shorthand each digit is repeated
   - Convert back to hex
2. Concatenate results with '#' prefix

Time Complexity: O(1) since we always process 3 color components
Space Complexity: O(1) constant space used
"""

from typing import List


class Solution:
    def similarRGB(self, color: str) -> str:
        def closest_component(component: str) -> str:
            # Convert the hex component to an integer
            num = int(component, 16)
            # Find the closest shorthand component
            closest_val = round(num / 17) * 17  # 17 = 0x11
            # Clamp the value to the range of hex values
            closest_val = min(255, max(0, closest_val))
            # Convert back to hex, ensuring two characters with leading zero if needed
            return '{:02x}'.format(closest_val)

        # Extract the color components (RR, GG, BB)
        r, g, b = color[1:3], color[3:5], color[5:7]

        # Find the closest shorthand for each component
        return f'#{closest_component(r)}{closest_component(g)}{closest_component(b)}'


def test_similar_rgb():
    solution = Solution()

    # Test case 1: Basic case
    color1 = "#09f166"
    result1 = solution.similarRGB(color1)
    assert result1 == "#11ff66", f"Test case 1 failed. Expected '#11ff66', got {result1}"
    print(f"Test case 1 passed: color={color1}, result={result1}")

    # Test case 2: Already in shorthand form
    color2 = "#112233"
    result2 = solution.similarRGB(color2)
    assert result2 == "#112233", f"Test case 2 failed. Expected '#112233', got {result2}"
    print(f"\nTest case 2 passed: color={color2}, result={result2}")

    # Test case 3: Edge case - all zeros
    color3 = "#000000"
    result3 = solution.similarRGB(color3)
    assert result3 == "#000000", f"Test case 3 failed. Expected '#000000', got {result3}"
    print(f"\nTest case 3 passed: color={color3}, result={result3}")

    # Test case 4: Edge case - all F's
    color4 = "#FFFFFF"
    result4 = solution.similarRGB(color4.lower())
    assert result4 == "#ffffff", f"Test case 4 failed. Expected '#ffffff', got {result4}"
    print(f"\nTest case 4 passed: color={color4}, result={result4}")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_similar_rgb()
