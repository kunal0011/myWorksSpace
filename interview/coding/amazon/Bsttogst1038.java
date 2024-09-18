package amazon;

import java.util.LinkedList;
import java.util.Queue;

// Definition for a binary tree node.
 class TreeNode1038 {
    int val;
    TreeNode1038 left;
    TreeNode1038 right;
    TreeNode1038() {}
    TreeNode1038(int val) { this.val = val; }
    TreeNode1038(int val, TreeNode1038 left, TreeNode1038 right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class Bsttogst1038 {
    private int runningSum = 0;

    public TreeNode1038 bstToGst(TreeNode1038 root) {
        reverseInorder(root);
        return root;
    }

    // Reverse in-order traversal
    private void reverseInorder(TreeNode1038 node) {
        if (node == null) {
            return;
        }

        // Traverse the right subtree first
        reverseInorder(node.right);

        // Update the current node's value
        runningSum += node.val;
        node.val = runningSum;

        // Traverse the left subtree
        reverseInorder(node.left);
    }

    // Helper function to print the tree in level order (for testing purposes)
    public void printTreeLevelOrder(TreeNode1038 root) {
        if (root == null) return;
        Queue<TreeNode1038> queue = new LinkedList<>();
        queue.add(root);
        while (!queue.isEmpty()) {
            TreeNode1038 node = queue.poll();
            if (node != null) {
                System.out.print(node.val + " ");
                queue.add(node.left);
                queue.add(node.right);
            } else {
                System.out.print("null ");
            }
        }
    }

    // Testing
    public static void main(String[] args) {
        Bsttogst1038 bsttogst1038 = new Bsttogst1038();

        TreeNode1038 root = new TreeNode1038(4);
        root.left = new TreeNode1038(1);
        root.right = new TreeNode1038(6);
        root.left.left = new TreeNode1038(0);
        root.left.right = new TreeNode1038(2);
        root.left.right.right = new TreeNode1038(3);
        root.right.left = new TreeNode1038(5);
        root.right.right = new TreeNode1038(7);
        root.right.right.right = new TreeNode1038(8);

        TreeNode1038 newRoot = bsttogst1038.bstToGst(root);
        System.out.print("Java Test Result: ");
        bsttogst1038.printTreeLevelOrder(newRoot);  // Output: 30 36 21 36 35 26 15 null null null 33 null null null 8
    }
}
