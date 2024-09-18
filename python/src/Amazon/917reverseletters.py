class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        letters = [ch for ch in S if ch.isalpha()]  # Extract all letters
        reversed_letters = letters[::-1]  # Reverse the list of letters

        result = []
        for ch in S:
            if ch.isalpha():
                # Replace with reversed letter
                result.append(reversed_letters.pop(0))
            else:
                result.append(ch)  # Keep non-letter characters as is

        return ''.join(result)


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    S1 = "ab-cd"
    print(sol.reverseOnlyLetters(S1))  # Expected output: "dc-ba"

    # Test case 2
    S2 = "a-bC-dEf-ghIj"
    print(sol.reverseOnlyLetters(S2))  # Expected output: "j-Ih-gfE-dCba"

    # Test case 3
    S3 = "Test1ng-Leet=code-Q!"
    print(sol.reverseOnlyLetters(S3))  # Expected output: "Qedo1ct-eeLg=ntseT!"
