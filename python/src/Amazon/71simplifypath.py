"""
LeetCode 71. Simplify Path

Problem Statement:
Given a string path, which is an absolute path (starting with a slash '/') to a file or directory
in a Unix-style file system, convert it to the simplified canonical path.

In a Unix-style file system:
- A period '.' refers to the current directory
- A double period '..' refers to the directory up a level
- Any multiple consecutive slashes '//' are treated as a single slash '/'
- The path must end with a single slash '/'
- The path starts with a single slash '/'

Example 1:
Input: path = "/home/"
Output: "/home"

Example 2:
Input: path = "/../"
Output: "/"
Explanation: Going one level up from root directory is not allowed.

Example 3:
Input: path = "/home//foo/"
Output: "/home/foo"
Explanation: Multiple consecutive slashes are treated as single slash.

Constraints:
- 1 <= path.length <= 3000
- path consists of English letters, digits, period '.', slash '/' or '_'
- path is a valid absolute path
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        # Split path by '/' and filter out empty strings
        components = [x for x in path.split('/') if x and x != '.']
        stack = []

        # Process each component
        for comp in components:
            if comp == '..':
                # Go up one level if possible
                if stack:
                    stack.pop()
            else:
                # Add valid directory name
                stack.append(comp)

        # Construct final path
        return '/' + '/'.join(stack)


def explain_path_simplification(path: str) -> None:
    """
    Function to explain the path simplification process step by step
    """
    print(f"\nSimplifying path: {path}")
    print("=" * 50)

    # Split and filter components
    components = [x for x in path.split('/') if x and x != '.']
    print("\nAfter splitting and filtering:")
    print(f"Components: {components}")

    stack = []
    print("\nProcessing components:")

    for i, comp in enumerate(components, 1):
        print(f"\nStep {i}: Processing '{comp}'")

        if comp == '..':
            if stack:
                removed = stack.pop()
                print(f"Found '..', going up one level (removing '{removed}')")
            else:
                print("Found '..', but already at root level")
        else:
            stack.append(comp)
            print(f"Added '{comp}' to path")

        print(f"Current stack: {stack}")
        print(f"Current path: /{'/'.join(stack)}")

    final_path = '/' + '/'.join(stack)
    print(f"\nFinal simplified path: {final_path}")
    return final_path


def visualize_path_components(path: str) -> None:
    """
    Helper function to visualize path components and their handling
    """
    print(f"\nVisualizing path components for: {path}")
    print("=" * 50)

    components = path.split('/')
    print("\nStep 1: Split by '/'")
    print(f"Components: {components}")

    filtered = [x for x in components if x and x != '.']
    print("\nStep 2: Filter out empty strings and single dots")
    print(f"Filtered: {filtered}")

    print("\nStep 3: Process each component:")
    stack = []
    for comp in filtered:
        print(f"\nProcessing: '{comp}'")
        if comp == '..':
            if stack:
                removed = stack.pop()
                print(f"  Going up one level (removing '{removed}')")
            else:
                print("  Already at root, ignoring '..'")
        else:
            stack.append(comp)
            print(f"  Adding to path")
        print(f"  Current path: /{'/'.join(stack)}")


def test_simplify_path():
    """
    Test function to verify the solution with various test cases
    """
    solution = Solution()

    test_cases = [
        {
            "path": "/home/",
            "expected": "/home",
            "description": "Simple path"
        },
        {
            "path": "/../",
            "expected": "/",
            "description": "Going up from root"
        },
        {
            "path": "/home//foo/",
            "expected": "/home/foo",
            "description": "Multiple slashes"
        },
        {
            "path": "/a/./b/../../c/",
            "expected": "/c",
            "description": "Complex path"
        },
        {
            "path": "/a/../../b/../c//.//",
            "expected": "/c",
            "description": "Very complex path"
        },
        {
            "path": "/home/user/./downloads/../documents/./files",
            "expected": "/home/user/documents/files",
            "description": "Realistic path"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        path = test_case["path"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nRunning test case {i}: {description}")
        print(f"Input path: {path}")

        result = solution.simplifyPath(path)

        assert result == expected, \
            f"\nTest case {i} failed!\nExpected: {expected}\nGot: {result}"
        print(f"✓ Test case {i} passed!")


if __name__ == "__main__":
    try:
        test_simplify_path()
        print("\nAll test cases passed successfully! 🎉")

        # Explain with detailed examples
        explain_path_simplification("/home//foo/")
        explain_path_simplification("/a/./b/../../c/")
        visualize_path_components("/home/user/./downloads/../documents")
    except AssertionError as e:
        print(f"Test failed! {str(e)}")
