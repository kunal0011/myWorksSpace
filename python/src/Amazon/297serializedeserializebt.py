"""
LeetCode 297 - Serialize and Deserialize Binary Tree

Problem Statement:
Design an algorithm to serialize and deserialize a binary tree. Serialization is the process
of converting a data structure into a sequence of bits so that it can be stored in a file
or memory buffer, or transmitted across a network connection. Deserialization reverses this
process to rebuild the tree from the sequence.

Logic:
1. Serialization:
   - Use preorder traversal (root, left, right)
   - Convert null nodes to "null" strings
   - Join all values with comma separator
2. Deserialization:
   - Split string into list of values
   - Use recursion to rebuild tree
   - Handle "null" values by returning None
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string."""
        def helper(node):
            if not node:
                return ["null"]
            # Preorder traversal
            return [str(node.val)] + helper(node.left) + helper(node.right)

        # Join the list into a string
        return ','.join(helper(root))

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        # Split the data string into list of values
        values = data.split(',')

        def helper():
            # Get the next value
            val = values.pop(0)
            if val == "null":
                return None
            # Create a new node
            node = TreeNode(int(val))
            # Recursively construct left and right subtrees
            node.left = helper()
            node.right = helper()
            return node

        return helper()

def test_codec():
    codec = Codec()
    
    def create_tree(values):
        if not values:
            return None
        root = TreeNode(values[0])
        queue = [root]
        i = 1
        while queue and i < len(values):
            node = queue.pop(0)
            if i < len(values) and values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1
            if i < len(values) and values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1
        return root
    
    def are_trees_equal(t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return (t1.val == t2.val and 
                are_trees_equal(t1.left, t2.left) and 
                are_trees_equal(t1.right, t2.right))
    
    # Test cases
    test_cases = [
        [1, 2, 3, None, None, 4, 5],  # Standard binary tree
        [1],                          # Single node
        [],                           # Empty tree
        [1, 2, 3, 4, 5, 6, 7]        # Perfect binary tree
    ]
    
    for i, values in enumerate(test_cases):
        original = create_tree(values)
        serialized = codec.serialize(original)
        deserialized = codec.deserialize(serialized)
        
        assert are_trees_equal(original, deserialized), f"Test case {i + 1} failed"
        print(f"Test case {i + 1} passed: values={values}")
        print(f"Serialized string: {serialized}")

if __name__ == "__main__":
    test_codec()
    print("All test cases passed!")
