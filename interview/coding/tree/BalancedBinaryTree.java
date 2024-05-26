package tree;



public class BalancedBinaryTree {

    // Helper class to store the height and balance status of a tree
    static class TreeInfo {
        int height;
        boolean isBalanced;

        TreeInfo(int height, boolean isBalanced) {
            this.height = height;
            this.isBalanced = isBalanced;
        }
    }

    // Main function to check if the tree is balanced
    public static boolean isBalanced(TreeNode root) {
        return checkBalance(root).isBalanced;
    }

    // Recursive function to check the balance and calculate the height of the tree
    private static TreeInfo checkBalance(TreeNode node) {
        // An empty tree is balanced and has a height of -1
        if (node == null) {
            return new TreeInfo(-1, true);
        }

        // Check the left subtree
        TreeInfo left = checkBalance(node.left);
        if (!left.isBalanced) {
            return new TreeInfo(-1, false);
        }

        // Check the right subtree
        TreeInfo right = checkBalance(node.right);
        if (!right.isBalanced) {
            return new TreeInfo(-1, false);
        }

        // Current node is balanced if the height difference is at most 1
        boolean isBalanced = Math.abs(left.height - right.height) <= 1;
        int height = Math.max(left.height, right.height) + 1;

        return new TreeInfo(height, isBalanced);
    }

    public static void main(String[] args) {
        // Example usage
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(2);
        root.left.left = new TreeNode(3);
        root.left.right = new TreeNode(3);
        root.left.left.left = new TreeNode(4);
        root.left.left.right = new TreeNode(4);

        System.out.println("Is the tree balanced? " + isBalanced(root));  // Output: false
    }
}
