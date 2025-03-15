"""
LeetCode 895: Maximum Frequency Stack

Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

Implement the FreqStack class:
- FreqStack() constructs an empty frequency stack
- void push(int val) pushes an integer val onto the top of the stack
- int pop() removes and returns the most frequent element in the stack
  - If there is a tie for the most frequent element, remove the element that occurred most recently

Constraints:
- 0 <= val <= 10^9
- At most 2 * 10^4 calls will be made to push and pop
- It is guaranteed that there will be at least one element in the stack before calling pop
"""

class FreqStack:
    def __init__(self):
        self.freq_count = {}  # Value -> Frequency
        self.stack_map = {}   # Frequency -> Stack of values
        self.max_freq = 0

    def push(self, val: int) -> None:
        # Update frequency count
        self.freq_count[val] = self.freq_count.get(val, 0) + 1
        freq = self.freq_count[val]
        
        # Update max frequency
        self.max_freq = max(self.max_freq, freq)
        
        # Add to stack map
        if freq not in self.stack_map:
            self.stack_map[freq] = []
        self.stack_map[freq].append(val)

    def pop(self) -> int:
        # Get the most frequent element
        val = self.stack_map[self.max_freq].pop()
        
        # Update frequency count
        self.freq_count[val] -= 1
        
        # Update max_freq if current stack is empty
        if not self.stack_map[self.max_freq]:
            self.max_freq -= 1
            
        return val

def test_freq_stack():
    """Test function for Maximum Frequency Stack"""
    def run_test(operations, values):
        stack = FreqStack()
        results = []
        
        for op, val in zip(operations, values):
            if op == "push":
                stack.push(val)
                results.append(None)
            elif op == "pop":
                results.append(stack.pop())
                
        return results

    # Test cases
    test_cases = [
        (
            ["push","push","push","push","push","push","pop","pop","pop","pop"],
            [[5],[7],[5],[7],[4],[5],[None],[None],[None],[None]],
            [None,None,None,None,None,None,5,7,5,4]
        ),
        (
            ["push","push","push","pop","push","pop","push","pop","push","pop"],
            [[1],[2],[1],[None],[2],[None],[2],[None],[1],[None]],
            [None,None,None,1,None,2,None,2,None,1]
        )
    ]

    for i, (ops, vals, expected) in enumerate(test_cases, 1):
        print(f"\nTest case {i}:")
        print("Operations:", ops)
        print("Values:", vals)
        results = run_test(ops, vals)
        print("Expected:", expected)
        print("Got:", results)
        print("Passed:", results == expected)
        
        # Print stack state after each operation
        stack = FreqStack()
        for j, (op, val) in enumerate(zip(ops, vals)):
            if op == "push":
                stack.push(val)
                print(f"\nAfter {op}({val}):")
                print(f"Frequency count: {stack.freq_count}")
                print(f"Stack map: {stack.stack_map}")
            else:
                result = stack.pop()
                print(f"\nAfter {op}():")
                print(f"Popped: {result}")
                print(f"Frequency count: {stack.freq_count}")
                print(f"Stack map: {stack.stack_map}")

if __name__ == "__main__":
    test_freq_stack()
