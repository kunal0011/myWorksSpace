"""
LeetCode 420: Strong Password Checker

Problem Statement:
A password is considered strong if all the following rules are satisfied:
- It has at least 6 characters and at most 20 characters.
- It contains at least one lowercase letter, at least one uppercase letter, and at least one digit.
- It does not contain three repeating characters in a row.

Given a string password, return the minimum number of steps required to make password strong.
If password is already strong, return 0.

In one step, you can:
- Insert one character to password,
- Delete one character from password, or
- Replace one character of password with another character.

Constraints:
- 1 <= password.length <= 50
- password consists of English letters, digits, and symbols.
"""


def strongPasswordChecker(password: str) -> int:
    # Helper function to count missing character types
    def missing_types(s: str) -> int:
        has_lower = has_upper = has_digit = False
        for c in s:
            if c.islower():
                has_lower = True
            elif c.isupper():
                has_upper = True
            elif c.isdigit():
                has_digit = True
        return 3 - (has_lower + has_upper + has_digit)

    n = len(password)
    missing = missing_types(password)

    # Case 1: Length < 6
    if n < 6:
        return max(6 - n, missing)

    # Count repeating sequences
    replace = 0
    one_char = 0  # sequences with length % 3 == 0
    two_char = 0  # sequences with length % 3 == 1
    i = 2
    while i < n:
        if password[i] == password[i-1] == password[i-2]:
            length = 2
            while i < n and password[i] == password[i-1]:
                length += 1
                i += 1
            replace += length // 3
            if length % 3 == 0:
                one_char += 1
            elif length % 3 == 1:
                two_char += 1
        else:
            i += 1

    # Case 2: Length <= 20
    if n <= 20:
        return max(missing, replace)

    # Case 3: Length > 20
    delete = n - 20

    # Try to use deletions to reduce the number of replacements needed
    replace -= min(delete, one_char)
    replace -= min(max(delete - one_char, 0), two_char * 2) // 2
    replace -= max(delete - one_char - 2 * two_char, 0) // 3

    return delete + max(missing, replace)

# Test driver


def run_tests():
    test_cases = [
        {"password": "a", "expected": 5},
        {"password": "aA1", "expected": 3},
        {"password": "1337C0d3", "expected": 0},
        {"password": "aaa111", "expected": 2},
        {"password": "aaa123", "expected": 1},
        {"password": "aaaB1", "expected": 1},
        {"password": "ABABABABABABABABABAB1", "expected": 2}
    ]

    for i, test in enumerate(test_cases, 1):
        result = strongPasswordChecker(test["password"])
        status = "PASSED" if result == test["expected"] else "FAILED"
        print(f"Test {i}: {status}")
        print(f"Password: {test['password']}")
        print(f"Expected: {test['expected']}")
        print(f"Got: {result}\n")


if __name__ == "__main__":
    print("Running test cases for Strong Password Checker problem:\n")
    run_tests()

"""
Solution Logic Explanation:

The solution handles three main cases based on password length:

1. Length < 6:
   - Need to add characters to reach minimum length
   - Must satisfy missing character types
   - Answer is max(6 - length, missing_types)

2. Length between 6 and 20:
   - Only need to handle missing types and repeating sequences
   - Answer is max(missing_types, replacements_needed)

3. Length > 20:
   - Need to delete (length - 20) characters
   - Optimize deletions to reduce required replacements:
     a) Delete from groups of 3 repeating chars (saves one replacement per deletion)
     b) Delete from groups of 4 repeating chars (saves one replacement per two deletions)
     c) Delete from groups of 5 repeating chars (saves one replacement per three deletions)
   - Still need to satisfy missing character types

Time Complexity: O(n)
Space Complexity: O(1)

The trickiest part is handling case 3 where we need to optimize deletions to minimize 
the total operations needed.
"""
