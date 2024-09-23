package amazon;

// Definition for a binary tree node.
class TreeNode1325 {
    int val;
    TreeNode366 left;
    TreeNode366 right;
    TreeNode1325() {}
    TreeNode1325(int val) { this.val = val; }
    TreeNode1325(int val, TreeNode366 left, TreeNode366 right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class DeleteLeafNodeRecursively1325 {
    public TreeNode366 removeLeafNodes(TreeNode366 root, int target) {
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
        TreeNode366 root = new TreeNode366(1,
                new TreeNode366(2, new TreeNode366(2), null),
                new TreeNode366(3, new TreeNode366(2), new TreeNode366(4)));

        DeleteLeafNodeRecursively1325 solution = new DeleteLeafNodeRecursively1325();
        TreeNode366 newRoot = solution.removeLeafNodes(root, 2);
        // Convert the new tree to a list (in-order traversal)
        printTree(newRoot);
    }

    // Helper function to print the tree in-order
    public static void printTree(TreeNode366 root) {
        if (root == null) {
            return;
        }
        printTree(root.left);
        System.out.print(root.val + " ");
        printTree(root.right);
    }
}
