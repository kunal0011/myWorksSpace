package amazon;

// Definition for a binary tree node.
class TreeNode1325 {
    int val;
    TreeNode1325 left;
    TreeNode1325 right;
    TreeNode1325() {}
    TreeNode1325(int val) { this.val = val; }
    TreeNode1325(int val, TreeNode1325 left, TreeNode1325 right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class DeleteLeafNodeRecursively1325 {
    public TreeNode1325 removeLeafNodes(TreeNode1325 root, int target) {
        if (root == null) {
            return null;
        }

        // Post-order traversal: process the children first
        root.left = removeLeafNodes(root.left, target);
        root.right = removeLeafNodes(root.right, target);

        // If it's a leaf node with value equal to target, remove it
        if (root.left == null && root.right == null && root.val == target) {
            return null;
        }

        return root;
    }

    // Testing
    public static void main(String[] args) {
        TreeNode1325 root = new TreeNode1325(1,
                new TreeNode1325(2, new TreeNode1325(2), null),
                new TreeNode1325(3, new TreeNode1325(2), new TreeNode1325(4)));

        DeleteLeafNodeRecursively1325 solution = new DeleteLeafNodeRecursively1325();
        TreeNode1325 newRoot = solution.removeLeafNodes(root, 2);
        // Convert the new tree to a list (in-order traversal)
        printTree(newRoot);
    }

    // Helper function to print the tree in-order
    public static void printTree(TreeNode1325 root) {
        if (root == null) {
            return;
        }
        printTree(root.left);
        System.out.print(root.val + " ");
        printTree(root.right);
    }
}
