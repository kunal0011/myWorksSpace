from abc import ABC, abstractmethod
from typing import List

# Abstract Node class


class Node(ABC):
    @abstractmethod
    def evaluate(self) -> int:
        pass

# TreeNode class for both operands and operators


class TreeNode(Node):
    def __init__(self, value: str):
        self.value = value
        self.left = None
        self.right = None

    # Evaluation logic
    def evaluate(self) -> int:
        if self.value.isdigit():  # If it's a digit, return it as an integer
            return int(self.value)
        # If it's an operator, evaluate left and right nodes recursively
        left_val = self.left.evaluate()
        right_val = self.right.evaluate()

        if self.value == '+':
            return left_val + right_val
        elif self.value == '-':
            return left_val - right_val
        elif self.value == '*':
            return left_val * right_val
        elif self.value == '/':
            return left_val // right_val  # Integer division

# Solution class to build and evaluate the expression tree


class TreeBuilder:
    def buildTree(self, postfix: List[str]) -> 'Node':
        stack = []

        for token in postfix:
            if token.isdigit():
                # Operand: Create a TreeNode and push to stack
                stack.append(TreeNode(token))
            else:
                # Operator: Pop two nodes, create a TreeNode, and push back
                node = TreeNode(token)
                node.right = stack.pop()
                node.left = stack.pop()
                stack.append(node)

        # The final element in the stack is the root of the expression tree
        return stack.pop()


# Example usage and testing
if __name__ == "__main__":
    # Postfix expression: [3, 4, +, 2, *, 7, /]
    postfix = ["3", "4", "+", "2", "*", "7", "/"]

    # Build the tree
    treeBuilder = TreeBuilder()
    exprTree = treeBuilder.buildTree(postfix)

    # Evaluate the tree
    result = exprTree.evaluate()

    print(f"Result of expression: {result}")  # Should output 2
