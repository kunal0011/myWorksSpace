package tree;

// Definition for a binary tree node
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}

public class IdenticalTrees {
    // Function to check if two binary trees are identical
    public static boolean isIdentical(TreeNode p, TreeNode q) {
        // Base cases
        if (p == null && q == null) {
            return true; // Both trees are empty
        }
        if (p == null || q == null) {
            return false; // One tree is empty, and the other is not
        }

        // Check if current nodes have the same value
        if (p.val != q.val) {
            return false;
        }

        // Recursively check the left and right subtrees
        return isIdentical(p.left, q.left) && isIdentical(p.right, q.right);
    }

    public static void main(String[] args) {
        // Example usage
        TreeNode tree1 = new TreeNode(1);
        tree1.left = new TreeNode(2);
        tree1.right = new TreeNode(3);

        TreeNode tree2 = new TreeNode(1);
        tree2.left = new TreeNode(2);
        tree2.right = new TreeNode(3);

        boolean result = isIdentical(tree1, tree2);
        System.out.println("The trees are identical: " + result); // Output: The trees are identical: true
    }
}
