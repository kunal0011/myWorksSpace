package amazon;

/**
 * Definition for a binary tree node.
 */
class TreeNode {
    int val;
    TreeNode1 left;
    TreeNode1 right;
    TreeNode(int x) { val = x; }
}

public class FindClonedBTTarget1379 {
    public final TreeNode1 getTargetCopy(final TreeNode1 original, final TreeNode1 cloned, final TreeNode1 target) {
        // If the current node is null, return null
        if (original == null) {
            return null;
        }

        // If we found the target node in the original tree, return the corresponding node in the cloned tree
        if (original == target) {
            return cloned;
        }

        // Recursively search in the left subtree
        TreeNode1 left = getTargetCopy(original.left, cloned.left, target);
        if (left != null) {
            return left;
        }

        // Recursively search in the right subtree
        return getTargetCopy(original.right, cloned.right, target);
    }

    // Example for testing:
    // Create the original and cloned trees, as well as the target node (not covered here for brevity)
}

