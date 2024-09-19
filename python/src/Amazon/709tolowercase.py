class Solution:
    def toLowerCase(self, s: str) -> str:
        result = []
        for char in s:
            # Check if the character is uppercase
            if 'A' <= char <= 'Z':
                # Convert it to lowercase
                result.append(chr(ord(char) + 32))
            else:
                result.append(char)
        return ''.join(result)


# Test the function
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    s1 = "Hello"
    print(sol.toLowerCase(s1))  # Output: "hello"

    # Test case 2
    s2 = "LOVELY"
    print(sol.toLowerCase(s2))  # Output: "lovely"

    # Test case 3
    s3 = "here"
    print(sol.toLowerCase(s3))  # Output: "here"
