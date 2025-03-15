"""
LeetCode 946: Validate Stack Sequences

Given two integer arrays pushed and popped each with distinct values, return true if this could have 
been the result of a sequence of push and pop operations on an initially empty stack, or false otherwise.

Constraints:
- 1 <= pushed.length <= 1000
- 0 <= pushed[i] <= 1000
- All the elements of pushed are unique
- popped.length == pushed.length
- popped is a permutation of pushed
"""

from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        pop_idx = 0
        
        # Simulate the push and pop operations
        for num in pushed:
            stack.append(num)
            
            # Try to pop while we can match with popped sequence
            while stack and pop_idx < len(popped) and stack[-1] == popped[pop_idx]:
                stack.pop()
                pop_idx += 1
                
        return len(stack) == 0

def validate_sequences(pushed: List[int], popped: List[int]) -> bool:
    """Validate input according to constraints"""
    if not 1 <= len(pushed) <= 1000:
        return False
    if len(pushed) != len(popped):
        return False
    if not all(0 <= x <= 1000 for x in pushed + popped):
        return False
    if len(set(pushed)) != len(pushed):
        return False
    return sorted(pushed) == sorted(popped)

def visualize_operations(pushed: List[int], popped: List[int]) -> None:
    """Visualize stack operations"""
    stack = []
    pop_idx = 0
    operations = []
    
    for num in pushed:
        stack.append(num)
        operations.append(f"Push {num}: {stack}")
        
        while stack and pop_idx < len(popped) and stack[-1] == popped[pop_idx]:
            value = stack.pop()
            pop_idx += 1
            operations.append(f"Pop {value}: {stack}")
    
    return operations

def test_validate_sequences():
    """Test function for Validate Stack Sequences"""
    test_cases = [
        ([1,2,3,4,5], [4,5,3,2,1], True),
        ([1,2,3,4,5], [4,3,5,1,2], False),
        ([1,2,3], [1,2,3], True),
        ([1,2,3], [3,2,1], True),
        ([1,2,3,4], [2,1,4,3], True),
        ([2,1,0], [1,2,0], False)
    ]
    
    solution = Solution()
    
    for i, (pushed, popped, expected) in enumerate(test_cases, 1):
        is_valid = validate_sequences(pushed, popped)
        result = solution.validateStackSequences(pushed, popped)
        
        print(f"\nTest case {i}:")
        print(f"Push sequence: {pushed}")
        print(f"Pop sequence: {popped}")
        print(f"Expected: {'✓' if expected else '✗'}")
        print(f"Result: {'✓' if result else '✗'}")
        print(f"Valid input: {'✓' if is_valid else '✗'}")
        print(f"Test passed: {'✓' if result == expected else '✗'}")
        
        if is_valid:
            print("\nStack operations:")
            operations = visualize_operations(pushed, popped)
            for op in operations:
                print(op)
            
        # Additional analysis
        print("\nSequence analysis:")
        print(f"Length: {len(pushed)}")
        print(f"Value range: [{min(pushed)}, {max(pushed)}]")
        inversions = sum(1 for i in range(len(popped)) for j in range(i+1, len(popped)) 
                        if popped[i] > popped[j])
        print(f"Inversions in pop sequence: {inversions}")

if __name__ == "__main__":
    test_validate_sequences()
