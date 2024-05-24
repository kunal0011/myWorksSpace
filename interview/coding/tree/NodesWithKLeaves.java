package tree;

public class NodesWithKLeaves {
    public static void printNodesWithKLeaves(TreeNode root, int k) {
        if (root == null) {
            return;
        }
        if (countLeaves(root) == k) {
            System.out.print(root.val + " ");
        }
        printNodesWithKLeaves(root.left, k);
        printNodesWithKLeaves(root.right, k);
    }

    private static int countLeaves(TreeNode node) {
        if (node == null) {
            return 0;
        }
        if (node.left == null && node.right == null) {
            return 1; // Node is a leaf
        }
        // Recursively count leaves in left and right subtrees
        return countLeaves(node.left) + countLeaves(node.right);
    }

    public static void main(String[] args) {
        /* Constructed binary tree is:
                   1
                 /   \
                2     3
               / \   / \
              4   5 6   7
                     \
                      8
        */
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);
        root.right.left = new TreeNode(6);
        root.right.right = new TreeNode(7);
        root.right.left.right = new TreeNode(8);

        int k = 3;
        System.out.println("Nodes with " + k + " leaves in their subtree:");
        printNodesWithKLeaves(root, k);
    }
}
