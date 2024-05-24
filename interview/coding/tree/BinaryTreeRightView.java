package tree;

import java.util.LinkedList;
import java.util.Queue;



public class BinaryTreeRightView {
    public static void rightView(TreeNode root) {
        if (root == null) {
            return;
        }

        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while (!queue.isEmpty()) {
            int levelSize = queue.size();

            for (int i = 0; i < levelSize; i++) {
                TreeNode node = queue.poll();

                // Print the rightmost node at each level
                if (i == levelSize - 1) {
                    System.out.println(node.val);
                }

                // Add the child nodes to the queue
                if (node.left != null) {
                    queue.offer(node.left);
                }
                if (node.right != null) {
                    queue.offer(node.right);
                }
            }
        }
    }

    public static void main(String[] args) {
        /* Constructed binary tree is:
                  1
                /   \
               2     3
                \   / \
                5  4   6
                  /
                 7
        */
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.right = new TreeNode(5);
        root.right.left = new TreeNode(4);
        root.right.right = new TreeNode(6);
        root.right.left.left = new TreeNode(7);

        System.out.println("Right view of the binary tree:");
        rightView(root);
    }
}
